# Mathematics of Cryptography

### Files

- [chall.py](chall.py)
- [output.txt](output.txt)


## Challenge Description

The Defenders heard that there are some Math legends among us and have reached out for assistance in breaking one of the Uprisers' security defenses.


## Let's see what we've got

The challenge contains a regular RSA encryption.

Btw what's with the `a = getRandomInteger(128)` trying to bait people? xD

We are given a few values:  
```
p-q
p^3 - q^3
n
ct
```

The flag is the encrypted message `m`:  
```
ct = m^e % n
```

To decrypt the ciphertext `ct`, we will need the private exponent `d` which is derived from `phi`:  
```
phi = (p-1)(q-1)
d = e^-1 % phi
m = ct^d % n
```

So we need to get the value `phi`, next is just some secondary school maths :)  
```
n = pq                  (We know this cause RSA)

phi = (p-1)(q-1)
phi = pq - p - q + 1
phi = n - p - q + 1     (Sub n = pq)
p+q = n + 1 - phi       (Equation 1)


p^2 + q^2 = (p+q)^2 - 2n                (Equation 2)

p^3 − q^3 = (p − q)(n + p^2 + q^2)
p^3 − q^3 = (p − q)((p+q)^2 - n)        (Sub equation 2)

(p+q)^2 - n = (p^3−q^3)/(p-q)
(p+q)^2 = (p^3−q^3)/(p-q) + n

p+q = sqrt( (p^3−q^3)/(p-q) + n )
n + 1 - phi = sqrt( (p^3−q^3)/(p-q) + n )

phi = n + 1 - sqrt( (p^3−q^3)/(p-q) + n )       (Sub equation 1)
```

## Maths using Python

Script to calculate `phi`, `d` and decrypt `ct`:  
```python
from Crypto.Util.number import long_to_bytes
import math

p_q = -1305235648860840853683949458831305072763230973669829177960178482866452800364412721111763583069321978987148627466498224410781024187725838888479326409184744
p3_q3 = -465514652595610856880453636545438331400010973790168791066069161352239209188533132121982942661849199245018660968880021999471046367873763759524854675286821508038418401864765726491449185192253500864628518550804809046508686959255535195714941766727484090297166583454871187745735758463441767587210583432967693381451227261083381147367649535205516682361917227931630894904749876510765825586785760034509104564737258991404912289408762611694496702482996518688138500642819128
n = 118316055600083929089071669812439032539191357668051889677911602916721340636167359556934591671598570703259986990715914276095866429868571322432308962619799310816435693053230854913872753733501348441234715512020861405241513403795045428404496593692411330352525309662619935495570018411169134102570106958094779439217
ct = 64880869410692063175906103028969957878271889970688259195068268235741104167117130794136851712307899764163566653527660540303926093374874865621497088649195483963877573321808998916766978276663044270028514646216644963284229260389738926787740160186040707610308628316701038087132926246223087221028661729121666185863
e = 65537

# phi = n + 1 - sqrt( (p^3−q^3)/(p-q) + n )
phi = n + 1 - math.isqrt(p3_q3//p_q + n)
d = pow(e, -1, phi)
m = pow(ct, d, n)

flag = long_to_bytes(m).decode()

print(f"Flag decrypted: {flag}")
```

Output:  
![screenshot1](assets/screenshot1.jpg)

Flag Captured: `NYP{y0uR3_getT1n_GUD_At_cRypt0_bRRR}`
