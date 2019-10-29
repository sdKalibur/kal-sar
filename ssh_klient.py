# !/usr/bin/env python3

import paramiko, logging, datetime , subprocess
import argparse

# Create loggeimer
log_fmt = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="ssh-klient.log",
                    level=logging.DEBUG,
                    # level = logging.INFO,
                    format=log_fmt,
                    datefmt="%m/%d/%Y %I:%M:%S %p %Z"
                    )

logger = logging.getLogger()
logTime = datetime.datetime.today().ctime()
def ssh_konnector(hostname, password, username, port, command):
    """ssh connection object"""
    """No sudo support need to work on that."""
# https://www.programcreek.com/python/example/11460/paramiko.AuthenticationException
    print("DEBUG: trying to setup connection")
    try:
        # Define connection object
        # checks for unreachable or otherwise fake hosts
        client = paramiko.SSHClient()
        client.load_host_keys('known_hosts')
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.get_transport()
        # Make connection
        client.connect(hostname=hostname,
                       port=port,
                       username=username, password=password,
                       timeout=10, auth_timeout=10,
                       gss_deleg_creds=True,
                       # allow_agent=True,
                       )
        stdin, stdout, stderr = client.exec_command(command,
                                                    get_pty=True,
                                                    )
        # stdin, stdout,stderr = client.invoke_shell()
        output = stdout.read().decode('utf-8')
        print(output)
        logger.debug("DEBUG: Executing command > " + str(command) + " :\n" + output)
        logger.error(str(hostname) + " : " + stderr)
        print(stdout)
        # raise NoValidConnectionsError(errors)
        #   paramiko.ssh_exception.NoValidConnectionsError: [Errno None] Unable to connect to port 22 on 10.42.0.2
    except paramiko.ssh_exception.NoValidConnectionsError as err:
        logger.error(err)
        print("DEBUG: Failed to establish a connection", err)
        raise err
    except paramiko.ssh_exception.AuthenticationException as err:
        logger.error(hostname, err)
        print("DEBUG: Auth failed", err)
        raise err
    except paramiko.ssh_exception.SSHException as err:
        logger.error(str(hostname) + " " + str(err))
        print("DEBUG: Auth failed", err)
        raise err
    # ERROR 10/23/2019 10:48:52 AM BST - [Errno None] Unable to connect to port 15454 on 127.0.0.1
    except:
        print("DEBUG: Some error ocured! stderr: " + str(stderr.read().decode('utf-8')))
    finally:
        # print("Stdout says : \n:", stdout.read().decode('utf-8'))
        # print("stderr says : \n:", stderr.read().decode('utf-8'))
        logger.info(str(hostname) + " " + " Closing connection now.")
        client.close()

    print("DEBUG: Closing connection now.")

    return stdout, stderr

if __name__ == '__main__':


    """
    Collects parameters to be used for creating ssh connection.
    """
    parser = argparse.ArgumentParser(description='Ssh client to run command on remote system.')
    parser.add_argument('hostname', help='hostname must dns resolvable or IP address.', default='localhost')
    parser.add_argument('-c', '--command', help="The command you wish to run on remote system.",
                        default="hostname; uptime")
    parser.add_argument('-u', '--username', help="Specify a user with ssh access to target host.")  # , default="rhel")
    parser.add_argument('-P', '--password', help="Enter a password for the user in use.")  # , default="rhel")
    parser.add_argument('-p', '--port', help="Specify port number default is 22.", default=22)

    print("DEBUG: Here are my args parsed", parser.parse_args())
    arguments = parser.parse_args()

    hostname = arguments.hostname
    command = arguments.command  # get command from kal_sar.py
    username = arguments.username
    password = arguments.password
    port = arguments.port
    ssh_konnector(hostname, password, username, port, command)
