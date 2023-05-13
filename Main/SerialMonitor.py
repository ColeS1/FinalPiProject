import serial
import pygame

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

def serial_monitor():

    ser = serial.Serial('/dev/ttyACM0', 19200, timeout=1)
    ser2 = serial.Serial('/dev/ttyACM1', 19200, timeout=1)

    while True:
        try:
            for event in pygame.event.get():

                if (event.type == KEYDOWN and event.key == K_ESCAPE):
                    exit()
                elif (event.type == QUIT):
                    exit()


            data = ser.readline().decode().strip()
            data2 = ser2.readline().decode().strip()

            
            new_data = data + " " + data2

                
            split = new_data.split()
            list_of_values = []
            if len(new_data) >= 83:
                
                try:
                    for i in split:
                        
                        list_of_values.append(int(i[5:len(i)]))

                except ValueError:
                    
                    continue
                    
                if len(list_of_values) == 12:
                    
                    return list_of_values
                
                
                
                
                
            
        except UnicodeDecodeError: #Because the unicode error always occur upon startup, we can now
                                #Just pass if it is raised. So we don't immediately crash and can use the arduinos.
            pass
