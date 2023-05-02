import serial


def serial_monitor():

    ser = serial.Serial('COM6', 19200, timeout=1)
    ser2 = serial.Serial('COM4', 19200, timeout=1)

    while True:
        try:
            
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
