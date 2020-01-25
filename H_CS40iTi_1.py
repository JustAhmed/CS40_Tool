import os
from menuPrinter import HPrinter

def parseLogs(logs):
    IPs = []
    URIs = []
    AccessMethods = []
    UserAgents = []
    try:
        for log in logs:
            IPs.append(log[0])
            AccessMethods.append(log[5])
            URIs.append(log[6])
            UserAgents.append(' '.join(log[11:-1]))
    except IndexError:
        print("Error! Make sure you imported access logs in proper format!")

    return IPs, URIs, AccessMethods, UserAgents

def getLogs(fileName):
    try:
        f = open(fileName, 'r')
        raw_logs = f.readlines()
        logs = []
        for log in raw_logs:
            logs.append(log.split())
    except:
        print("Error! Invalid/Corrupt file\nQuitting....")
        exit(1)
    return logs

def main1():
    print("Parsing Logs")
    f = input("access.log absolute path: ")
    logs = getLogs(f)
    IPs, URIs, AccessMethods, UserAgents = parseLogs(logs)

    #Unique

    UIPs = "\n".join(list(set(IPs)))
    UURIs = "\n".join(list(set(URIs)))
    UAccessMethods = "\n".join(list(set(AccessMethods)))
    UUserAgents = "\n".join(list(set(UserAgents)))

    t1List = ["\n\nParsing Complete!", "1. Display Output", "2. Save it to file (/root/Desktop/parsedLogs.txt)"]
    opt = HPrinter(t1List, 2)
    if opt == 1:
        print("\n#---------------------Unique IPs---------------------#")
        print(UIPs)

        print("\n#---------------------Unique URIs---------------------#")
        print(UURIs)

        print("\n#---------------------Unique Access Methods---------------------#")
        print(UAccessMethods)

        print("\n#---------------------Unique User Agents---------------------#")
        print(UUserAgents)
    else:
        f = open("/root/Desktop/logsParsed.txt", "w")
        f.write("\n#---------------------Unique IPs---------------------#")
        f.write(UIPs)

        f.write("\n\n#---------------------Unique URIs---------------------#")
        f.write(UURIs)

        f.write("\n\n#---------------------Unique Access Methods---------------------#")
        f.write(UAccessMethods)

        f.write("\n\n#---------------------Unique User Agents---------------------#")
        f.write(UUserAgents)
        f.close()
    print("\n\n\nDone!!!")