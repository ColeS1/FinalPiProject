import RPi.GPIO as GPIO
from time import sleep
buttons = [17, 16, 13, 12, 6, 5, 4, 27, 26, 25, 24, 23, 22, 21, 20, 19]

button_vals = {17: "1",
               16: "2",
               13: "3",
               6: "4",
               5:"5",
               4: "6",
               26: "7",
               25: "8",
               24: "9",
               22: "<",
               21: "0",
               20: ">",
               27: "Run",
               12: "Lock",
               23: "Read",
               19: "Dist"}

GPIO.setmode(GPIO.BCM)

GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    
    for i in buttons:
        
        if GPIO.input(i) == True:
            
            print(button_vals[i])
            sleep(0.2)
            
            
