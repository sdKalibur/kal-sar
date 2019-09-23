# !/usr/bin/env python3

import paramiko, sys, subprocess
import argparse

from kal_sar import get_sysstat_day as get_sar


def ssh_konnector(hostname, password, username, port, command):
    """ssh connection object"""
# https://www.programcreek.com/python/example/11460/paramiko.AuthenticationException
    print("trying to setup connection")
    try:
        # Define connection object
        client = paramiko.SSHClient()
        client.load_host_keys('known_hosts')
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Make connection
        client.connect(hostname=hostname, port=port, username=username, password=password, timeout=10, auth_timeout=10,
                       gss_deleg_creds=True, allow_agent=True, )
        # raise NoValidConnectionsError(errors)
        #   paramiko.ssh_exception.NoValidConnectionsError: [Errno None] Unable to connect to port 22 on 10.42.0.2

        # Excute command on successful connection
        print("I wanna run: ", command)
        stdin, stdout, stderr = client.exec_command(command)
        print("Stdout says : \n:", stdout.read().decode('utf-8'))
        print("stderr says : \n:", stderr.read().decode('utf-8'))

    finally:
        client.close()

    print("Closing connection now.")

    return stdout, stderr

if __name__ == '__main__':
    """Collects parameters to be used for creating ssh connection."""
    parser = argparse.ArgumentParser(description='Ssh client to run command on remote system.')
    parser.add_argument('hostname', help='hostname must dns resolvable or IP address.', default='localhost')
    parser.add_argument('-c', '--command', help="The command you wish to run on remote system.",
                        default="hostname; uptime")
    parser.add_argument('-u', '--username', help="Specify a user with ssh access to target host.")  # , default="rhel")
    parser.add_argument('-P', '--password', help="Enter a password for the user in use.")  # , default="rhel")
    parser.add_argument('-p', '--port', help="Specify port number default is 22.", default=22)

    print("Here are my args parsed", parser.parse_args())
    arguments = parser.parse_args()

    hostname = arguments.hostname
    command = arguments.command  # get command from kal_sar.py
    username = arguments.username
    password = arguments.password
    port = arguments.port
    ssh_konnector(hostname, password, username, port, command)
