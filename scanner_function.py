from socket import *
import time 

def scan(ip_table):
    t_IP = gethostbyname(target)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect((t_IP, i))
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()
