from base64 import b64decode, b64encode
from nclib import Netcat
from enum import Enum
from typing import Any

EOF_MARKER = "#"
HOST = "chal00bq3ouweqtzva9xcobep6spl5m75fucey.ctf.sg"
PORT = 18261
BOSS_HPS = (5, 30, 100)


def encode(data: str) -> bytes:
    return b64encode(data.encode()) + EOF_MARKER.encode()

def decode(data: bytes) -> str:
    return b64decode(data).decode()


class Command(Enum):
    ATTACK = "ATTACK"
    BATTLE = "BATTLE"
    VIEW_STATS = "VIEW_STATS"
    HEAL = "HEAL"
    BOSS_ATTACK = "BOSS_ATTACK"
    RUN = "RUN"
    VALIDATE = "VALIDATE"
    BUY_SWORD = "BUY_SWORD"
    BUY_POTION = "BUY_POTION"
    BACK = "BACK"
    WORK = "WORK"
    EXIT = "EXIT"

class NetClient:
    def __init__(self, host: str, port: int, verbose: bool = False):
        self.__client = Netcat((host, port), verbose=verbose)

    def send(self, command):
        return self._send_raw(command.value)

    def _send_raw(self, data: str) -> int:
        return self.__client.send(encode(data))

    def recv(
        self,
        marker: str = EOF_MARKER,
        max_size: Any | None = None,
        timeout: str = "default",
    ) -> str:
        return decode(
            self.__client.recv_until(marker, max_size, timeout)[
                : -len(EOF_MARKER)
            ]
        )

    def close(self):
        self.__client.close()


# Connection to server
con = NetClient(HOST, PORT)

# Defeat the 3 bosses
for i in BOSS_HPS:
    con.send(Command.BATTLE)  # Start battle
    con.recv()    # Receive boss info

    # Attack "i" number of times
    # Add VALIDATE command to bypass BOSS_ATTACK command
    data = " ".join([Command.ATTACK.value]*i + [Command.VALIDATE.value])
    con._send_raw(data)  # Send attack payload
    con.recv()    # Receive VALIDATE_OK/FLAG_OBTAINED

flag = con.recv()  # Get flag!

con.close()

# Success message (and flag!)
print(f"You have slain the dragon!\nFlag captured:\n{flag}")
