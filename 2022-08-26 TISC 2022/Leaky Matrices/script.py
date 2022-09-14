from nclib import Netcat
import numpy as np

HOST = "chal00bq3ouweqtzva9xcobep6spl5m75fucey.ctf.sg"
PORT = 56765


def recv():
    line = con.recv().decode()
    print(line)
    return line

def send(line:str):
    con.sendline(line)
    print(f">>> {line}")


# Connection to server
con = Netcat(HOST, PORT)

recv()  # Receive banner

secret = []  # Secret matrix

# Leak secret
for i in range(8):
    recv()  # Receive prompt
    send("0"*i + "1" + "0"*(7-i))
    line = recv()  # Receive response
    line = line.split(">")[-1].strip()
    secret.append(list(map(int, line)))

# Create secret matrix
secret = np.matrix(secret).transpose()

# Respond to server challenges
for i in range(8):

    # The 1st prompt looks different from the subsequent prompts
    if not i:
        challenge = recv().split(">")[-1].split()[0]
    else:
        challenge = recv().split(">")[-1].strip()
        recv()

    challenge = np.fromiter(challenge, dtype="int").reshape(8, 1)

    response = (secret @ challenge) & 1
    response = response.reshape(-1).tolist()[0]
    response = "".join(map(str, response))

    send(response)  # Send response

recv()  # Receive passed msg
recv()  # Get flag

con.close()
