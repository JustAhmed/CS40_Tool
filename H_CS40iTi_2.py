import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from os import system
from menuPrinter import HPrinter

def main2():
    auditList = ["\n\n#--------------Directory Auditor V1.0--------------#", "1. Save output to file (/root/Desktop/CS40AuditLogs.log)",
     "2. Pipe output to terminal"]
    inp = HPrinter(auditList, 2)
    if(inp == 1):
        logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                        filename="/root/Desktop/CS40AuditLogs.log")
    else:
        logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    try:
        path = input("Directory Full Path: ")
        event_handler = LoggingEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
    except:
        print("ERROR!! Invalid Directory")
        exit(2)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()