#https://python.plainenglish.io/chat-app-using-udp-5b486241748c
import socket
import os
import time

os.system("clear")

os.system("tput setaf 3")

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
     
ip=input("Enter tu IP: ")
port=int(input("Enter tu numero de puerto: "))
sendip=input("Enter del servidor IP: ")
sendport=int(input("Enter el puerto del servidor: "))
s.bind((ip,port))
while True:
  i=input("Enter your message:")
  s.sendto(i.encode(), (sendip,sendport))
  x=s.recvfrom(20)
  clientip=x[1][0]
  data=x[0].decode()
  print(clientip + " : " + data)