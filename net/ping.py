import subprocess


def pingSingleHost(host, packets):
    """
    Pings a single host, returns bool of result

    Requires sudo for "-c" option, otherwise will always return False

    Parameters:
    host (string): IP/hostname to ping
    packets (int): Number of packets to send

    Returns:
    bool: Ping success/failure

    """
    if packets < 1:
        packets = 1

    command = ['ping', '-c', str(packets), host]
    return subprocess.call(command, stdout=subprocess.DEVNULL) == 0


if __name__ == "__main__":
    testHost = "8.8.8.8"
    
    print("----------------------------")
    print("net/ping.py\n")
    print(f"call: pingSingleHost({testHost}, 1)")
    print(f"result: {pingSingleHost(testHost, 1)}\n")
    print("----------------------------")
