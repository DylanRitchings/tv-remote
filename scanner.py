import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin connected to the IR receiver as an input
IR_PIN = 27  # Replace with the GPIO pin number you're using
GPIO.setup(IR_PIN, GPIO.IN)

try:
    while True:
        while GPIO.input(IR_PIN) == GPIO.HIGH:
            pass  # Wait for the start of the IR signal
        start_time = time.time()

        while GPIO.input(IR_PIN) == GPIO.LOW:
            pass  # Wait for the end of the start pulse
        end_time = time.time()

        pulse_duration = end_time - start_time
        print(f"IR Pulse Duration: {pulse_duration:.6f} seconds")

except KeyboardInterrupt:
    pass

# Clean up and release the GPIO pin
GPIO.cleanup()
