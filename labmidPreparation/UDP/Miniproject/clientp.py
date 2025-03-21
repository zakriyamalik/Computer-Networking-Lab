import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 2000)
    
    try:
        message = input("Enter your message: ")
        sock.sendto(message.encode(), server_address)
        
        data, _ = sock.recvfrom(2000)  # ✅ Corrected buffer size
        print("In client, the message from server:", data.decode())  # ✅ Decoding received data
        
        items = input("Enter list of books: ").split()  # ✅ Corrected input handling
        items_string = " ".join(items)  # ✅ Convert list to space-separated string
        
        sock.sendto(items_string.encode(), server_address)  # ✅ Corrected encoding
        
    except Exception as e:
        print("Error:", e)

main()
