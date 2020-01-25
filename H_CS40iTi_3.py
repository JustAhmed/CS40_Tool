import os
import re
import time
import socket
import subprocess
from menuPrinter import HPrinter

IP_Port = {}
def pscan(target, start=0, end=444):
    host = socket.gethostbyname(target)
    for port in range(start, end):
        scannerTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        status = scannerTCP.connect_ex((host, port))

        if not status:
            IP_Port[target].append(str(port))

        scannerTCP.close()

def IPFilter(UpHosts):
    filtered = []
    for ip in UpHosts:
        res = subprocess.Popen("ping -c 2 " + ip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
        if "ttl" in str(res.stdout.read(), "utf-8"):
            filtered.append(ip)
    return filtered

def main3():
    res = subprocess.Popen("arp-scan -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
    res = str(res.stdout.read(), "utf-8")
    ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
    UpHosts = list(set(ips))
    print("Scanning your network for up hosts.....")
    UpHosts_NoFireWall = IPFilter(UpHosts)

    if len(UpHosts_NoFireWall):
        print("Ping sweep complete! " + str(len(UpHosts_NoFireWall)) + " hosts found!\nInitiating port scanner.......")
        time.sleep(2)

        for ip in UpHosts_NoFireWall:  
            IP_Port[ip] = []
            print("Scanning " + ip + " ........")
            pscan(ip)
    
    print("\nScan Complete!!\n Feeding Results to Nmap....")
    #print(IP_Port) #Debugging
    nmapList = ["1. Save results to file (/root/Desktop/Hmap.txt)", "2. Write results to screen"]
    inp = HPrinter(nmapList, 2)
    f = None
    if inp == 1:
        f = open("/root/Desktop/Hmap.txt", "w")
    for i in IP_Port:
        if len(IP_Port[i]):
            print(f"\n\n<==================Scanning {i}==================>")
            portS = ','.join(IP_Port[i])
            nmapCMD = "nmap -sC -sV -p " + portS + " " + i
            res = os.popen(nmapCMD).read()
            ports = re.findall(r'\d+/tcp.+', res)
            
            if inp == 2:
                print("\n".join(ports))
                print("\n\n")
            else: 
                f.write("<<<<<< IP: " + i + " >>>>>>\n")
                f.write("\n".join(ports))
                f.write("\n----------------------------------------------------------\n")
        else:
            if inp == 2:
                print("No open ports to be scanned ;)\n\n")
            else: 
                f.write("<<<<<< IP: " + i + " >>>>>>\n")
                f.write("No open ports to be scanned ;)\n")
                f.write("\n----------------------------------------------------------\n")
    if inp == 1:
        f.close()