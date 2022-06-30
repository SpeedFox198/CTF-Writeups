from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import os

flag = open("flag.txt", "rb").read()
key = os.urandom(16)

def encrypt(msg):
    iv = os.urandom(16)
    cipher = AES.new(iv, AES.MODE_CBC, key)
    return (iv + cipher.encrypt(pad(msg, 16))).hex()

print(encrypt(b"If you put your mind to it you can accomplish anything."))
print(encrypt(flag))