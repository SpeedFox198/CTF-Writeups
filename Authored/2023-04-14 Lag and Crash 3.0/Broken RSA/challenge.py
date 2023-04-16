from Crypto.Util.number import getPrime, bytes_to_long

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 1616

with open("flag.txt", "rb") as f:
    flag = f.read()

c = pow(bytes_to_long(flag), e, n)

with open("output.txt", "w") as f:
    f.write(f"{p=}\n")
    f.write(f"{q=}\n")
    f.write(f"{c=}\n")
    f.write(f"{e=}\n")
