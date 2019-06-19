
#!/usr/bin/env python3

import paramiko,sys, subprocess
import argparse

from kal_sar import get_sysstat_day as get_sar


def ssh_konnector(hostname ='localhost', port=22, username='rhel', password='rhel', command='uptime',  *args):
    # if len(sys.argv) < 4:
    #     print("args missing")
    #     sys.exit()


    # hostname = sys.argv[1]
    port = 22
    # password = sys.argv[2]
    # command = sys.argv[3]

    # command = get_sar()

    # username = 'rhel'
    # password = 'rhel'
    # port = 22
    print(hostname, username, password, command)
    command = input("enter your command: ")
    print("trying to setup connection")
    try:
        client = paramiko.SSHClient()
        client.load_host_keys('known_hosts')
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #assert isinstance(password, object)
        client.connect(hostname, port=port, username=username, password=password)
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
    ssh_konnector(*args)