import serial
ser = serial.Serial('/dev/ttyACM0', 19200)  # open serial port
ser2 = serial.Serial('/dev/ttyACM1', 19200)
while True:
    try:
        
        data = ser.readline().decode().strip()  # read line of text from serial port
        data2 = ser2.readline().decode().strip()  # read line of text from serial port
        
        new_data = data + " " + data2

            
        split = new_data.split()
        list_of_values = []
        if len(new_data) >= 83:
            
            for i in split:
                
                list_of_values.append(int(i[5:len(i)]))
                
        if len(list_of_values) == 12:
            
            print(list_of_values)
            
            
            
            
            
        
    except UnicodeDecodeError: #Because the unicode error always occur upon startup, we can now
                            #Just pass if it is raised. So we don't immediately crash and can use the arduinos.
        pass
