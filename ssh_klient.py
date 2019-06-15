
#!/usr/bin/env python3

import paramiko,sys, subprocess

 # |      client = SSHClient()
 # |      client.load_system_host_keys()
 # |      client.connect('ssh.example.com')
 # |      stdin, stdout, stderr = client.exec_command('ls -l')
#
# def copy_file(hostname,port,username,password,src,dst):
#     client = paramiko.SSHClient()
#     client.load_host_keys('sample.csv')
#     print("connecting to %s \n with username=%s....\n" %(hostname,username))
#     t = paramiko.Transport(hostname, port)
#     t.connect(username='rhel', password='rhel')
#     sftp = paramiko.SFTPClient.from_transport(t)
#     print("copying file:...%s " %(src, dst))
#     sftp.put(src,dst)
#     sftp.close()
#     t.close()
#
#
# copy_file('localhost',22, 'rhel','rhel', 'sample.csv', '/tmp/')

if len(sys.argv) < 4:
    print("args missing")
    sys.exit()


hostname = sys.argv[1]
password = sys.argv[2]
command = sys.argv[3]

username = 'rhel'
# password = 'rhel'
port = 22

try:
    client = paramiko.SSHClient()
    client.load_host_keys('/home/rhel/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    assert isinstance(password, object)
    client.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read())
    print(stderr.read())
    # msg = subprocess.getoutput(client.connect(hostname, port=port, username=username, password=password))
    # print('My output: ', msg)


finally:
    client.close()