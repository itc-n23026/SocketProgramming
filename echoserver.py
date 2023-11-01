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

    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)
    ss.bind((ip, port))
    ss.listen()
    print('starting server ...')
    cs, (ca, cp) = ss.accept()
    print(f'accepted from {ca}:{cp}')
    for rm in recv_msg(cs):
        send_msg(cs, rm)
        print(f'echo: {rm}')
    cs.close()
    ss.close()

if __name__ == '__main__':
    ip, port = input().split(':')
    main(ip, int(port))
