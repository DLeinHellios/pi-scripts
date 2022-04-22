import blinkt, time


def fadeIn(rgb, maxBrightness):
    """
    Fades a single color in from darkness

    Accepts a single color value, sets all pixels to that value and gradually
    increases brightness until reaching max value

    Parameters:
    rgb (int[]): List of numbers corresponding to rgb color values
    maxBrightness (float): max brightness value from 0.1 - 1.0

    """
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
    """
    Fades a single color out to darkness

    Accepts a single color value, sets all pixels to that value and gradually
    decreasing brightness until lighting is off

    Parameters:
    rgb (int[]): List of numbers corresponding to rgb color values
    startBrightness (float): starting brightness value from 1.0 - 0.1

    """
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
    testColor = [255,255,255]
    testBrightness = .8

    print("----------------------------")
    print("fx/fade.py\n")
    print(f"playing: fadeIn({testColor}, {testBrightness})")
    fadeIn(testColor, testBrightness)
    time.sleep(5)
    print(f"playing: fadeOut({testColor}, {testBrightness})")
    fadeOut(testColor, testBrightness)
    print("\n----------------------------")
