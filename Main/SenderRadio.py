import subprocess
import pyttsx3

def radio_code(string):

    """Function that takes in the radio string and sends it to the idling micro:bit"""

    #The code variable holds the code that is sent to the idling micro:bit, where we are using the radio to send over the radio string after configuring the radio.

    code = f"""from microbit import *

import radio

radio.on()
radio.config(channel = 7, group = 1)

sleep(1000)
radio.send("{string}")
    """

    with open("main.py", "w") as f: #Opens a main.py file and with the "w" it will write on to that. If there is no existing file, then it will create a file
        f.write(code)



    # Use uflash to transfer the file to the micro:bit
    subprocess.call(["uflash", "main.py"]) #Uses the subprocess library to import the main.py file that is written using uflash onto the micro:bit

    engine = pyttsx3.init() #The text to speech engine says that the code was uploaded after the code is flashed on to the micro:bit
    UPLOADED = "The code was sent via radio."
    engine.say(UPLOADED)
    engine.runAndWait()


