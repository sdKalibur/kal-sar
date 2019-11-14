from pylab import *

t = arange(0.0,2.0,0.001)
s = sin(2*pi*t)
plot(t, s, linewidth= 1.0)

xlabel('Time (s)')
ylabel('Voltage (mV)')
title('About as simple as it gets, folks')
grid(True_)
show()


# import paramiko
#
# def copy_file(hostname, port, username, password, src, dst):
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     print (" Connecting to %s \n with username=%s... \n" %(hostname,username))
#     t = paramiko.Transport(hostname, port)
#     t.connect(username=username,password=password)
#     sftp = paramiko.SFTPClient.from_transport(t)
#     print ("Copying file: %s to path: %s" %(src, dst))
#     sftp.put(src, dst)
#     sftp.close()
#     t.close()
#
# def execute_ssh_command(self, command):
#     """Executes command on switch.
#
#     Args:
#         command(str):  ssh command to execute
#
#     """
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#     # Make connection and create shell.
#     client.connect(self.ipaddr, self._sshtun_port, self.ssh_user, self.ssh_user_pass)
#     shell = client.invoke_shell()
#
#     # Execute command and get results.
#     _, stdout, stderr = client.exec_command(command)
#     data = self._read_command_output(stdout, stderr, 'both')
#
#     # Close connection.
#     shell.close()
#     client.close()
#
#     return data
#
# def exec_remote_list_of_cmds(hostname, commands, username='root', port=22, sudo=False):
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(hostname, port=port, username=username)
#
#     returned_array = []
#
#     for command in commands:
#         # log.debug('command to launch in ssh in {}: {}'.format(hostname, command))
#         stdin, stdout, stderr = client.exec_command(command)
#         out = stdout.read().decode('utf-8')
#         err = stderr.read().decode('utf-8')
#         returned_array.append({'out': out, 'err': err})
#         # log.debug('commnad launched / out: {} / error: {}'.format(out, err))
#
#     client.close()
#
#     return returned_array
#
# #
# arguments = parser.parse_args()
# arguments.method(**vars(arguments))