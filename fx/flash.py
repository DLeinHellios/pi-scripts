import blinkt, time

def flashSingle(rgb, brightness, waitTime, reps):
    '''Flashes between lights out and a single color'''
    for rep in range(reps):
        blinkt.clear()
        blinkt.show()
        time.sleep(waitTime)
        blinkt.set_all(rgb[0],rgb[1],rgb[2],brightness)
        blinkt.show()
        time.sleep(waitTime)


def flashMulti(rgbs, brightness, waitTime, reps):
    '''Flashes between all colors in list of RGB values''' 
    pass #TODO

if __name__ == "__main__":
    flashSingle([220,0,0],.8,.5,5) 
