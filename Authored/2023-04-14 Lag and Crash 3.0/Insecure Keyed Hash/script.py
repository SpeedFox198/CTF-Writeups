from string import ascii_lowercase
from hashlib import md5
import pwn

SERVER = "nc.lagncra.sh"
PORT = 8012
PASSPHRASE = b"Better than HMAC!"

def get_key(x: str, p: bytes, k=b"", depth=5):
    if depth:
        for i in ascii_lowercase:
            result = get_key(x, p, k+i.encode(), depth=depth-1)
            if result:
                break
        return result
    elif md5(k+p).hexdigest() == x:
        return k

p = b"Hello"  # Known plaintext

cns = pwn.connect(SERVER, PORT)
cns.recvuntil(b"Enter option: ")
cns.sendline(b"1")
cns.recvuntil(b"Enter message: ")
cns.sendline(p)
cns.recvuntil(b"Here's your signed message: ")
x = cns.recvline()[:-2].split(b".")[-1]
key = get_key(x.decode(), p)
print(key)
cns.recvuntil(b"Enter option: ")
cns.sendline(b"2")
cns.recvuntil(b"Enter signed message: ")
cns.sendline(PASSPHRASE + b"." + md5(key+PASSPHRASE).hexdigest().encode())
cns.recvuntil(b"Message verified!\r\n")
flag = cns.recvuntil(b"}").decode()
cns.close()
print(f"Flag captured: {flag}")
