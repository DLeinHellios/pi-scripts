import subprocess

def pingSingleHost(host, packets):
    if packets < 1:
        packets = 1

    command = ['ping', '-c', str(packets), host]
    return subprocess.call(command, stdout=subprocess.DEVNULL) == 0


if __name__ == "__main__":
    print(singleHost('8.8.8.8', 1))
