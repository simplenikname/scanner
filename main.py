from netaddr import *
import threading
import scanner_function

class Schedule(threading.Thread):
    def __init__(self, ip_range):
        super().__init__(self)
        self.raw_ip_range = ip_range

    def run(self):
        from_ip, to_ip = self.raw_ip_range.split()
        ip_range = IPRange(from_ip, to_ip)
        scanner_function.scan(list(ip_range))
