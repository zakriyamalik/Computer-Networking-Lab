import socket
import time
import csv
import os


def setup():
   if not os.path.exists('attendence.csv'):
      with open('attendence.csv','w')as file:
         writer=csv.writer(file)
         writer.writerow(["RollNumbers"])
         print("File created")

   

def inputFunction(name):
 name = "".join(name.strip())
 name=name[:-3]
#  print("The name that is input is \t"+name)
 with open('attendence.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)

    spamwriter.writerow([name])


def removeFunction(name):
 temp=[]
 name = "".join(name.strip())
 name=name[:-3]
#  print("The name that is to be removed is \t"+name)
 with open('attendence.csv', 'r', newline='') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
       if name not in row:
          temp.append(row)
 print("Have a nice day "+name)
 with open('attendence.csv','w',newline='')as file:
         writer=csv.writer(file)
         for row in temp:
           writer.writerow(row)
 allPresent()



def allPresent():
    with open('attendence.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)
def checkifPresent(value):
    # print("In check present")
    if not os.path.exists('attendence.csv'):
      return False
    else:
      with open('attendence.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            # print(value,"\tfdgfdgfdg",row)
            if value in row:
                
                return True
    return False
     
def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the server address and port
    server_address = ('127.0.0.1', 2000)
    sock.bind(server_address)
    setup()
    print("Socket created and bound")
    print("Listening for messages...\n")

    while True:
        try:
            # Receive the message from the client
            client_message, client_address = sock.recvfrom(2000)
            client_message=client_message.decode()
            client_message = client_message.strip()

            print(f"Received message from IP: {client_address[0]} and Port No: {client_address[1]}")
            # print(f"Client Message: {client_message}",flush=True)
            sock.sendto(client_message.encode(), client_address)

            time.sleep(0.1)

            # print("This is the last character"+client_message[-1])
            last_char=client_message[-1]
           

            if last_char=="I":
                # print("Input")
                if(checkifPresent("".join(client_message)) ):
                 print("You are already Present")
                 allPresent()
                else:
                #  print("Present students list")
                 allPresent()
                #  print("Marking you present....")
                 
                 inputFunction("".join(client_message))
                #  print("Attendence is Marked")
                 print("WellCome student "+client_message[:-3])
                 allPresent()
            else:
                # print("Out")
                removeFunction("".join(client_message))

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