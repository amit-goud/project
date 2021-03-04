import socket
s= socket.socket()
host= input(str("Please enter the host address of the sender :"))
port=8080
s.connect((host,port))
print("Successfully COnnected")
filename=input(str("Enter filename :"))
file =open(filename,'wb')
filedata= s.recv(1024)
file.write(filedata)
file.close()
print("file has been recieved")