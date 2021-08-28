import socket
from env import BOT, CHANNEL, OATH

HEADER = 64
PORT = 6667
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "irc.chat.twitch.tv"
ADDR = (SERVER, PORT)

BOT_USERNAME = BOT
CHANNEL_NAME = CHANNEL
OATH_TOKEN = OATH

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#automatically starts
def login():
    client.send((f"PASS " + OATH_TOKEN + "\n").encode(FORMAT))
    client.send((f"NICK " + BOT_USERNAME + "\n").encode(FORMAT))
    client.send((f"JOIN " + CHANNEL_NAME + "\n").encode(FORMAT))
    client.send(f'CAP REQ :twitch.tv/membership\n'.encode(FORMAT))
    print(client.recv(2048).decode(FORMAT))

#buffers the data being sent
def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        print(client.recv(2048).decode(FORMAT))


#buffer data recieved and is used for reading what is send
def recveive():
    recievingthechatmessage = (client.recv(2048).decode(FORMAT))
    msg_length = len(recievingthechatmessage)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    x = recievingthechatmessage
    return x.strip()
