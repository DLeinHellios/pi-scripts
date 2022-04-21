import fx, net
import time

rgb = fx.sequences['oranges'] # List of [r,g,b] values for lighting effects 
host = "192.168.1.55" # Main IP to be monitored (open pings for Win10)

def main():
    time.sleep(30) # Wait for network
    hasNet = False
    isOn = False
    while True:
        try:
            hasNet = net.pingSingleHost('google.com',1)
        except:
            hasNet = False

        try:    
            isOnline = net.pingSingleHost(host,1)
        except:
            isOnline = False

        if not hasNet:
            # No network, flash warning
            fx.flashSingle([255,0,0],.8,.5,30)
        else:    
            if isOnline and not isOn:
                # Turn on
                fx.fadeIn(rgb[0], .7)
                isOn = True
            elif isOnline:
                # Play animation 
                fx.twinkle(rgb, .8, 10, True)
            elif isOn:
                # Turn off
                fx.fadeOut(rgb[0], .7)
                isOn = False
            else:
                time.sleep(5)


if __name__ == "__main__":
    main()
