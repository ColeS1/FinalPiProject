import serial
ser = serial.Serial('/dev/ttyACM0', 19200)  # open serial port
ser2 = serial.Serial('/dev/ttyACM1', 19200)
while True:
    try:
        data = ser.readline().decode().strip()  # read line of text from serial port
        data2 = ser2.readline().decode().strip()  # read line of text from serial port
        print(data + " " + data2)  # print the data
    except UnicodeDecodeError: #Because the unicode error always occur upon startup, we can now
                            #Just pass if it is raised. So we don't immediately crash and can use the arduinos.
        pass