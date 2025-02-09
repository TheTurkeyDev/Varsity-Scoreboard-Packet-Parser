import serial  # import the module

con = serial.Serial('/dev/ttyUSB0')  # open COM3
con.baudrate = 115200
con.bytesize = 8  # Number of data bits = 8
con.parity = 'N'  # No parity
con.stopbits = 1  # Number of Stop bits = 1
con.timeout = 0.001

str = ''

def handle_str(packet_str):
    if packet_str.startswith("f618ffff"):
        p1 = packet_str
        #print("p1")
    elif packet_str.startswith("f636b6"):
        p1 = packet_str
        #print("p2")
    elif packet_str.startswith("f607dc"):
        p1 = packet_str
        #print("p3")
    elif packet_str.startswith("f622dcff"): # Something score related
        p1 = packet_str
        print(p1)
    elif packet_str.startswith("f614dc"):
        p1 = packet_str
        #print("p5")
    elif packet_str.startswith("f60bdc"):
        p1 = packet_str
        #print("p6")
    elif packet_str.startswith("f60cdc"):
        p1 = packet_str
        #print("p7")
    elif packet_str.startswith("f6d6"):
        p1 = packet_str
        #print("p8")
    elif packet_str.startswith("f6c6"): #Similar to above?
        p1 = packet_str
        #print("p9")
    elif packet_str.startswith("f686"): #Full packet?
        p1 = packet_str
        #print("p10")
    elif packet_str.startswith("f6969"):
        p1 = packet_str
        #print("p11")
    else:
        print(packet_str)


while True:
    bytes = con.read(1)
    hex = bytes.hex()
    if bytes:
        str += bytes.hex()

        if str.count("f6") == 2:
            start = str.index("f6")
            nxtI = start+4
            has = str.find("f6", nxtI) != -1
            end = str.index("f6", nxtI) if has else len(str)
            packet_str = str[start: end]
            handle_str(packet_str)
            str = str[end:]

con.close()  # Close the Com port
