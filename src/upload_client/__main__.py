from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from os import listdir
from os.path import join


CONF_FILENAME = "conf_client.txt"


def debug(x: str):
    print(str(datetime.now()).split()[1].split(".")[0], x)


def get_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


if __name__ == "__main__":

    debug(f"Reading configuration file ({CONF_FILENAME})...")
    with open(CONF_FILENAME) as conf_file:
        port, files_dir, *addr = conf_file.read().split(":")
        port = int(port)
        addr[1] = int(addr[1])
        addr = tuple(addr)

    debug("Creating socket object...")
    s = socket(AF_INET, SOCK_STREAM)

    lan_ip = get_ip()
    debug(f"Binding socket to {lan_ip}:{port}...")
    s.bind((lan_ip, port))

    debug(f"Connecting to server at {addr[0]}:{addr[1]}...")
    s.connect(tuple(addr))

    debug("Sending filenames to server...")
    for filename in listdir(files_dir):
        s.send(filename.encode() + b"|")
    s.send(b"+")

    debug("Receiving required filenames from server...")
    filenames_serialized = ""
    data = " "
    while data[-1] != "+":
        data = s.recv(1024).decode()
        filenames_serialized += data
    received_filenames = filenames_serialized[:-1].split("|")

    debug("Sending files to server...")
    for filename in received_filenames:
        with open(join(files_dir, filename), "rb") as file:
            data = file.read()
        s.send(str(len(data)).encode() + b"|" + filename.encode() + b"|" + data)

    debug("Closing socket object...")
    s.close()
