from netaddr import *
import threading

class Schedule(threading.Thread):
    def __init__(self, ip_range):
        super().__init__(self)
        self.raw_ip_range = ip_range

    def run(self):
        from_ip, to_ip = self.raw_ip_range.split()
        range = IPRange(from_ip, to_ip)