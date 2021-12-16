###############################################
#WINDOWS VER 0.1
#CREATED BY GITHUB.COM/XAMZY
###############################################

#imports exists for current method, winreg for new unfinished method, and time for another unused method
from os.path import exists
import os
import winreg
import time
import itertools

#locates Bully install directory from registry and stores it in key
test = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 12200")
key = winreg.QueryValueEx(test, r"InstallLocation")

#changes directory to stored location in key and checks if Bully.exe and SilentPatchBully.asi are in said directory with no folders seperating them
os.chdir(key[0])
file_existsBL = exists('Bully.exe')
file_existsSP = exists('SilentPatchBully.asi')

#if both files exist, return true that SPBully is installed correctly // else if a file is missing(aka, not both found) then return false 
if file_existsSP and file_existsBL:
    print("SilentPatchBully is installed in the correct directory")
    input()
#else if any of these files are missing, tells you where to put them.
elif not file_existsSP or not file_existsBL:
    print("SilentPatchBully is NOT installed correctly.. Place all files in the main Bully Directory. You can find the correct location here: ")
    #test = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 12200")
    #key = winreg.QueryValueEx(test, r"InstallLocation")
    print(key[0])
input()
