import socket
import time
from colorama import Fore, init


init()

def scan(ip_table: list) -> None:
    for table in ip_table:
        print(f'{Fore.BLUE}[-]{Fore.RESET} {table}')
        with open('log_ip.txt', 'w') as f1:
            f1.write(table)

        for port in [80, 8000, 8080]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f'{Fore.BLUE}[-]{Fore.RESET} {port}')
            with open('log_ports.txt, w') as f2:
                f2.write(port)

            try:
                conn = s.connect((host, port))
                print(f'{Fore.GREEN}[*]{Fore.RESET}The resource is available {host} : {port}')
            except Exception:
                print(f'{Fore.RED}[!]{Fore.RESET} The resource is not available {host} : {port}')

            s.close()
