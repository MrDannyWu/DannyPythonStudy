import io
import os
from pathlib import Path
str1 = "我是中国人"
file_path = 'E:\\DannyWu\\Desktop\\python_files'
#os.mkdir(file_path)
#name = file_path + "\\test"
#for i in range(10):
#    with open(name + str(i+1) +".txt",'w') as f:
#        f.write(str1)
#        print(f.name)

#with open("E:\\text1.txt",'r+') as r:
#    str2 = r.read()
#    print(str2)


#os.rename("E:\\text1.txt","E:\\text2.txt")
#print("Rename Successful!")


#file_name = "E:\\text2.txt"
#os.remove(file_name)
#print()
#print("Remove File Successful!")
#print()

#os.chdir('../')
#print(os.getcwd())
#print(os.listdir(os.getcwd()))
#dir_list = os.listdir(os.getcwd())
#for dir1 in dir_list:
#    print(dir1)


path1 = Path(file_path)
print(path1.exists())

print(path1.is_file())

try: 
    my_path = path1.resolve()
except FileNotFoundError:
    print("FileNotFound")
else:
    print(my_path)
