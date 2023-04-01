from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
# GLOBAL CONSTANTS
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZE = 512

# GLOBAL VARIABLES
messages = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def receive_messgaes():
    """
    receive messages from server
    :return: None
    """
    while True:
        try:
            msg = client_socket.recv(BUFSIZE).decode()
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEPTION]", e)
            break

def send_messages(msg):
    """
    send messages to server
    :return: None
    """
    if msg == "{quit}":
        client_socket.close()
    client_socket.send(bytes(msg, "utf8"))
    


receive_thread = Thread(target=receive_messgaes)
receive_thread.start()

send_messages("Tim")
time.sleep(5)
send_messages("hello")
time.sleep(5)
send_messages("{quit}")