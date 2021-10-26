from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from os import listdir
from os.path import join


CONF_FILENAME = "conf_server.txt"


def debug(x: str):
    print(str(datetime.now()).split()[1].split(".")[0], x)


def get_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


if __name__ == "__main__":

    debug(f"Reading configuration file ({CONF_FILENAME})...")
    with open(CONF_FILENAME) as conf_file:
        port, files_dir = conf_file.read().split(":")
        port = int(port)

    debug("Creating socket object...")
    s = socket(AF_INET, SOCK_STREAM)

    lan_ip = get_ip()
    debug(f"Binding socket to {lan_ip}:{port}...")
    s.bind((lan_ip, port))

    debug("Beginning main server loop...")
    while True:

        try:
            debug("Awaiting client connection...")
            s.listen(1)
            conn, addr = s.accept()
        except KeyboardInterrupt:
            debug("Breaking main server loop...")
            break

        debug("Receiving filenames...")
        filenames_serialized = ""
        data = " "
        while data[-1] != "+":
            data = conn.recv(1024).decode()
            filenames_serialized += data
        received_filenames = filenames_serialized[:-1].split("|")

        debug("Eliminating existing videos...")
        required_filenames = [filename for filename in received_filenames if filename not in listdir(files_dir)]

        debug("Sending required filenames to client...")
        for filename in required_filenames:
            conn.send(filename.encode() + b"|")
        conn.send(b"+")

        debug("Receiving files from client...")
        for _ in range(required_filenames):
            data = b""
            while data.count(b"|") < 2:
                data += conn.recv(1024)
            data_len, filename, data = data.split(b"|", 2)
            while len(data) < data_len:
                data += conn.recv(1024)
            with open(join(files_dir, filename), "wb") as file:
                file.write(data)

    debug("Closing socket object...")
    s.close()
