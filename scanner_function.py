import socket
import time

def scan(ip_table: list) -> None:
    for table in ip_table:
        pass

        for port in [80, 8000, 8080]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            conn = s.connect((host, port))
            if (conn == 0):
                print('Port %d: OPEN' % (i,))
            s.close()
