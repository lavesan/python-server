import socket, sys, os
import base64
from prodPages import getBytesDistHtml
# , getIcon

# def getStringIcon():
#     with open("../qual_professor/assets/icons/1.jpg", "rb") as imageFile:
#         return base64.b64encode(imageFile.read())

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

        if 'GET' == datas[0]:
            parameter_string = datas[1].split('/')

            if ('/login' == datas[1]) | ('/' == datas[1]):
                html_bytes = getBytesDistHtml('login')
                print('entrou')
                connection.sendall(html_bytes)
            elif '/home' == datas[1]:
                html_bytes = getBytesDistHtml('home')
                connection.sendall(html_bytes)
            elif '/details' == datas[1]:
                html_bytes = getBytesDistHtml('details')
                connection.sendall(html_bytes)
            # elif 'icon' == parameter_string[1]:
            #     # O id
            #     parameter_string[2]
            #     response = 'HTTP/1.0 200 OK\r\nContent-Type: image/jpg\r\nContent-Length: ' + str(len(getStringIcon())) + '\r\n\r\n', getStringIcon()
            #     conn.sendall(bytes(response))
    finally:
        print('finalizando')