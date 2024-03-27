import sys
import paramiko
from paramiko.ssh_exception import AuthenticationException, SSHException, BadHostKeyException

def ssh_to_skytap(argv):

    try:
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(argv[0], username='dataabc', password='dataxyz', look_for_keys=False, allow_agent=False)
        stdin, stdout, stderr = conn.exec_command(argv[1])
        print "output:- %s" % str(stdout.read())
    except AuthenticationException:
        print("Authentication failed, please verify your credentials: %s")
    except SSHException as sshException:
        print("Unable to establish SSH connection: %s" % sshException)
    except BadHostKeyException as badHostKeyException:
        print("Unable to verify server's host key: %s" % badHostKeyException)
    except Exception as e:
        print("Operation error: %s" % e)


if __name__ == "__main__":
    ssh_to_skytap(sys.argv[1:])
