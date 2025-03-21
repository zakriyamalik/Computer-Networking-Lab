# import socket
# def main():
#  print("In main function")
#  sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  server_address=("127.0.0.1",2000)
#  sock.bind(server_address)
#  print("Socket created and bound")
#  print("Listening for messages ......")
#  while True:
#   try:
#    client_message,client_address=sock.recvfrom(2000)
#    print("Message from client is ",client_message.decode())
#    sock.sendto(client_message,client_address)
  
#   except Exception as e:
#    print(e)
 


# main()



# import socket

# def main():
#    sock=socket.socket(socket.AF_INET,socket.NI_DGRAM)
#    server_address=("127.0.0.1",2000)
#    sock.bind(server_address)
#    while True:
#       try:
#        data,address=sock.recvfrom(2000)
#        print(data)
#        sock.sendto(data,address)
#       except Exception as e:
#        print(e)
   


import socket

def main():
    sock=socket.socket(socket.AF_INET,socket.NI_DGRAM)
    server_address=("127.0.0.1",2000)
    sock.bind(server_address)
    while True:
        try:
            data,address=sock.recvfrom(2000)
            print(data)
            sock.sendto(data,address)
        except Exception as e:
            print(e)
