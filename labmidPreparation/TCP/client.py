# import socket

# def main():
#     sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     server_address=('localhost',10000)
#     sock.connect(server_address)
#     try:
#         message=input("Enter your message")
#         sock.sendto(message.encode(),server_address)
#         sock.shutdown(socket.SHUT_WR)
#         while True:
#             data=sock.recv(16)
#             if data:
#                 print(data.decode())
#             else:
#                 print("Finished.......")
#                 break
#     except Exception as e:
#         print(e)



# main()


import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("localhost",1000)
sock.connect(server_address)

try:
    message=input("Enter your message")
    sock.sendall(message.encode(),server_address)
    sock.shutdown(socket.SHUT_WR)
    while True:
        data=sock.recv(16)
        if data:
            print(data)
        else:
            break
    


except Exception as e:
    print(e)