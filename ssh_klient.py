# !/usr/bin/env python3

import paramiko, sys, subprocess
import argparse

from kal_sar import get_sysstat_day as get_sar


def ssh_konnector(hostname, password, username, port, command):
    """ssh connection object"""

    print("trying to setup connection")
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy('AutoAddPolicy')
        # client.connect(timeout=10)
        # client.connect(auth_timeout=5)
        # client.connect(allow_agent=True)
        # client.connect(gss_deleg_creds=True)
        client.load_host_keys('known_hosts')
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # assert isinstance(password, object)
        client.connect(hostname=hostname, port=port, username=username, password=password, timeout=10, auth_timeout=10, gss_deleg_creds=True, allow_agent=True)
        print("I wanna run: ", command)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))

    finally:
        client.close()

    print("Closing connection now.")

    return stdout


# ssh_konnector(command='uptime')
# ssh_konnector(hostname='kalibur-mce', command="sadf   -d   --  /var/log/sysstat/sa15     -s 12:00 -e 17:00   -q")

# def main():
#    pass # ssh_konnector()

if __name__ == '__main__':
    """Collects parameters to be used for creating ssh connection."""
    parser = argparse.ArgumentParser(description='Ssh client to run command on remote system.')
    parser.add_argument('hostname', help='hostname must dns resolvable or IP address.', default='localhost')
    parser.add_argument('-c', '--command', help="The command you wish to run on remote system.", default="hostname; uptime")
    parser.add_argument('-u', '--username', help="Specify a user with ssh access to target host.") #, default="rhel")
    parser.add_argument('-P', '--password', help="Enter a password for the user in use.") #, default="rhel")
    parser.add_argument('-p', '--port', help="Specify port number default is 22.", default=22)

    print("Here are my args parsed", parser.parse_args())
    arguments = parser.parse_args()

    hostname = arguments.hostname
    command = arguments.command  # get command from kal_sar.py
    username = arguments.username
    password = arguments.password
    port = arguments.port
    ssh_konnector(hostname, password, username, port, command)

