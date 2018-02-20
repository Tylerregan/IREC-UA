# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
#pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
#ledPin1 = 23 # Broadcom pin 23 (P1 pin 16)


def State_machine(turnon, switchnum):






    On_Blender = 2 # Broadcom pin 2

    Switch1 = 14 # Broadcom pin 14

    Switch2 = 15 # Broadcom pin 15

    Switch3 = 17 # Broadcom pin 17

    Switch4 = 18 # Broadcom pin 18

    Switch5 = 27 # Broadcom pin 27

    Switch6  = 22 # Broadcom pin 22



    dc = 95 # duty cycle (0-100) for PWM pin

    # Pin Setup:
    GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
    GPIO.setup(Switch1, GPIO.OUT) #  Pin 14  set as output
    GPIO.setup(Switch2, GPIO.OUT) #  Pin 15  set as output
    GPIO.setup(Switch3, GPIO.OUT) #  Pin 17  set as output
    GPIO.setup(Switch4, GPIO.OUT) #  Pin 18  set as output
    GPIO.setup(Switch5, GPIO.OUT) #  Pin 27  set as output
    GPIO.setup(Switch6, GPIO.OUT) #  Pin 15  set as output
    GPIO.setup(On_Blender, GPIO.OUT) #  Pin 2 set as output


    #May Not need this initialization of a 100 Frequency signal
    #pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
    #GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

    # Initial state for all switches
    GPIO.output(Switch1, GPIO.LOW)
    GPIO.output(Switch2, GPIO.LOW)
    GPIO.output(Switch3, GPIO.LOW)
    GPIO.output(Switch4, GPIO.LOW)
    GPIO.output(Switch5, GPIO.LOW)
    GPIO.output(Switch6, GPIO.LOW)
    GPIO.output(On_Blender, GPIO.LOW)







    print("Here we go! Press CTRL+C to exit")
    try:
        while 1:
            '''
            if GPIO.input(butPin): # button is released
                pwm.ChangeDutyCycle(dc)
                GPIO.output(ledPin1, GPIO.LOW)
            else: # button is pressed:
                pwm.ChangeDutyCycle(100-dc)
                GPIO.output(ledPin1, GPIO.HIGH)
                time.sleep(0.075)
                GPIO.output(ledPin1, GPIO.LOW)
                time.sleep(0.075)

            '''
            if (turnon  and switchnum == 1 ):
                GPIO.output(Switch1, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.HIGH)

            elif( turnon  and  switchnum == 2):
                GPIO.output(Switch2, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.HIGH)

            elif (turnon and switchnum == 3):
                GPIO.output(Switch3, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.HIGH)

            elif (turnon and switchnum == 4):
                GPIO.output(Switch4, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.HIGH)

            elif (turnon and switchnum == 5):
                GPIO.output(Switch5, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.HIGH)

            elif (turnon and switchnum == 6):
                GPIO.output(Switch6, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.HIGH)

            elif (not turnon and switchnum == 1):
                GPIO.output(Switch1, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.LOW)

            elif (not turnon and switchnum == 2):
                GPIO.output(Switch2, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.LOW)

            elif (not turnon and switchnum == 3):
                GPIO.output(Switch3, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.LOW)

            elif (not turnon and switchnum == 4):
                GPIO.output(Switch4, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.LOW)

            elif(not turnon and switchnum == 5):
                GPIO.output(Switch5, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.LOW)

            elif (not turnon and switchnum == 5):
                GPIO.output(Switch5, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.LOW)

            elif (not turnon and switchnum == 6):
                GPIO.output(Switch6, GPIO.HIGH)
                GPIO.output(On_Blender, GPIO.LOW)

            else:

                GPIO.output(On_Blender, GPIO.LOW)
                GPIO.output(Switch1, GPIO.LOW)
                GPIO.output(Switch2, GPIO.LOW)
                GPIO.output(Switch3, GPIO.LOW)
                GPIO.output(Switch4, GPIO.LOW)
                GPIO.output(Switch5, GPIO.LOW)
                GPIO.output(Switch6, GPIO.LOW)

    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        #pwm.stop() # stop PWM
        GPIO.cleanup() # cleanup all GPIO


#Call function from Terminal with 


State_machine()


