import socket, sys, os
from prodPages import getBytesDistHtml

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding socket to a port
server_address = ('', 8080)
print('Iniciando servidor na porta', server_address[1])
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        data = connection.recv(16)
        data_to_string = str(data)
        datas = data_to_string.split(' ')

        if 'GET' in data_to_string:
            parameter_string = datas[1].split('/')

            if ('/login' == datas[1]) | ('/' == datas[1]):
                html_bytes = getBytesDistHtml('login')
                connection.sendall(html_bytes)
            elif '/home' == datas[1]:
                html_bytes = getBytesDistHtml('home')
                connection.sendall(html_bytes)
            elif '/details' == datas[1]:
                html_bytes = getBytesDistHtml('details')
                connection.sendall(html_bytes)
    finally:
        print('enviando dados')
