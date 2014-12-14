import struct

with open(r'C:\Users\bob\Desktop\file.pcap', 'rb') as f:
     data = f.read()

print struct.unpack("I", data[40:])
