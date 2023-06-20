from buildhat import Motor
from time import sleep

motor = Motor('A')
# SPEED = 50

# STATE "DEV", "STOP", "FIX", "CUSTOM"
State = "DEV"

# second per switch rotation
switch_rotation = 10

# take user input for speed of motor
SPEED = int(input("What speed do you want to use? (in percent): "))

# define a function to toggle motor direction every predefined seconds for the input duration
def run_motor(duration):
    for i in range(int(duration / switch_rotation)):
        if i & 1:
            motor.run_for_seconds(switch_rotation, speed=SPEED)
        else:
            motor.run_for_seconds(switch_rotation, speed=-SPEED)
    
    motor.run_for_seconds(duration % switch_rotation, speed=SPEED)


while True:
    try:
        if State == "DEV":
            duration = input("How long for the DEV process? (in seconds): ")
            print("developing for " + duration + " seconds")
            run_motor(int(duration))
            print("DEV ended! \n")

            State = "STOP"

        elif State == "STOP":
            input("Press enter to start the STOP process")
            print("stopping for 10 seconds")
            run_motor(10)
            print("STOP ended! \n")

            State = "FIX"

        elif State == "FIX":
            input("Press enter to continue to FIX process")
            print("fixing for 3 minutes and 30 seconds")
            run_motor(210)
            print("FIX ended! \n \n All success!")
            break

    except:
        print("Error!")
        motor.stop()

        duration = input("How long for the CUSTOM process? (in seconds): ")
        print("customizing for " + duration + " seconds")
        run_motor(int(duration))
        print("CUSTOM ended! \n")

        # user select next state
        State = input("What next state do you want to use? (DEV, STOP, FIX, CUSTOM): ")
        print("Next state: " + State)
    







