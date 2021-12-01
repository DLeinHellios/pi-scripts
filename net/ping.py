import subprocess

def singleHost(host, packets):
    if packets < 1:
        packets = 1

    command = ['ping', '-c', str(packets), host]
    return subprocess.call(command) == 0

if __name__ == "__main__":
    print(singleHost('192.168.1.1', 1))

