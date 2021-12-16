#imports exists for current method, winreg for new unfinished method, and time for another unused method
from os.path import exists
import winreg
import time

#querying file existance for SPBully asi and Bully exe
file_existsSP = exists('C:/Program Files (x86)/Steam/steamapps/common/Bully Scholarship Edition/SilentPatchBully.asi')
file_existsBL = exists('C:/Program Files (x86)/Steam/steamapps/common/Bully Scholarship Edition/Bully.exe')

#if both files exist, return true that SPBully is installed // else if a file is missing(aka, not both found) then return false 
if file_existsSP and file_existsBL:
    print("SilentPatchBully is installed in the correct directory")
elif not file_existsSP and file_existsBL:
    print("SilentPatchBully is NOT installed correctly.. Place all files in the main Bully Directory.")
input()

#NOTES:
#Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Valve\Steam\Apps\12200 - location of bully directory i think