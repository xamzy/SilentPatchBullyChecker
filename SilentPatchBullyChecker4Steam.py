###############################################
#WINDOWS VER 1.0
#GITHUB.COM/XAMZY
###############################################

#imports exists for current method, winreg for new unfinished method, and time for another unused method
import os
import winreg
import time
import itertools

#locates Bully install directory from registry and stores it in key
locate = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 12200")
key = winreg.QueryValueEx(locate, r"InstallLocation")

#changes directory to stored location in key and checks if Bully.exe and SilentPatchBully.asi are in said directory with no folders seperating them
os.chdir(key[0])

#creates a list of all the files required for SPBully
filelist = ["Bully.exe",
            "dinput8.dll",
            "MiniDumper.asi",
            "modupdater.asi",
            "modupdater.ini",
            "SilentPatchBully.asi",
            "SilentPatchBully.ini"]

#if any of these files are missing, tells you where to put them.
for file in filelist:
    if not os.path.exists(file):
        print(f"SilentPatchBully is NOT installed correctly. Place all files in the main Bully Directory.\nYou can find the correct location here: {key[0]}")
        break
#else if all files exist, print true that SPBully is installed correctly
else:
    print("SilentPatchBully is installed in the correct directory")

input("\n You may now close this program.")
