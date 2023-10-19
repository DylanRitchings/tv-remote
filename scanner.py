import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 17 as an input
GPIO.setup(17, GPIO.IN)

try:
    while True:
        # Read the state of GPIO pin 17
        input_state = GPIO.input(17)
        
        if input_state == GPIO.HIGH:
            print("GPIO 17 is HIGH")
        else:
            print("GPIO 17 is LOW")
        
        # Delay for a short period to avoid busy-waiting
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

# Clean up and release the GPIO pins
GPIO.cleanup()
