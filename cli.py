import dataclasses
import socket

from lib import decrypt, encrypt

key = "таємнийключ"


@dataclasses.dataclass
class Message:
    id: int
    user: str
    text: str


def get_message(recv: str) -> Message:
    id, user, text = recv.split(".:")
    print(id, user, text)
    return Message(int(id), user.strip(), decrypt(text.strip(), key))


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    inp = ""
    while inp != "вихід":
        inp = input("Введіть повідомлення або 'вихід': ")
        s.sendall(encrypt(inp, key).encode())
        data = s.recv(2048)
        text = data.decode().split("\n")
        print("\n".join([get_message(msg).text for msg in text if msg]))

    s.close()


main()
