import blinkt, random, time, fx.colors

def twinkle(rgbs, brightness, reps, randomize):
    '''Twinkle transition between an array of rgb lists'''
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
    twinkle(colors.sequences['rainbow1'], .8, 3, True)
