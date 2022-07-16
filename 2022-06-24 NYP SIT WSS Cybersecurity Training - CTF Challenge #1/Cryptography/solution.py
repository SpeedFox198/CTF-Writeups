from Crypto.Cipher import AES

# A convinient XOR function I got from stackoverflow
# https://stackoverflow.com/questions/29408173/byte-operations-xor-in-python
def xor(a, b):
    return bytes(i ^ j for i, j in zip(a, b))

def decrypt(msg:str, iv:bytes):  
    temp = bytes.fromhex(msg)
    key = temp[:16]     # Key is 1st 16 bytes/characters
    ct = temp[16:]      # Ciphertext is the rest of the bytes
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(ct)

# Get the ciphertexts
ct1, ct2 = open("output.txt", "r").read().splitlines()

# Attempt to decrypt with a known IV
known_iv = b"0" * 16
failed_decrypt = decrypt(ct1, known_iv)

# Get decrypted ciphertext before XOR
decrypted_block = failed_decrypt[:16]
b4_xor = xor(known_iv, decrypted_block)

# XOR to get the correct IV
pt = b"If you put your mind to it you can accomplish anything."
the_iv = xor(pt, b4_xor)

print(decrypt(ct2, the_iv).decode())
