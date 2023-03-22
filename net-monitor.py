# net-monitor.py - monitors a single host + internet connection to display simple lighting effect
import fx, net, config
import time, os

def main():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    settings = config.read_config('net-monitor')
    rgb = fx.sequences[settings['color-sequence']]
    hasNet = False
    isOn = False
    time.sleep(30) # Wait for network

    while True:
        # Check internet connection
        try:
            hasNet = net.pingSingleHost('8.8.8.8',1)
        except:
            hasNet = False

        # Check desired host
        try:    
            isOnline = net.pingSingleHost(settings['monitor-ip'],1)
        except:
            isOnline = False

        # Take action on net results
        if not hasNet:
            # No network, flash warning
            fx.flashSingle([255,0,0],.8,.5,20)
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
