#imports exists for current method, winreg for new unfinished method, and time for another unused method
import os
from os.path import exists
import winreg
#import wget
import requests
import re
import shutil
import time
import itertools
from zipfile import ZipFile


#locates Bully install directory from registry and stores it in key
locate = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 12200")
key = winreg.QueryValueEx(locate, r"InstallLocation")

#changes directory to stored location in key
os.chdir(key[0])

#sets url var for github (unused in this ver)
url = "https://github.com/CookiePLMonster/SilentPatchBully/releases/download/BUILD-3-TEST/SilentPatchBully.zip"

#list of all the files it checks for
filelist = ["Bully.exe",
            "dinput8.dll",
            "MiniDumper.asi",
            "modupdater.asi",
            "SilentPatchBully.asi",
            "SilentPatchBully.ini"]

#for the files in the list, check if the source code was incorrectly added or if a file is missing
for file in filelist:
    if exists("SilentPatchBully.cpp") or exists("README.md") or not os.path.exists(file):
        print(f"You have not installed SilentPatchBully correctly.")
        print(f"\nThis can be done for you automatically. Would you like to download it now?")
        input(f"\nPress Any Key to start installing SilentPatchBully")

        #if that was the case, get request the patch, open with write perms
        r = requests.get(url, allow_redirects=True)
        open('SilentPatchBully.zip', 'wb').write(r.content)
        if url.find('/'):
            print(url.rsplit('/',1)[1])
                    #cur_directory = os.getcwd()
                    #shutil.move(cur_directory, key)
            #take the zip file, extract it to the bully directory and complete.
            with ZipFile('SilentPatchBully.zip', 'r') as zip:
                print(f"\nInstalling...")
                zip.extractall()
                print(f"Install Complete! SilentPatchBully is now installed!")
        break

#else if all files exist, print true that SPBully is installed correctly
else:
    print("SilentPatchBully is installed in the correct directory")
    
input("\nYou may now close this program.")
