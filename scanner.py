import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the IR receiver
ir_pin = 13

# Set the GPIO pin as an input
GPIO.setup(ir_pin, GPIO.IN)

try:
    while True:
        # Wait for a falling edge (IR signal received)
        GPIO.wait_for_edge(ir_pin, GPIO.FALLING)
        
        # Record the start time
        start_time = time.time()
        
        # Wait for a rising edge (IR signal ended)
        GPIO.wait_for_edge(ir_pin, GPIO.RISING)
        
        # Record the end time
        end_time = time.time()
        
        # Calculate the duration of the IR signal
        signal_duration = end_time - start_time
        
        # You can add your own logic to handle the IR signal duration
        print(f"IR Signal Duration: {signal_duration} seconds")
        
except KeyboardInterrupt:
    pass

# Clean up GPIO
GPIO.cleanup()
