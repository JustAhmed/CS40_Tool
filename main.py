import os
import H_CS40iTi_5
import H_CS40iTi_4
import H_CS40iTi_3
import H_CS40iTi_2
import H_CS40iTi_1
from menuPrinter import HPrinter

if __name__ == "__main__":
    mainList = ["Welcome to CS40 tool V1 (Developed By Ahmed Hesham)", "1. Log Parser", "2. Directory Watcher", "3. Port Scanner", "4. Attack Detection", "5. Web Scraper"]
    inp = HPrinter(mainList, 5)
    if inp == 1:
        H_CS40iTi_1.main1()
    elif inp == 2:
        H_CS40iTi_2.main2()
    elif inp == 3:
        H_CS40iTi_3.main3()
    elif inp == 4:
        H_CS40iTi_4.main4()
    elif inp == 5:
        H_CS40iTi_5.main5()