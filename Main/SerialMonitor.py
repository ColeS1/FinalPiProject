import serial
import pygame

from pygame.locals import ( #Used for any of the instances where blocks are being read and we may want to close the window (beforehand, the window took forever to close, and after this
                            #fix, it started to close immediately)
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

def serial_monitor():

    ser = serial.Serial('/dev/ttyACM0', 19200, timeout=1) #Sets for reading the serial monitor with serial port "/dev/ttyACM0" (which is typically rack with Lines 1-6). 
                                                          #Runs at a 19200 baud rate, with a timeout to allow for more accurate information.

    ser2 = serial.Serial('/dev/ttyACM1', 19200, timeout=1) #Sets for reading the serial monitor with serial port "/dev/ttyACM1" (which is typically rack with Lines 7-12).
                                                           #Runs at a 19200 baud rate, with a timeout to allow for more accurate information.

    while True:

        try:
            for event in pygame.event.get():

                if (event.type == KEYDOWN and event.key == K_ESCAPE):
                    exit()
                elif (event.type == QUIT):
                    exit()


            data = ser.readline().decode().strip() #Reads what is on the serial monitor for Rack 1-6, then sanitizes the information with the decode() and strip() functions

            data2 = ser2.readline().decode().strip() #Reads what is on the serial monitor for Rack 7-12, then sanitizes the information with the decode() and strip() functions

            
            new_data = data + " " + data2 #Concatenates the data to be used to go through analyzation

                
            split = new_data.split() #Uses the split function to create a list of the values with the data given
            list_of_values = [] #List to return once all analog values are appended

            if len(new_data) >= 83: #Checks for corruption of data (incase the data is less than what it should at minimum be (when all analog values are 0))
                
                try:

                    for i in split:
                        
                        list_of_values.append(int(i[5:len(i)])) #Goes through each of the split values. Because each string value has 5 characters in the front ("Line#")
                                                                #Then we slice the string at 5 and end at the length of the string to get the integer value of the analog value.

                except ValueError: #If there is a Value Error then that means that data was corrupted (string values where there should ONLY be integers)
                    
                    continue
                    
                if len(list_of_values) == 12: #Checks if the length of the list to be return is equal to 12. If it isn't then the loop will continue (makes sure that nothing extra is
                                              # potentially being added)
                    
                    return list_of_values
            
        except UnicodeDecodeError: #Because the unicode error always occur upon startup, we can just pass if it is raised so we don't immediately crash and can use the arduinos.
            pass
