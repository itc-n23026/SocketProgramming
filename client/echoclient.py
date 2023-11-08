import socket

def send_msg(sock, msg):
    totalsl = 0
    totalml = len(msg)
    while totalsl < totalml:
        sl = sock.send(msg[totalsl:])
        if sl == 0:
            raise RuntimeError('socket connection broken')
        totalsl += sl

def recv_msg(sock, cl=1024):
    while True:
        rc = sock.recv(cl)
        if len(rc) == 0:
            break
        yield rc

def main(ip, port):

    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((ip, port))
    message = "Hello, World!"
    message_bytes = message.encode('ASCII')
    send_msg(cs, message_bytes)
    for received_data in recv_msg(cs):
        print(received_data.decode('ASCII'), end='')
    cs.close()

if __name__ == '__main__':
    ip, port = input().split(':')
    main(ip, int(port))
