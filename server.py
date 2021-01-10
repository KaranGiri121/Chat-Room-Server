import socket
import threading
SERVER=socket.gethostbyname(socket.gethostname())
PORT=9092
server=socket.socket()
server.bind((SERVER,PORT))
server.listen()
connection={}
address={}
def rev(conn,addr):
	while True:
		lenofbyte=conn.recv(1).decode('utf-8')
		bytesize=conn.recv(int(lenofbyte)).decode('utf-8')
		msg=conn.recv(int(bytesize)).decode('utf-8')
		lenofbyte=conn.recv(1).decode('utf-8')
		bytesize=conn.recv(int(lenofbyte)).decode('utf-8')
		whom=conn.recv(int(bytesize)).decode('utf-8')
		if msg=='online':
			if len(connection)==0:
				conn.send('No One Is Online'.encode('utf-8'))
			else:
				for x in address:
					conn.send(adress[x].encode('utf-8'))
		else:
			print(f'{address[addr[1]]} : {msg}')

def main():
	while True:
		conn,addr=server.accept()
		nickname=conn.recv(1024).decode('utf-8')
		address[addr[1]]=nickname
		connection[nickname]=conn
		print(f'New Client {nickname} Connect On {addr[1]}')
		rec=threading.Thread(target=rev,args=(conn,addr))
		rec.start()
main()
