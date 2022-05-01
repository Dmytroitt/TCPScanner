import socket
import os
os.system('cls' if os.name == 'nt' else 'clear')

mainports = [21,22,23,25,80,135,8080,443,3306] # You can edit this
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def menu():
    print '''
      $ Scan type $

[0] Heavy  - 0.4ms of ttl (all ports)
[1] Light  - 0.08 of ttl (only main ports)
[2] Custom - ex: port 0 until 80 (custom ttl)
          '''

def custom_socket_ttl():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time_to_leave = str(input('TTL (time to leave): '))  # Function linked with custom scan

def light_scan():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.08)
    ip = raw_input('[$] IP or adress: ')
    for port in mainports:
        code = client.connect_ex((ip, port))
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.08)
        if code == 0:
            print str(port)+" -> open"

def heavy_scan():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.4)
    ip = raw_input('[$] IP or adress: ')
    ports = range(65535)
    for port in ports:
        code = client.connect_ex((ip, port))
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.4)
        if code==0:
            print str(port)+" -> open"

def custom_scan():
    ip = raw_input('[$] IP or adress: ')
    first_port = int(raw_input('First port: '))
    last_port = int(raw_input('Last port: '))
    ports = range(first_port,last_port)
    custom_socket_ttl()
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code=client.connect_ex((ip, port))
        if code==0:
            print str(port)+" -> open"

menu()
user_choice = int(raw_input(': '))
if user_choice == 0:
    heavy_scan()
elif user_choice == 1:
    light_scan()
elif user_choice == 2:
    custom_scan()
else:
    print('Invalid choice!')
