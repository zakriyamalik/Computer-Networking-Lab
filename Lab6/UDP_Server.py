import socket
import time
import csv

def inputFunction(name):
    
 with open('attendence.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)

    spamwriter.writerow(name)

def allPresent():
    with open('attendence.csv','r') as file:
        reader=reader(file)
        for row in reader:
            print(row)
def checkifPresent(value):
     with open('attendence.csv','r') as file:
        reader=reader(file)
        for row in reader:
            if row==value:
             return True
        return False
     
def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the server address and port
    server_address = ('127.0.0.1', 2000)
    sock.bind(server_address)

    print("Socket created and bound")
    print("Listening for messages...\n")

    while True:
        try:
            # Receive the message from the client
            client_message, client_address = sock.recvfrom(2000)
            client_message=client_message.decode()
            print(f"Received message from IP: {client_address[0]} and Port No: {client_address[1]}")
            print(f"Client Message: {client_message}",flush=True)
            sock.sendto(client_message.encode(), client_address)

            time.sleep(0.1)

            print("This is the last character"+client_message[-1])
            last_char=client_message[-1]
           

            if last_char=="I":
                print("Input")
                if(checkifPresent(client_message)):
                 print("You are already Present")
                 allPresent()
                else:
                 print("Allready present")
                 allPresent()
                 print("Marking you present....")
                 
                 inputFunction(client_message)
                 print("Attendence is Marked")
                 allPresent()
            else:
                print("Out")

            # personal_message=input("How would you like to repond to that ?")


            # Send the message back to the client
            # sock.sendto(personal_message.encode(),client_address)
            # sock.sendto(client_message, client_address)

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    # Closing the socket
    sock.close()

if __name__ == "__main__":
    main()