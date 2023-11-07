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
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect(('127.0.0.1', 54321))
    operand1 = int(input("Enter operand1: "))
    operand2 = int(input("Enter operand2: "))
    print(f'operand1: {operand1}, operand2: {operand2}')
    rqm = struct.pack('!ii', operand1, operand2)
    send_msg(cs, rqm)
    print(f'sent: {rqm}')
    rm = b''.join(recv_msg(cs, 8))
    print(f'received: {rm}')
    (adv, ) = struct.unpack('!q', rm)
    print(f'result: {adv}')
    cs.close()

if __name__ == '__main__':
    main()
