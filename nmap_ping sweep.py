# Record the IP addresses of an nmap ping sweep in a text file 

import nmap
import time

time_stamp=int(time.time())
obj1=nmap.PortScanner()
obj1.scan(hosts='172.20.74.0/24', arguments='-n -sP')

fh=open("nmap_ping_sweep"+str(time_stamp)+".txt","w")
fh.write('************NMAP SWEEP IPs***********\n')
for i in obj1.all_hosts():
    fh.write(i+"\n")
    fh.flush()
