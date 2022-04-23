import blinkt, time, random


def flashSingle(rgb, brightness, waitTime, reps):
    """
    Flashes a single color on and off

    Accepts a single color value, flashes between the single color and
    all pixels off

    Parameters:
    rgb (int[]): List of numbers corresponding to rgb color values
    brightness (float): light brightness value from 1.0 - 0.1
    waitTime (int): number of seconds to wait between flashes
    reps (int): number of repetitions before exiting

    """
    for rep in range(reps):
        # On
        blinkt.set_all(rgb[0],rgb[1],rgb[2],brightness)
        blinkt.show()
        time.sleep(waitTime)
        # Off
        blinkt.clear()
        blinkt.show()
        time.sleep(waitTime)


def flashMulti(rgbs, brightness, waitTime, reps, randomize):
    """
    Flashes between all colors in a list of RGB values

    Accepts a list of color values, iterates over the list, flashing all colors

    Parameters:
    rgb (int[][]): List of lists of numbers corresponding to rgb color values
    brightness (float): light brightness value from 1.0 - 0.1
    waitTime (int): number of seconds to wait between flashes
    reps (int): number of repetitions before exiting
    randomize (bool): randomize RGB values before iteration

    """
    if randomize:
        random.shuffle(rgbs)

    for rep in range(reps):
        for rgb in rgbs:
            blinkt.set_all(rgb[0],rgb[1],rgb[2],brightness)
            blinkt.show()
            time.sleep(waitTime)


if __name__ == "__main__":
    testColor1 = [220,0,0]
    testColor2 = [0,220,0]
    testColor3 = [0,0,220]
    testBrightness = .8

    print("----------------------------")
    print("fx/flash.py\n")
    print(f"playing: flashSingle({testColor1}, {testBrightness}, .5, 5)")
    flashSingle(testColor1, testBrightness, .5, 5)
    print(f"playing: flashMulti([{testColor1},{testColor2},{testColor3}], {testBrightness}, .5, 5, True)")
    flashMulti([testColor1, testColor2, testColor3], testBrightness, .5, 5, True)
    print("\n----------------------------")

