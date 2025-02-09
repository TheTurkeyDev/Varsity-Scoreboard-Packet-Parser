import serial  # import the module

con = serial.Serial('/dev/ttyUSB0')  # open COM3
con.baudrate = 115200
con.bytesize = 8  # Number of data bits = 8
con.parity = 'N'  # No parity
con.stopbits = 1  # Number of Stop bits = 1
con.timeout = 0.1


def handle_packet(header, length, data):
    if length == '22':
        n = 2
        # This is not effecient. Really should use the byte array and not the hex string
        parts = [data[i:i+n] for i in range(0, len(data), n)]
        print("tt: " + parts[0])
        print("uu: " + parts[1])
        print("uu: " + parts[1])
        print("pp: Counter?: " + parts[5])
        print("aa: Home Score: " + parts[9])
        print("bb: Away Score: " + parts[10])
        print("cc: Home Shots: " + parts[11])
        print("dd: Away Shots: " + parts[12])
        print("ee: Home Goal: " + parts[13])
        print("ff: Away Goal: " + parts[14])
        print("gg: Period: " + parts[15])
        print("hh: H Pen 1: " + parts[25])
        print("ii: H Pen 2: " + parts[26])
        print("jj: A Pen 1: " + parts[27])
        print("kk: A Pen 2: " + parts[28])
        print("ll: H Pen Ind: " + parts[29])
        print("mm: A Pen Ind: " + parts[30])
        print("yy: Checksum?: " + parts[32])


try:
    while True:
        header = con.read(1).hex()
        if header == 'f6':
            lengthHex = con.read(1).hex()
            if lengthHex == '':
                continue
            length = int(lengthHex, 16)
            data = con.read(length - 1).hex()
            print(header + lengthHex + data)
            #handle_packet(header, lengthHex, data)
        elif header != "":
            print("None f6 recieved! " + header)
except KeyboardInterrupt:
    con.close()  # Close the Com port
