import RPi.GPIO as GPIO
import time
GPIO_NO = 27
# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 17 as an input
GPIO.setup(GPIO_NO, GPIO.IN)

try:
    while True:
        # Read the state of GPIO pin 17
        input_state = GPIO.input(GPIO_NO)
        
        print(f"Value: {input_state}"
        
        # Delay for a short period to avoid busy-waiting
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

# Clean up and release the GPIO pins
GPIO.cleanup()
