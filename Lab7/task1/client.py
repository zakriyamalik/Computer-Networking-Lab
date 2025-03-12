import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address) 
try:

  message = 'Hello I am client. My Id is '
  id=input("Enter your id")
  message=message+id
  print('sending %s' % message)
  sock.sendall(message.encode())
  amount_received = 0
  amount_expected = len(message)
#   while amount_received < amount_expected:
#    data = sock.recv(16)
#    amount_received += len(data)
#    print('received %s' % data)
finally:
   print('closing socket')
   sock.close()