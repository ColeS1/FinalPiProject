import subprocess
import pyttsx3

def radio_code(string):

    code = f"""from microbit import *

import radio

radio.on()
radio.config(channel = 7, group = 1)

sleep(1000)
radio.send("{string}")
    """

    with open("main.py", "w") as f:
        f.write(code)



    # Use uflash to transfer the file to the micro:bit
    subprocess.call(["uflash", "main.py"])

    engine = pyttsx3.init()
    UPLOADED = "The code was sent via radio."
    engine.say(UPLOADED)
    engine.runAndWait()


