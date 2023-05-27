import socket

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

        # Read the message from the file
        with open(message, 'r') as f:
            message = f.read()

        # Add the recipient to the message
        message = "To: " + recipient + '\n' + message

        # Send the message to the proxy server
        s.sendall(message.encode())
        while True:
            resp = s.recv(1024).decode()
            if resp:
                break
        print('Proxy response:', resp)

if __name__ == '__main__':
    main()
