from microbit import *

import radio

radio.on()
radio.config(channel = 7)

sleep(1000)

print("micro:bit radio sender")

while True:
    string = "f4r89wpx34r5"
    message = string

    print("Send: ", message)
    
    radio.send(message)
    
    print("Done!")

    sleep(2000)