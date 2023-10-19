from gpiozero import DigitalInputDevice
import time

# Define the GPIO pin connected to the IR receiver
ir_pin = 18  # Replace with the appropriate GPIO pin

# Create a DigitalInputDevice for the IR receiver
ir_receiver = DigitalInputDevice(ir_pin, pull_up=False)

try:
    while True:
        # Wait for a falling edge (IR signal received)
        ir_receiver.wait_for_active()
        start_time = time.time()

        # Wait for a rising edge (IR signal ended)
        ir_receiver.wait_for_inactive()
        end_time = time.time()

        # Calculate the duration of the IR signal
        signal_duration = end_time - start_time
        print(f"IR Signal Duration: {signal_duration} seconds")

except KeyboardInterrupt:
    pass

# Cleanup (not always required, depending on your platform)
ir_receiver.close()

