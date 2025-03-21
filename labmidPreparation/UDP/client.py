# import socket
# def main():
#     sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     server_address=('127.0.0.1',2000)
#     try:
#         user_input=input("Enter your message ")
#         sock.sendto(user_input.encode(),server_address)
#         receivedmessage,receivedaddress=sock.recvfrom(2000)
#         print("received data is ",receivedmessage.decode())
#     except Exception as e:
#         print(e)


# main()


# import socket;

# def main():
#     sock=socket.socket(socket.AF_INET,socket.NI_DGRAM)
#     server_address=("127.0.0.1",2000)
#     try:
#         message=input("Enter your message ")
#         sock.sendto(message.encode(),server_address)
#     except Exception as e:
#         print(e)

import socket

def main():
    sock=socket.socket(socket.AF_INET,socket.NI_DGRAM)
    server_address=("127.0.0.1",2000)
    try:
        mess=input("Enter your message")
        sock.sendto(mess.encode(),server_address)
        sock.recvfrom(2000)

    except Exception as e:
        print(e)