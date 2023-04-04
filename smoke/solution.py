import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8000))
s.listen(10)

while True:
    conn, address = s.accept()
    with conn:
        buffer = b""
        data = conn.recv(1024)
        if not data:
            conn.sendall(buffer)
        buffer += data
