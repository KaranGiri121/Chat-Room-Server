import socket
import threading
SERVER='127.0.0.1'
PORT=9092
whom=''
client=socket.socket()
client.connect((SERVER,PORT))
def se():
	whom=''
	while True:
		msg=input(f'{nickname}: ')
		bytesize=len(msg)
		lenofbyte=len(str(bytesize))
		client.send(str(lenofbyte).encode('utf-8'))
		client.send(str(bytesize).encode('utf-8'))
		client.send(msg.encode('utf-8'))
		bytesize=len(whom)
		lenofbyte=len(str(bytesize))
		client.send(str(lenofbyte).encode('utf-8'))
		client.send(str(bytesize).encode('utf-8'))
		client.send(whom.encode('utf-8'))
		if msg=='online':
			while True:
				person=client.recv(20).decode('utf-8')
				if person!='finish'
					print(person)
		elif msg=='done':
			whom=''
			print("whol=''")

def main():
	global nickname
	nickname=input("Give Your Self A NickName ")
	client.send(nickname.encode('utf-8'))
#	re=threading.thread(target=recv,args=())
	set=threading.Thread(target=se,args=())
#	re.start()
	set.start()
main()
