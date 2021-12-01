import blinkt, time

def fadeIn(rgb, maxBrightness):
    if maxBrightness <= 0 or maxBrightness > 1:
        maxBrightness = 1

    brightness = 0
    blinkt.set_all(rgb[0], rgb[1], rgb[2], brightness)
    blinkt.show()

    while brightness < maxBrightness and brightness <= .9:
        brightness += 0.1
        blinkt.set_brightness(brightness)
        blinkt.show()
        time.sleep(.0001)

    blinkt.set_all(0,0,0,maxBrightness)


def fadeOut(rgb, startBrightness):
    if startBrightness <= 0 or startBrightness > 1:
        startBrightness = 1

    brightness = startBrightness
    blinkt.set_all(rgb[0], rgb[1], rgb[2], brightness)
    blinkt.show()
    
    while brightness >= 0.1:
        brightness -= 0.1
        blinkt.set_brightness(brightness)
        blinkt.show()
        time.sleep(.0001)


if __name__ == "__main__":
    fadeIn([120,40,0],.8)
    time.sleep(10)
    fadeOut([120,40,0],.8)
