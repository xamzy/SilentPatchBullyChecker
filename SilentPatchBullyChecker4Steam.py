#imports exists for current method, winreg for new unfinished method, and time for another unused method
import os
from os.path import exists
import winreg
#import requests
#piimport shutil
import time
import itertools


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
            "modupdater.ini",
            "SilentPatchBully.asi",
            "SilentPatchBully.ini"]

#for the files in the list, check if the source code is there, if so - bail, then/or check if a file is missing, if so - print incorrect.
for file in filelist:
    if exists("SilentPatchBully.cpp") or exists("README.md"):
        print(f"You have downloaded the source code. \nPlease download SilentPatchBully.zip from the releases tab instead.")
        #print(f"\nThis can be done for you automatically. Would you like to download the source code?")
        #input(f"\nPress Any Key to start installing SilentPatchBully")
        #r = requests.get(url)

        break
    elif not os.path.exists(file):
        notinstalled = print(f"SilentPatchBully is NOT installed correctly. Place all files in the main Bully Directory.\nYou can find the correct location here: {key[0]}")
        break
#else if all files exist, print true that SPBully is installed correctly
else:
    print("SilentPatchBully is installed in the correct directory")
    
input("\nYou may now close this program.")
