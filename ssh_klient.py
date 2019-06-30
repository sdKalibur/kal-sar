#!/usr/bin/env python3g

import paramiko
import sys, subprocess
import argparse

from kal_sar import get_sysstat_day as get_sar



parser = argparse.ArgumentParser(description='Ssh into a server')
parser.add_argument('hostname', help='hostname must dns resolvable or IP address.', default='localhost', type=str )
parser.add_argument('-m', '--mode', help="enter performance matrix", default='cpu_load')
parser.add_argument('-u', '--username', help="Specify a user with ssh access to target host.", default="rhel")
parser.add_argument('-p', '--password', help="Enter a password for the user in use.", default="rhel")
parser.add_argument('-P', '--port', help="Set the ssh port for this connection.", default=22, type=int)

print("trying to setup connection: \n" + str(parser.parse_args()))
def ssh_konnector():
    """ssh client connector"""
    command == 'top'

    # command == mode

    client.connect(hostname, timeout='20')
    try:
        client = paramiko.SSHClient()
        client.load_host_keys('known_hosts')
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #assert isinstance(password, object)
        client.connect(hostname, timeout=20)
        print("I wanna run: ", command)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read())
        print(stderr.read())
        # msg = subprocess.getoutput(client.connect(hostname, port=port, username=username, password=password))
        # print('My output: ', msg)


    finally:
        client.close()

    print("Closing connection now.")

    return stdout

# ssh_konnector(command='uptime')
# ssh_konnector(hostname='kalibur-mce', command="sadf   -d   --  /var/log/sysstat/sa15     -s 12:00 -e 17:00   -q")
#
# def main():
#     ssh_konnector()
#
#
# if __name__ == '__main__':
#      main()