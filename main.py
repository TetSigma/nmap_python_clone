import socket

print("\n█───█─▄▀▀─█───▄▀▀─▄▀▀▄─█▄─▄█─▄▀▀"
"\n█───█─█───█───█───█──█─█▀▄▀█─█──"
"\n█───█─█▀▀─█───█───█──█─█─▀─█─█▀▀"
"\n█▄█▄█─█───█───█───█──█─█───█─█──"
"\n─▀─▀───▀▀──▀▀──▀▀──▀▀──▀───▀──▀▀")

ip = input('Please input IP: ')
question = input('Checking one port or range?(type one or range): ')
if question == 'one':
    portone = int(input('Please input your port: '))
elif question == 'range':
    port1 = int(input('Please input first port: '))
    port2 = int(input('Please input second port: '))
else:
    print('WRONG COMMAND ERROR 1')

def port_range_checker(ip, port1, port2):
    lst = []
    for i in range(port1, port2 + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        print('Checking port ', i)
        if sock.connect_ex((ip, i)) == 0:
            lst.append(i)
            print('FOUND OPENED PORT - ', i)
        else:
            print('PORT', i, 'IS CLOSED')
    print('List of open ports: ', lst)

def port_checker(ip, portone):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(20)
    if sock.connect_ex((ip,portone)) == 0:
        print('PORT IS OPENED')


if question == 'one':
    port_checker(ip, portone)
elif question == 'range':
    port_range_checker(ip, port1, port2)