# LEGO Motor Control Script

This script allows you to control a LEGO motor using a Raspberry Pi and the Build HAT. You can specify the speed and duration for each motor control step, and the script will run the motor accordingly.

## Prerequisites

- Raspberry Pi with Build HAT installed
- Python 3.x
- buildhat library (`pip install buildhat`)
- tqdm library (`pip install tqdm`)

## Usage

1. Connect the LEGO motor to the Build HAT port 'A'.
2. Run the script using Python 3: `python legofilm.py`
3. Follow the instructions provided by the script to input the desired speed and durations for each step.

## Script Details

The script follows a state-based control flow with the following states:

- DEV: Development process
- STOP: Stop process
- FIX: Fix process
- CUSTOM: Custom process

For each state, you will be prompted to input the duration. The script will then run the motor accordingly at the specified speed. The motor direction will toggle every `switch_rotation` seconds.

During motor running, a progress bar will be displayed, indicating the elapsed time within each stage.

## Note

- Ensure that the motor is properly connected to the Build HAT and the correct port is specified in the script.

## License

This script is licensed under the [MIT License](LICENSE).
