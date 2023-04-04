import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("0.0.0.0", 8000))
socket.listen(10)

while True:
    conn, _ = socket.accept()
    with conn:
        buffer = b""
        data = conn.recv(1024)
        if not data:
            conn.sendall(buffer)
        buffer += data
