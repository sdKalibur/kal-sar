import paramiko

 # |      client = SSHClient()
 # |      client.load_system_host_keys()
 # |      client.connect('ssh.example.com')
 # |      stdin, stdout, stderr = client.exec_command('ls -l')

def copy_file(hostname, port, username, password, src, dst):
    client = paramiko.SSHClient()
    client.load_host_keys('sample.csv')
    print("connecting to %4 \n with username=%s....\n" %(hostname, username))
    t = paramiko.Transport(hostname, port)
    t.connect(username=rhel,password=rhel)
    sftp = paramiko.SFTPClient.from_transport(t)
    print("copying file:;;;; %s " %(src, dst))
    sftp.put(src,dst)
    sftp.close()
    t.close()


copy_file('localhost', '22', 'rhel', 'rhel', 'sampple.csv', '/tmp/')