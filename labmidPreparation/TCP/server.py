# import socket

# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server_address=('localhost',10000)
# sock.bind(server_address)
# sock.listen(1)
# while True:
#     try:
#         connection,address=sock.accept()
#         while True:
#          data=connection.recv(16)
#          if data:
#            print("Data from client is ",data.decode())
#          else:
           
#             break  
#         data="asda dad adda dasda dadssada dawer rwrw rrdsfdg gdfhh weretadsg "
#         connection.sendall(data.encode())
#         connection.shutdown(socket.SHUT_WR)
#     except Exception as e:
#      print(e)

import socket;

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',1000)
sock.bind(server_address)
sock.listen(1)
try:
    while True:
        connection,address=sock.accept()
        while True:
           data=connection.recv(16)
           if data:
               print("data is "+data)
           else:
               break
        message=input("Enter your responce")
        connection.sendall(message)
        sock.shutdown(socket.SHUT_WR)
except Exception as e:
    print(e)
        


 