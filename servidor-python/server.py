import socket, sys, os, struct, json
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
            elif '/icon' == datas[1]:
                obj = { 'name': 'Alguém ai', 'idade': 23 }
                msg = json.dumps(obj).encode('utf-8')
                frmt = "=%ds" % len(msg)
                packedMsg = struct.pack(frmt, msg)
                packedHdr = struct.pack('=I', len(packedMsg))
    
                print(packedMsg)
                print(packedHdr)
                # self._send(packedHdr)
                # self._send(packedMsg)
                sent = 0
                sent2 = 0
                while sent < len(packedHdr):
                    sent += connection.send(packedHdr[sent:])
                while sent2 < len(packedMsg):
                    sent2 += connection.send(packedMsg[sent2:])
            #     # O id
            #     parameter_string[2]
            #     response = 'HTTP/1.0 200 OK\r\nContent-Type: image/jpg\r\nContent-Length: ' + str(len(getStringIcon())) + '\r\n\r\n', getStringIcon()
            #     conn.sendall(bytes(response))
    finally:
        print('finalizando a conexão')
        connection.close()