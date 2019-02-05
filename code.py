# Helpful Links
# -------------
# https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/blob/master/adafruit_circuitplayground/express.py
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
from adafruit_circuitplayground.express import cpx
import time
import board
import microcontroller
import digitalio
import busio
import adafruit_mpl3115a2

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

# ######################################################################################################
# Checks if Circuit Playground is in read/write mode
# ######################################################
def cpxWriteMode():
    switch = cpx.switch
    if switch == False:
        # CPx can write to the storage
        cpx.red_led = True
        return True
    else:
        # Computer can write to the storage
        cpx.red_led = False
        return False
# ######################################################

# ######################################################################################################
# Gets altitude from MPL3115A2
# Links:
#    Tutorial: https://github.com/adafruit/Adafruit_CircuitPython_MPL3115A2/blob/master/examples/simpletest.py
#    Weather: https://forecast.weather.gov/MapClick.php?lat=40.8764&lon=-73.6029#.XFj_BVxKhaQ
# ######################################################
def get_altitude():
    PRESSURE_SEA_LEVEL_PASCALS = 101626

    # Initialize the I2C bus.
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize the MPL3115A2.
    sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

    # Set this to a value in pascals:
    sensor.sealevel_pressure = PRESSURE_SEA_LEVEL_PASCALS

    print('*** BEGIN MEASUREMENTS ***')

    if cpxWriteMode():
        logger = open("/log.txt", "a")

    while True:
        altitude = sensor.altitude
        print('Altitude: {0:0.3f} meters'.format(altitude))

        if cpxWriteMode():
            logger.write('Altitude: {0:0.3f} meters\r\n'.format(altitude))
            logger.flush()

        time.sleep(0.2)

        if cpx.button_a == True and cpx.button_b == True:
            print('*** END MEASUREMENTS ***')

            if cpxWriteMode():
                logger.write('*** END MEASUREMENTS ***')
                logger.flush()
                logger.close()

            break

# ######################################################


#true = read and write

# if cpx.switch == False:
#     cpx.red_led = True

#get_temperature()
get_altitude()
