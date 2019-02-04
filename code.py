# Helpful Links
# -------------
# https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/blob/master/adafruit_circuitplayground/express.py
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
from adafruit_circuitplayground.express import cpx
import time
import board
import microcontroller
import digitalio

def get_temperature():
    counter = 1
    with open('temperature.csv', 'a') as fp:
        print('counter, temperature')
        fp.write('counter, temperature')
        while True:
            print('%d,%d\n' % (counter, cpx.temperature))
            fp.write('%d,%d\n' % (counter, cpx.temperature))
            fp.flush()
            counter += 1
            time.sleep(1)
            if cpx.button_a == True and cpx.button_b == True:
                print('Both buttons are pressed.')
                break

#true = read and write

# if cpx.switch == False:
#     cpx.red_led = True

get_temperature()