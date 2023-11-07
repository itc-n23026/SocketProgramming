import socket
import struct

def send_msg(sock, msg):
    totalsl = 0
    totalml = len(msg)
    while totalsl < totalml:
        sl = sock.send(msg[totalsl:])
        if sl == 0:
            raise RuntimeError('socket connection broken')
        totalsl += sl

def recv_msg(sock, totalms):
    totalrs = 0
    while totalrs < totalms:
        rc = sock.recv(totalms - totalrs)
        if len(rc) == 0:
            raise RuntimeError('socket connection broken')
        yield rc
        totalrs += len(rc)

def main():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)
    ss.bind(('127.0.0.1', 54321))
    ss.listen()
    print('starting server ...')
    cs, (ca, cp) = ss.accept()
    print(f'accepted from {ca}:{cp}')
    rm = b''.join(recv_msg(cs, totalms=8))
    print(f'received: {rm}')
    (operand1, operand2) = struct.unpack('!ii', rm)
    print(f'operand1: {operand1}, operand2: {operand2}')
    result = operand1 + operand2
    print(f'result: {result}')
    rsm = struct.pack('!q', result)
    send_msg(cs, rsm)
    print(f'sent: {rsm}')
    cs.close()
    ss.close()

if __name__ == '__main__':
    main()
