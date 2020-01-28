import socket
import time

def scan(ip_table):
    for table in ip_table:
        pass

        for i in range(50, 500):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            conn = s.connect((t_IP, i))
            if (conn == 0):
                print('Port %d: OPEN' % (i,))
            s.close()
