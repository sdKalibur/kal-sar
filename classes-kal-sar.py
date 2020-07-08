#!/usr/bin/env python3
#
# from kal_sar.py import main as kal_sar
# from ssh_klient.py import main as ssh_klient

# client.connect(hostname, port=port, username=username, password=password)

class Host_state:
    """Gives an overview of a hosts health status"""
    def __init__(self):
        """constructor"""
        self.hostname = hostname
        self.address = address # fqdn or ip addess should do

    def __repr__(self):
        return self.address
        pass

    def __str__(self):
        self.adress

    def __ldavg__():
        data_set = kal_sar() # take address as argument
        labels = data_set[0]
        data = data_set[1]
    #
    #
    # ssh_klient(self.address, command='uptime')


print(Host_state.address())