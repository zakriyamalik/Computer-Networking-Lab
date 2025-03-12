import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address) 
try:

  message = 'the birds fly in dry sky at night'
  print('sending %s' % message)
  sock.sendall(message.encode())
  final_data=""
  sock.shutdown(socket.SHUT_WR)
  amount_received = 0
  amount_expected = len(message)
  while True:
    data = sock.recv(16)
    if not data:
        break
    final_data += data.decode()
  print("Total data received in client is "+final_data)
  chunks=[]
  chunks=final_data.split(" ")
  final_data=""
  for i in chunks:
    if "a" in i:
        
        final_data+=i
        final_data+=" "
        print(i)
    elif "e" in i:
            final_data+=i
            final_data+=" "
            print(i)
    elif "i" in i:
            final_data+=i
            final_data+=" "
            print(i)
    elif "o" in i:
            final_data+=i
            final_data+=" "
            print(i)
    elif "u" in i:
            final_data+=i
            final_data+=" "
            print(i)
    else:
            final_data+=i[::-1]
            final_data+=" "


  print("Hello I am Client: Data computed is "+final_data)
finally:
   print('closing socket')
   sock.close()