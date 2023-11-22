import socket
import threading

clients = []
lock = threading.Lock()

def broadcast(message, sender_socket):
    with lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    remove(client)

def remove(client):
    with lock:
        if client in clients:
            clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                remove(client_socket)
                break
            else:
                broadcast(message, client_socket)
        except:
            remove(client_socket)
            break

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"チャットサーバーが {host}:{port} で起動しました...")

    while True:
        client_socket, addr = server_socket.accept()
        with lock:
            clients.append(client_socket)

        print(f"新しい接続: {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()

