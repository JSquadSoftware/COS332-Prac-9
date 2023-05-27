import socket
from newspeak import newspeak
import time

def send_message(message, recipient):
    print("Sending message to recipient")
    s = socket.socket()
    s.connect(('DESKTOP-HLJS7S1.localdomain', 25))
    print(s.recv(512).decode('UTF-8'))
    s.send(b'HELO DESKTOP-HLJS7S1.localdomain\r\n')
    print(s.recv(512).decode('UTF-8'))
    s.send(b'MAIL FROM:' + recipient.encode('UTF-8') + b'\r\n')
    print(s.recv(512).decode('UTF-8'))
    s.send(b'RCPT TO:' + recipient.encode('UTF-8') + b'\r\n')
    print(s.recv(512).decode('UTF-8'))
    s.send(b'DATA\r\n')
    print(s.recv(512).decode('UTF-8'))
    s.send(b'Subject: Newspeak production\r\n')
    content = message.encode('UTF-8')
    s.send(content + b'\r\n.\r\n')
    print(s.recv(512).decode('UTF-8'))
    s.send(b'QUIT\r\n')
    s.close()

def get_mime_type(message):
    content_type = None

    # Split the message into lines
    lines = message.split('\n')

    # Search for the Content-Type header
    for line in lines:
        if line.startswith('Content-Type:'):
            # Extract the content type value
            content_type = line.split(':', 1)[1].strip()
            break

    print("Content Type:", content_type)
    print("Content Type Type:", type(content_type))
    return content_type.strip()



def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 55555))
    server_socket.listen(1)
    print('SMTP Proxy Server listening on port 55555')

    client_socket = None
    while client_socket is None:
        client_socket, client_address = server_socket.accept()
    print('Received connection from:', client_address)

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            continue
        print("Received data:", data)
        mimetype = get_mime_type(data)
        print("Got mimetype: ", mimetype)
        print('Received message from client:', data)
        recipient, data = newspeak(data, mimetype)

        ## TEST Remove
        print("Data: ", data)
        if not data:
            resp = 'Your message was rejected by Newspeak!'
            client_socket.sendall(resp.encode())
            continue
        send_message(data, recipient)
        print("Email sent to recipient")
        resp = 'NewSpeak proxy sent: ' + data
        client_socket.sendall(resp.encode())
    
    client_socket.close()

if __name__ == '__main__':
    main()


