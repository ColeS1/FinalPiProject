import RPi.GPIO as GPIO

def buttons():

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

    argument_list = []

    RUNNING = True

    while RUNNING:
        
        for i in buttons:
            
            if GPIO.input(i) == True:
                
                if i == 12:

                    RUNNING = False
                    return argument_list
                
                else:

                    argument_list.append(button_vals[i])
