import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode())
        except:
            break

def main(host, port):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    host, port = input("IPアドレスとポート番号を入力してください:").split(':')
    main(host, int(port))

