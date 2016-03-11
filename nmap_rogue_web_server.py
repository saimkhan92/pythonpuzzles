# Record the IP addresses of an nmap ping sweep in a text file 

import nmap
import time

time_stamp=int(time.time())
obj1=nmap.PortScanner()
obj1.scan(hosts='172.20.74.0/24', arguments='-p 80,443,8080')

fh=open("nmap_rogue_server"+str(time_stamp)+".txt","w")
fh.write('************NMAP SWEEP IPs***********\n')
for i in obj1.all_hosts():
    j=i.split(".")
    #print(j)
    if int(j[3]) not in range(1,11): 
        fh.write(i+"\n")
        fh.flush()
