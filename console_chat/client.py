"""
The module responsible for the operation
of the client side of the console chat
"""

import socket
from threading import Thread
import sys
from server import server_info


def receive():
    """Receives a message from the server and processes it"""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'ENTER NICKNAME':
                client.send(nickname.encode('utf-8'))
            elif message.split()[0] == nickname:
                print('---message delivered---')
            else:
                print(message)
        except:
            print("--message not delivered--", '\n', "you are logged out of the server")
            client.close()
            break


def write():
    """Sends messages to the server"""
    while True:
        message = f'{nickname} : {input("")}'
        if message == f'{nickname} : /exit':
            client.close()
            print('closing...')
            sys.exit(0)
        client.send(message.encode('utf-8'))


if __name__ == '__main__':
    nickname = input("Choose a nickname: ")
    host, port = server_info()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    receive_thread = Thread(target=receive).start()
    write_thread = Thread(target=write).start()
