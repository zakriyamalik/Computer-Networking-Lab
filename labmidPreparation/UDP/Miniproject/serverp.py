import socket
 
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 2000)
    sock.bind(server_address)
    
    while True:
        try:
            message, address = sock.recvfrom(2000)
            message = message.decode().lower()
            print("Received message:", message)
            
            if message == "request":
                print("In if")
                response = "Enter your list:"
                sock.sendto(response.encode(), address)
                
                message, address = sock.recvfrom(2000)
                message = message.decode()
                items = message.split()  # 🔹 Convert string to list
                
                print("List of items received:", items)
                for item in items:
                    print(item)

        except Exception as e:
            print("Error:", e)

main()
