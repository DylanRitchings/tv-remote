import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

IR_INPUT_PIN = 27  
IR_OUTPUT_PIN = 17
GPIO.setup(IR_INPUT_PIN, GPIO.IN)
GPIO.setup(IR_OUTPUT_PIN, GPIO.OUT)

def ir_input():
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

ir_output_list = [0.009032011032104492, 0.0005812644958496094, 0.0005795955657958984, 0.0006098747253417969, 0.0006024837493896484, 0.0005953311920166016, 0.0006110668182373047, 0.0006051063537597656, 0.0005955696105957031, 0.0006074905395507812, 0.0005819797515869141, 0.0006053447723388672, 0.0006053447723388672, 0.0006053447723388672, 0.0006091594696044922, 0.0006108283996582031, 0.0005810260772705078, 0.0006089210510253906, 0.0006067752838134766, 0.0006051063537597656, 0.0005819797515869141, 0.0006062984466552734, 0.0006074905395507812, 0.0006043910980224609, 0.0006082057952880859, 0.0006039142608642578, 0.0006043910980224609, 0.0006079673767089844, 0.0005807876586914062, 0.0006091594696044922, 0.0006086826324462891, 0.0006074905395507812, 0.0006058216094970703, 0.0006062984466552734, 0.009046792984008789, 0.0006046295166015625]
def ir_output():
    try:
        for pulse_length in ir_output_list:
            GPIO.output(IR_OUTPUT_PIN, 1)
            time.sleep(pulse_length)
            print(pulse_length)
            GPIO.output(IR_OUTPUT_PIN, 0)
    except KeyboardInterrupt:
        pass
            
ir_input()

    # Clean up and release the GPIO pin
GPIO.cleanup()





