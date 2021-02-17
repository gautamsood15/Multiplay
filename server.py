import socket
from _thread import *
import sys


server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(2)     # allows only 2 people to connect to server

print("Waiting for a connection, Server Started")





