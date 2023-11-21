import socket


def run(socket, size=1024):
    with socket as s:
        while True:
            if not (data := s.recv(size)):
                break
            print(data.decode('utf-8'), end='')
            s.sendall(data)


def main(host, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        print('Connected by', addr)
        run(conn)


if __name__ == '__main__':
    host, port = input().split(':')
    main(host, int(port))
