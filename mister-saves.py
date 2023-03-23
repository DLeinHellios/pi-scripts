# mister-saves.py - backs up MiSTer FPGA saves via FTP
import net, config
import time, datetime, os, shutil
from ftplib import FTP

def main():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    
    settings = config.read_config('mister-saves')
    time.sleep(30) # Wait for network

    while True:
        success = False
        for mister in settings['misters']:
            # Check internet connection
            try:
                alive = net.pingSingleHost(mister['ip-address'],1)
            except:
                alive = False

            if alive:
                # Connect to FTP
                try:
                    ftp = FTP(mister['ip-address'])
                    ftp.login(mister['credentials']['user'], mister['credentials']['password'])
                    print(f"Connected to MiSTer {mister['name']} at {mister['ip-address']}")
                except:
                    print(f"Error connecting to MiSTer {mister['name']} at {mister['ip-address']}")
                    break

                # Download saves
                try:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H%M%S")
                    downloadPath = f"{settings['download-location']}/{mister['name']}/{timestamp}"
                    os.makedirs(downloadPath)
                    print(f"Downloading saves to {downloadPath}")
                    ftp.cwd("/media/fat/saves")
                    cores = ftp.nlst()
                    cores.sort()
                    for core in cores:
                        if core in settings['exclude-cores']:
                            print(f"> Skipping core '{core}'")
                            continue
                        ftp.cwd(f"/media/fat/saves/{core}")
                        savelist = ftp.nlst()
                        if len(savelist):
                            os.makedirs(f"{downloadPath}/{core}")
                            for savefile in ftp.nlst():
                                ftp.retrbinary('RETR ' + savefile, open(f"{downloadPath}/{core}/{savefile}", 'wb').write)
                            print(f"Saves for core '{core}' downloaded successfully")
                    success = True
                except:
                    # Cleanup failed downloads
                    try:
                        if os.path.isdir(downloadPath):
                            shutil.rmtree(downloadPath)
                        print(f"Error downloading saves from MiSTer {mister['name']} at {mister['ip-address']}")
                        continue
                    except:
                        continue

                # Prune extra backups
                try:
                    backupList = os.listdir(f"{settings['download-location']}/{mister['name']}")
                    backupList.sort(reverse=True)
                    if len(backupList) > settings['retain-versions']:
                        for version in backupList[3:]:
                            shutil.rmtree(f"{settings['download-location']}/{mister['name']}/{version}")
                    print("Successfully pruned old versions")
                except:
                    print("Error pruning backups")

                # If we're only checking aliases of a single MiSTer
                if not settings['multiple-misters']:
                    break 
                
        if success and not settings['multiple-misters']:
            print(f"Saves written successfully, sleeping for {settings['long-delay-seconds']} seconds")
            time.sleep(settings['long-delay-seconds'])
        else:
            time.sleep(settings['short-delay-seconds'])


if __name__ == "__main__":
    main()
