import socket
import sys

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print(f'starting up on {server_address[0]} port {server_address[1]}', file=sys.stderr)
    sock.bind(server_address)
    final_data=""

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection', file=sys.stderr)
        connection, client_address = sock.accept()
        try:
            print(f'connection from {client_address}', file=sys.stderr)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                final_data+=data.decode()
                print(f'received "{data.decode()}"', file=sys.stderr)
                if data:
                    # print('sending data back to the client', file=sys.stderr)
                    # connection.sendall(data)
                    print("")
                else:
                    # print("Hello I am Server: Id received is "+final_data[-1])
                    chunks=[]
                    chunks=final_data.split(" ")
                    final_data=""
                    for i in chunks:
                        if "a" in i:
                            
                            final_data+=i[::-1]
                            final_data+=" "
                            print(i)
                        elif "e" in i:
                             final_data+=i[::-1]
                             final_data+=" "
                             print(i)
                        elif "i" in i:
                                final_data+=i[::-1]
                                final_data+=" "
                                print(i)
                        elif "o" in i:
                                final_data+=i[::-1]
                                final_data+=" "
                                print(i)
                        elif "u" in i:
                                final_data+=i[::-1]
                                final_data+=" "
                                print(i)
                        else:
                             final_data+=i
                             final_data+=" "
                    
                   
                    print("Hello I am Server: Data computed is "+final_data)
                    connection.sendall(final_data.encode())
                    print(f'no more data from {client_address}', file=sys.stderr)
                    break
        except Exception as e:
            print(f'An error occurred: {e}', file=sys.stderr)
        finally:
            # Clean up the connection
            connection.close()
