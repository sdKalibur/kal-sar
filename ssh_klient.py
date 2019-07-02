
#!/usr/bin/env python3

import paramiko,sys, subprocess
import argparse

from kal_sar import get_sysstat_day as get_sar



def ssh_konnector( hostname, password, username, port, command):
    """ssh connector function"""

    print("trying to setup connection")
    try:
        client = paramiko.SSHClient()
        client.load_host_keys('known_hosts')
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #assert isinstance(password, object)
        client.connect(hostname=hostname, port=port, username=username, password=password)
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

def main():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ssh into a server')
    parser.add_argument('hostname', help='hostname must dns resolvable or IP address.', default='localhost')
    parser.add_argument('-c', '--command', help="enter performance matrix", default='cpu_load')
    parser.add_argument('-u', '--username', help="Specify a user with ssh access to target host.", default="rhel")
    parser.add_argument('-P', '--password', help="Enter a password for the user in use.", default="rhel")
    parser.add_argument('-p', '--port', help="Specify port number default is 22.", default=22)

    print("Here are my args parsed", parser.parse_args())
    arguments = parser.parse_args()

    hostname = arguments.hostname
    command = arguments.command # get command from kal_sar.py
    username = arguments.username
    password = arguments.password
    port = arguments.port
    day = input("Which day would you like system stats, options are 1 to 31: ")
    ssh_konnector(hostname, password, username, port, get_sar(str(day)))