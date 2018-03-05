# External library imports
import RPi.GPIO as GPIO
from time import sleep
import sys, traceback





def ignition_protocol():
    Input_IgnitionSwitch = 5 # Broadcom pin 5
    Output_IgnitionSwitch = 1 # Broadcom pin 1
    Output_LED = 7  # Broadcom pin 3
    Heating_Element_Signal = 11   # Broadcom pin 11
    Primary_Valve_Signal = 13  # Broadcom pin 13
    Stepper_Input = 15 # Broadcom pin 15
    Kill_Process =  False
    Get_Verification = False
    Operator_Control_Signal = 19 # Broadcom pin 19

    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # Broadcom pin-numbering scheme
    GPIO.setup(Input_IgnitionSwitch, GPIO.IN)  # Pin 5  set as input
    GPIO.setup(Output_IgnitionSwitch, GPIO.OUT)  # Pin 3  set as output
    GPIO.setup(Output_LED, GPIO.OUT)
    GPIO.setup(Heating_Element_Signal, GPIO.OUT)
    GPIO.setup(Primary_Valve_Signal, GPIO.OUT)
    GPIO.setup(Stepper_Input, GPIO.OUT)
    GPIO.setup(Operator_Control_Signal, GPIO.IN)



    #Initial settings for all the GPIO-PINS
    GPIO.output(Output_IgnitionSwitch, GPIO.HIGH)
    GPIO.output(Heating_Element_Signal, GPIO.LOW)
    GPIO.output(Output_LED, GPIO.LOW)
    GPIO.setup(Operator_Control_Signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(Primary_Valve_Signal, GPIO.LOW)



    while(Get_Verification == False):



        Answer = int(input("Do you want to begin the rocket bench test sequence (1 or 0)"))

        if(Answer == 1):
            Get_Verification = True



        elif(Answer == 0):
            print("Shutdown requested...exiting")
            sys.exit(0)

        else:
            print("Wrong Input please enter 1 for ignition sequence to begin and 0 to exit")


    print("Countdown to ignition beginning")
    for x in range(20, -5, -1):
        if(x > 15 ):
            print(x + " seconds till ignition sequence")


        elif(x > 10):
            if (x == 10):
                print("Start of Auto Sequence" + "Ignition beginning in 10 seconds")
            else:
                print(x + " seconds till ignition sequence")

        elif(x == 5):
            while(GPIO.input(Operator_Control_Signal) == True ):
                print("Operator turn switch in the on position to energize control system power")
                sleep(1)

        elif(x == 0):

            print("Ignition Circuit is closing to ignite solid starter motor")
            GPIO.output(Heating_Element_Signal, GPIO.HIGH)

        elif(x == -1):

            print("N2O flow beginning, closing circuit for valve relay")
            GPIO.output( Primary_Valve_Signal, GPIO.HIGH)

        elif (x == -2):

            print("Ignition Circuit is opening de-energizing ignition wire")
            GPIO.output(Heating_Element_Signal, GPIO.LOW)

        elif (x == -5):

            print("Ignition Circuit is opening de-energizing ignition wire")
            GPIO.output(Heating_Element_Signal, GPIO.LOW)


        sleep(1)



    print("Here we go! Press CTRL+C to exit")
    try:
        while 1:

            if GPIO.input(Input_IgnitionSwitch) and not  Kill_Process:
                GPIO.output(Output_LED, GPIO.HIGH)
                GPIO.output( Heating_Element_Signal, GPIO.HIGH) #This turns on the heating element relay signal
                sleep(3) # Have heating element on for 3 seconds before turning it off
            else:
                GPIO.output(Output_LED, GPIO.LOW)
                GPIO.output(Heating_Element_Signal, GPIO.LOW)






    except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
        # pwm.stop() # stop PWM
        GPIO.cleanup()  # cleanup all GPIO
        sys.exit(0) #system exit


    return


def main():



    ignition_protocol()

    return 0


main()