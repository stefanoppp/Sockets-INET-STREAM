import socket   
import threading
import subprocess
import time
HEADER=64
SERVER=socket.gethostbyname(socket.gethostname())
PORT=5050
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    connected=True
    print('Nueva conexion')
    horarios_comandos=[]
    comandos=[]
    
    while connected:
        
        msg_length=conn.recv(HEADER).decode('utf-8')
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode('utf-8')
            if msg=='quit':
                connected=False
                break
            else:
                comando=msg
                salida=subprocess.call(msg,shell=True) 
                horario_comando= time.strftime("%c")
                horarios_comandos.append(horario_comando)
                comandos.append(comando)
                print(salida)
    print('Comandos y su horario: ')
    for i in zip(comandos, horarios_comandos):
        print(i[0],i[1])


def start():
    server.listen()
    while True:
        conn, addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
print('Servidor iniciado')
start()