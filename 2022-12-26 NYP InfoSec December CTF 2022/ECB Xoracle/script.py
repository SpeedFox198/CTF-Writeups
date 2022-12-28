import string
from pwn import b64d, remote


FLAG_LEN = 16
BLOCK_SIZE = 16

HOST = "34.126.175.135"
PORT = 8009

conn = remote(HOST, PORT)


def send(pt):
    conn.recv()  # Recieve prompt
    conn.sendline(pt)
    return conn.recvline().decode()


def one_attempt(incomplete):
    pt = "".join(char*16 for char in incomplete) + "A"  # Extra to ensure pt%16>0
    received = send(pt.encode())
    result = b64d(received.replace(">", "").strip())
    return result[:BLOCK_SIZE] == result[-(BLOCK_SIZE*2):-BLOCK_SIZE]


def solve():
    incomplete = list("NYP{")  # Flag should be of `NYP{...}` format
    for _ in range(FLAG_LEN-len(incomplete)-1):
        incomplete.append("")
        for char in string.printable:
            print(f"Attempting: {''.join(incomplete)}")
            incomplete[-1] = char
            yes = one_attempt(incomplete)
            send(b"next")  # Skip to encrypt again
            if yes: break
    return "".join(incomplete) + "}"


conn.recv()  # Recieve banner


flag = solve()
print(f"Flag retrieved: {flag}")
