import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

IR_INPUT_PIN = 27  
IR_OUTPUT_PIN = 17
GPIO.setup(IR_INPUT_PIN, GPIO.IN)
GPIO.setup(IR_OUTPUT_PIN, GPIO.OUT)

try:
    pulse_duration_list=[]
    while True:
        while GPIO.input(IR_INPUT_PIN) == GPIO.HIGH:
            pass  
        start_time = time.time()

        while GPIO.input(IR_INPUT_PIN) == GPIO.LOW:
            pass  
        end_time = time.time()

        pulse_duration = end_time - start_time
        pulse_duration_list.append(pulse_duration)
        print(f"IR Pulse Duration: {pulse_duration:.6f} seconds")
        print(pulse_duration_list)

except KeyboardInterrupt:
    pass

# Clean up and release the GPIO pin
GPIO.cleanup()
