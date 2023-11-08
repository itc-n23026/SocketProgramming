import socket

server_ip = socket.gethostbyname(socket.gethostname())
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_server.bind((server_ip, 52001))

tcp_server.listen(1)
print('Wait tcp accepting...')
client, address = tcp_server.accept()
print('Connected client ip : {}'.format(address))

rcv_data = client.recv(1024)
print('Data : {}'.format(rcv_data.decode("utf-8")))

client.send('Hi!'.encode("utf-8"))
client.close()
