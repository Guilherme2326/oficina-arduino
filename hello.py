import time
from pyfirmata import Arduino

port = 'COM3'

board = Arduino(port)

led_pin = board.get_pin('d:13:o')

while True:
    led_pin.write(1)
    time.sleep(1)
    led_pin.write(0)
    time.sleep(1)