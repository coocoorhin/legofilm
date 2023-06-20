from buildhat import Motor
from time import sleep, time
from tqdm import tqdm

# Create a motor object connected to port 'A' on the Build HAT
motor = Motor('A')

# Define the speed of the motor (in percent)
SPEED = int(input("What speed do you want to use? (in percent): "))

# Define the states as constants
STATE_DEV = "DEV"
STATE_STOP = "STOP"
STATE_FIX = "FIX"
STATE_CUSTOM = "CUSTOM"

# Define the duration for each state
DEV_DURATION = 10
STOP_DURATION = 10
FIX_DURATION = 210

# Define a function to toggle motor direction every predefined seconds for the input duration
def run_motor(duration, speed):
    start_time = time()
    for i in tqdm(range(duration), desc='Progress', unit='s'):
        elapsed_time = time() - start_time
        remaining_time = duration - elapsed_time
        if i % switch_rotation == 0:
            speed = -speed if speed > 0 else speed
        motor.run_for_seconds(1, speed=speed)
        sleep(min(1, remaining_time))

# Start in the DEV state
state = STATE_DEV

while True:
    try:
        if state == STATE_DEV:
            duration = int(input("How long for the DEV process? (in seconds): "))
            print("developing for", duration, "seconds")
            run_motor(duration, SPEED)
            print("DEV ended!\n")

            state = STATE_STOP

        elif state == STATE_STOP:
            input("Press enter to start the STOP process")
            print("stopping for", STOP_DURATION, "seconds")
            run_motor(STOP_DURATION, SPEED)
            print("STOP ended!\n")

            state = STATE_FIX

        elif state == STATE_FIX:
            input("Press enter to continue to FIX process")
            print("fixing for", FIX_DURATION, "seconds")
            run_motor(FIX_DURATION, SPEED)
            print("FIX ended!\n\nAll success!")
            break

    except Exception as e:
        print("Error:", str(e))
        motor.stop()

        duration = int(input("How long for the CUSTOM process? (in seconds): "))
        print("customizing for", duration, "seconds")
        run_motor(duration, SPEED)
        print("CUSTOM ended!\n")

        # User selects the next state
        state = input("What next state do you want to use? (DEV, STOP, FIX, CUSTOM): ")
        print("Next state:", state)
