import socket # import required libraries
import time

''' this script sends a UDP packet to port 53000 containing a hi-res timestamp '''

UDP_IP = "localhost" # use loopback address ( localhost is an alias for 127.0.0.1 )
UDP_PORT = 53000 # chose a random UDP port ( ~ 50000 - 65535)
TIMESTAMP = str(time.time())
MESSAGE = bytes(TIMESTAMP,"ASCII")  # convert TIMESTAMP into bytes to send as a packet 
                                    # (encoded in ASCII protocol rather than UTF-8, for speed)

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # initialize UDP socket object
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT)) # send MESSAGE