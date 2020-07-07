import os
from pathlib import Path
import shutil

tc_cache_path = "E:\\DannyWu"
files = os.listdir(tc_cache_path)
open_path = "start explorer " + str(tc_cache_path)
os.system(open_path) #c:为要打开c盘，也可以改成其他路
for file1 in files:
    if ('fcc' in file1):
        os.remove(tc_cache_path + "\\" + file1)
    if("Teamcenter" in file1):
        shutil.rmtree(tc_cache_path + "\\" + file1)
    if('FCCCache' in file1):
        shutil.rmtree(tc_cache_path + "\\" + file1)
    print(file1)
print()
print("######Cleanup finished !######")
