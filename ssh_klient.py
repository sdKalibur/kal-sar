
#!/usr/bin/env python3

import paramiko,sys, subprocess
from kal_sar import main as get_sar


def ssh_konnector(hostname ='localhost', command='ls', *args):
    # if len(sys.argv) < 4:
    #     print("args missing")
    #     sys.exit()


    # hostname = sys.argv[1]
    port = 22
    # password = sys.argv[2]
    # command = sys.argv[3]

    command = get_sar()

    username = 'kalibur'
    password = 'p4ss3d'
    port = 22

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
ssh_konnector(hostname='kalibur-mce', command="sadf   -d   --  /var/log/sysstat/sa15     -s 12:00 -e 17:00   -q")

def main():
    pass

if __name__ == '__main__':
    ssh_konnector()