from cryptography.fernet import Fernet
from base64 import b64decode

# Key and encrypted flag
key = b64decode("VzVDZjlWT2RuWU1RT2N2WVFxcHlFQU1nQUVjMGVrNHM4NUpsZTZ5VFZDMD0=")
ct = b64decode("Z0FBQUFBQml3V3lVRDI2WVlMdnF4Mm5FaTlrNXoxTnZZTGNZQjlXTGNoQkdHN3g2b3I5S01kWFllc2RsVmFNNEdqQVh5dUl6Q2p6V0hfRzFfQmVYQ3lRVVJRUGt1dXRTeG5iUXowV0J5OXZZUGRFb2FvWkdRcWFBUUVWTF90VTAxYUdJbTdEM1BKXy0=")

# Decrypt flag
pt = Fernet(key).decrypt(ct)

# Display decrypted flag
print(pt)
