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
    reqt = 'GET / HTTP/1.1\r\nHost: www.it-college.ac.jp\r\n\r\n'
    reqb = reqt.encode('utf-8')
    send_msg(cs, reqb)
    reqb = b''.join(recv_msg(cs))
    reqt = reqb.decode('utf-8')
    print(reqt)
    cs.close()

if __name__ == '__main__':
    ip, port = input().split(':')
    main(ip, int(port))
