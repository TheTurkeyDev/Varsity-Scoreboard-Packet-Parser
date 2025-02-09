import serial  # import the module

con = serial.Serial('/dev/ttyUSB0')  # open COM3
con.baudrate = 115200
con.bytesize = 8  # Number of data bits = 8
con.parity = 'N'  # No parity
con.stopbits = 1  # Number of Stop bits = 1
con.timeout = 0.001

str = ''


def handle_str(packet_str):
    if packet_str.startswith("f607"):
        print("07")


try:
    while True:
        header = con.read(1).hex()
        if header == 0xf6:
            lengthHex = con.read(1).hex()
            length = int(lengthHex, 16)
            data = con.read(length - 1).hex()
            print("f6" + lengthHex + data)
        else:
            print("None f6 recieved! " + header)
except KeyboardInterrupt:
    con.close()  # Close the Com port
