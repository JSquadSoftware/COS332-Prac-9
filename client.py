import socket
import base64

def displayMenu():
    print('1. Send a message')
    print('2. Quit')
    choice = input('Enter your choice: ')
    message = ''
    if choice == '1':
        print('1. Semi-illegal message')
        print('2. Illegal message')
        print('3. Legal message')
        choice = input('Enter your choice: ')
        if choice == '1':
            message = './messages/semi-illegal.txt'
        elif choice == '2':
            message = './messages/illegal.txt'
        elif choice == '3':
            message = './messages/legal.txt'
        else:
            print('Invalid choice. Please try again')
            displayMenu()
    elif choice == '2':
        message = 'Quit'
    else:
        print('Invalid choice. Please try again')
        message = displayMenu()
    return message

def main():

    # Connect to PROXY server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 55555)
    s.connect(server_address)
    print('Connected to the server:', server_address)

    while True:

        # Get the message from the user
        message = displayMenu()

        # Quit if the user wants to quit
        if message == 'Quit':
            s.close()
            return

        # Get the recipient from the user
        recipient = input('Enter the recipient: ')

        print("Select a mimetype:")
        print("1. application/octet-stream (base64)")
        print("2. text/plain")
        mimetype = input("Enter your choice: ")
        mimetype = 'application/octet-stream' if mimetype == '1' else 'text/plain'

        # Read the message from the file
        with open(message, 'r') as f:
            message = f.read()

        if mimetype == 'application/octet-stream':
            message = base64.b64encode(message.encode('utf-8')).decode('utf-8')

        print("Encoded Message:", message)
        print("Encoded Message Type:", type(message))

        # Add the recipient to the message
        message = "To: " + recipient + '\n' + message
        message = "MIME-Version: 1.0\nContent-Type: " + mimetype + "\n" + message

        print("Final Message", message)

        # Send the message to the proxy server
        print("About to send message to proxy")
        s.sendall(message.encode())
        print("Message sent to proxy")
        while True:
            resp = s.recv(1024).decode()
            if resp:
                break
        print('Proxy response:', resp)

if __name__ == '__main__':
    main()
