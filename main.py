import socket
import sys
import subprocess
from datetime import datetime

subprocess.call('clear', shell=True)

print("quik-portlist - v1.0.0")
remoteServer = input("IP Address / Host: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("-" * 50)
print("Target: ", remoteServerIP)
print("-" * 50)

starttime = datetime.now()
socket.setdefaulttimeout(0.5)

try:
    print("[", remoteServerIP, "]")
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("\033[92m", port, "\033[0m", end=" : Open\n")
        sock.close()

except KeyboardInterrupt:
    sys.exit()

except socket.gaierror:
    print("Resolve error.")
    sys.exit()

except socket.error:
    print("Service not available")
    sys.exit()

endtime = datetime.now()
total = endtime - starttime
print("Elapsed: ", total)
