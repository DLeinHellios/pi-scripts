import fx, net
import time

rgb = [140, 40, 0]
host = "192.168.1.35"

def main():
    isOn = False
    while True:
        isOnline = net.pingSingleHost(host,1)

        if isOnline and not isOn:
            # Turn on
            fx.fadeIn(rgb, .8)
            isOn = True
        elif isOnline:
            # Keep on
            time.sleep(5)
        elif isOn:
            # Turn off
            fx.fadeOut(rgb, .8)
            isOn = False
        else:
            time.sleep(5)

if __name__ == "__main__":
    main()
