import socket

HOST = ''
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connection initiated {}', addr)

while True:
    data = conn.recv(2014)
    if not data:
        break
    conn.sendall(data.upper())
conn.close()
