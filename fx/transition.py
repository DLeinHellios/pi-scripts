import blinkt, random, time


def twinkle(rgbs, brightness, reps, randomize):
    """
    Twinkle transition between an array of rgb lists

    Accepts a list of color values, transitions between colors in the list, in order,
    by setting a single pixel to the next color until all pixels are set

    Parameters:
    rgb (int[][]): List of lists of numbers corresponding to rgb color values
    brightness (float): light brightness value from 1.0 - 0.1
    reps (int): number of repetitions before exiting
    randomize (bool): randomize pixel order before iteration

    """
    blinkt.set_all(rgbs[0][0], rgbs[0][1], rgbs[0][2], brightness)
    for rep in range(reps):
        for color in rgbs:
            pixelIndx = list(range(0,8))
            if randomize:
                random.shuffle(pixelIndx)

            for pxl in range(len(pixelIndx)):
                   blinkt.set_pixel(pixelIndx.pop(), color[0], color[1], color[2], brightness)
                   blinkt.show()
                   time.sleep(.01)
        

if __name__ == "__main__":
    testColor1 = [220,0,0]
    testColor2 = [0,220,0]
    testColor3 = [0,0,220]
    testBrightness = .8

    print("----------------------------")
    print("fx/transition.py\n")
    print(f"playing: twinkle([{testColor1}, {testColor2}, {testColor3}], {testBrightness}, 3, True)")
    twinkle([testColor1, testColor2, testColor3], testBrightness, 3, True)
    print("\n----------------------------")
