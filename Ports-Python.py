import socket
import sys
try:
    import nmap
except:
    import os
    os.system('pip3 instal python-nmap')
    os.system('clear')

line = "---------------------------------------------------------------"

if len(sys.argv)!=3:
    print(' python3 Ports-Python.py <Host_Address> <Ports_Range>')
    sys.exit(0)

hostaddress = sys.argv[1]
portsrange = sys.argv[2]

ipaddress = socket.gethostbyname(hostaddress)

print(line)
print('    Please wait... Now scaning ' + ipaddress)
print(line)

try:
    nmscan=nmap.PortScanner()
    nmscan.scan(hostaddress, portsrange)

except:
    print('    Program Stoped...')
    sys.exit(0)

for host in nmscan.all_hosts():
    print('    Host :      |%s(%s)' % (host, hostaddress))
    print('    Status :    |%s' % nmscan[host].state())
    for proto in nmscan[host].all_protocols():
        print(line)
        print('    Protocols : |%s ' % proto)
        
        lport = nmscan[host][proto].keys()
        sorted(lport)
        for port in lport:
            print('    Port :      |%s \t State : %s ' %(port,nmscan[host][proto][port]['state']))
