import socket

HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr=(SERVER,PORT)
client.connect(addr)

def send():
    mensaje=input("Digite comando a enviar: ")
    message=mensaje.encode('utf-8')
    message_length=len(message)
    send_length=str(message_length).encode('utf-8')
    send_length+=b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    
while True:
    send()
