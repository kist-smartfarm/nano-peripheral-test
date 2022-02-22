# redtiger@kist.re.kr
# 
# reference: 

import RPi.GPIO as GPIO
import time

output_pins = {
    'JETSON_XAVIER': 18,
    'JETSON_NANO': 33, # GPIO32 : PWM0, GPIO33 : PWM2 
    'JETSON_NX': 33,
    'CLARA_AGX_XAVIER': 18,
    'JETSON_TX2_NX': 32,
}

output_pin = output_pins.get(GPIO.model, None)
if output_pin is None:
    raise Exception('PWM not supported on this board')

def test_motor():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    p = GPIO.PWM(output_pin, 50)
    val = 0
    incr = 1
    p.start(val)

    print("PWM for survo is running. Press CTRL+C to exit.")
    try:
        for i in range(20):
            time.sleep(0.5)
            if val >= 10:
                incr = -incr
            if val <= 0:
                incr = -incr
            val += incr
            p.ChangeDutyCycle(val) 
            #TODO : find proper value for PWM after setting external power supply. 
    finally:
        print("Exiting")
        p.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    test_motor()
