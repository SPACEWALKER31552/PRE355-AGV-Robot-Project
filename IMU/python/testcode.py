import time 
import board
import digitalio
 
led = digitalio.DigitalInOut(board.SCL)
led.direction = digitalio.Direction.OUTPUT
while True:
  led.value = True
  time.sleep(0.1)
  led.value = False 
  time.sleep(0.1)
