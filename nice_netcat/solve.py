import socket

HOST = 'mercury.picoctf.net'
PORT = 21135

# grab data from the service
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    s.close()

# the data received is in a bytestring
# first decode it to a utf8 string
data = data.decode('utf-8')

# the data is a series of ASCII codes separated by newline characters
# split the string into an array so we can iterate over it and convert each
# ASCII code to its corresponding character to assemble the flag
lines = data.split('\n')
for line in lines:
    if line:
        character = chr(int(line))
        print(character, end='')