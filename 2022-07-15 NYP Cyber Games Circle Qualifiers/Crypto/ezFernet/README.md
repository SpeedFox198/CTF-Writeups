# ezFernet

> Is fernet a new kind of fern?

## Files

- [challenge.txt](challenge.txt)

## Description

Challenge gives a single [text file](challenge.txt) containing a key and the encrypted flag.

## Solution

The title of the challenge is a huge hint. A simple search of "fernet" on the internet reveals that Fernet is a symmetric encryption algorithm. There is a python module that could be used for decrypting it.

So i wrote some python code to decrypt the text:
```py
from cryptography.fernet import Fernet

key = "VzVDZjlWT2RuWU1RT2N2WVFxcHlFQU1nQUVjMGVrNHM4NUpsZTZ5VFZDMD0="
ct = "Z0FBQUFBQml3V3lVRDI2WVlMdnF4Mm5FaTlrNXoxTnZZTGNZQjlXTGNoQkdHN3g2b3I5S01kWFllc2RsVmFNNEdqQVh5dUl6Q2p6V0hfRzFfQmVYQ3lRVVJRUGt1dXRTeG5iUXowV0J5OXZZUGRFb2FvWkdRcWFBUUVWTF90VTAxYUdJbTdEM1BKXy0="

pt = Fernet(key).decrypt(ct)

print(pt)
```

However, I was given an error:
```
ValueError: Fernet key must be 32 url-safe base64-encoded bytes.
```

What could be the issue then? Looking at the key and the ciphertext again, both of them seem to be base64 encoded. So I tried decoding them using base64 and voila, the ciphertext has been decrypted, and we have our flag.

Solution:
```py
from cryptography.fernet import Fernet
from base64 import b64decode

key = b64decode("VzVDZjlWT2RuWU1RT2N2WVFxcHlFQU1nQUVjMGVrNHM4NUpsZTZ5VFZDMD0=")
ct = b64decode("Z0FBQUFBQml3V3lVRDI2WVlMdnF4Mm5FaTlrNXoxTnZZTGNZQjlXTGNoQkdHN3g2b3I5S01kWFllc2RsVmFNNEdqQVh5dUl6Q2p6V0hfRzFfQmVYQ3lRVVJRUGt1dXRTeG5iUXowV0J5OXZZUGRFb2FvWkdRcWFBUUVWTF90VTAxYUdJbTdEM1BKXy0=")

pt = Fernet(key).decrypt(ct)

print(pt)
```

Output:
```
b'FLAG{f3rn3t_sYmMetRiC_eNcRyPt10n}'
```

Flag Captured: `FLAG{f3rn3t_sYmMetRiC_eNcRyPt10n}`
