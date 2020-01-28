import socket
import time
from colorama import Fore, init
from pprint import pprint


init()

def logger(data, file_name = None):
    if file_name:
        with open('log.txt', 'a') as file:
            file.write(data)
    else:
        pprint(data)

def scan(ip_table: list) -> None:
    for table in ip_table:
        print(f'{Fore.BLUE}[~]{Fore.RESET} {table}')

        for port in [80, 8000, 8080]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f'{Fore.BLUE}[~]{Fore.RESET} {port}')

            try:
                conn = s.connect((host, port))
                print(f'{Fore.GREEN}[*]{Fore.RESET}The resource is available {host} : {port}')
            except Exception:
                print(f'{Fore.RED}[!]{Fore.RESET} The resource is not available {host} : {port}')



            s.close()
