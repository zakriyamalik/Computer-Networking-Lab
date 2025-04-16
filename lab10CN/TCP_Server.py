import socket
import threading
import os


class userStruct:
    def __init__(self,u_name, u_cnic ):
        self.u_name=u_name
        self.u_cnic = u_cnic


def handleClient(thread_structs):
    file_path = "output.txt"
    thread_structs=thread_structs[0]
    print("Handle Client function\n",thread_structs)
    if os.path.exists("Voters_List.txt"):
      f = open("Voters_List.txt", "r")
      for x in f:
       if thread_structs.u_name in x:
          print("Valid Client")
          candidate=input("Enter candiate option from the list")
          if os.path.exists(file_path):
           k = open("Candidates_List.txt", "r")
           for x in k:
               print(x)
           if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                line=thread_structs.u_name+thread_structs.u_cnic+candidate
                file.write(line)

           else:
            file = open("output.txt", "a")
            line=thread_structs.u_name+thread_structs.u_cnic+candidate
            file.write(line)
            file.close()
          else:
              print("Candidates File not found")
    else:
       print("Voters File not found")

    

def main():
    host = '127.0.0.1'
    port = 2000
    buffer_size = 2000
    threads =[]
    thread_structs =[]
    
     

    # Create socket
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created")
    except socket.error as err:
        print(f"Could not create socket. Error: {err}")
        return

    # Bind socket to IP and port
    try:
        server_socket.bind((host, port))
        print("Bind done")
    except socket.error as err:
        print(f"Bind failed. Error: {err}")
        return

    
    # Listen for incoming connections
    try:
        server_socket.listen(5)
        print("Listening for incoming connections...")
    except socket.error as err:
        print(f"Listen failed. Error: {err}")
        return

    # Accept a client connection
    
    try:
        client_socket, client_address = server_socket.accept()

            
        print(f"Client connected with IP: {client_address[0]} and Port No: {client_address[1]}")
    except socket.error as err:
        print(f"Accept failed. Error: {err}")
        return

    # Receive message from client
    try:
        client_message = client_socket.recv(buffer_size).decode()
        client_message1=client_message
        client_message=client_message.split(' ')
        thread_structs.append(userStruct(client_message[0],client_message[1]))
        t = threading.Thread(target=handleClient,args=(thread_structs,))
        threads.append(t)
        t.start()

        # userStruct(client_message[0],client_message[1])
        print(client_message[0],client_message[1])
        print(f"Client Message: {client_message}")
    except socket.error as err:
        print(f"Receive failed. Error: {err}")
        client_socket.close()
        server_socket.close()
        return

    # Send message back to client
    try:
        client_socket.sendall(client_message1.encode())
    except socket.error as err:
        print(f"Send failed. Error: {err}")

# Close sockets
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()
