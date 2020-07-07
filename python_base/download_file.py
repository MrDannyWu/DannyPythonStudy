# Mycode
import requests
from pathlib import Path
import os

class DownloadFile():

    def download(self,url):
        file_path = 'E:\\DannyWu\\Desktop\\pytest'
        print(file_path)
        file_path = Path(file_path)
        data = requests.get(url)
        if (file_path.exists()):
            #name = str(file_path) + '/' + 'baidu.ico'
            #print(name)
            with open(str(file_path) + '\\baidu.ico','wb') as f:
                f.write(data.content)
            print("Finished!")
        else:
            os.mkdir(file_path)
            with open(str(file_path) + '\\baidu.ico','wb') as f:
                f.write(data.content)
            print("Finished!")


dl = DownloadFile()
url = 'https://www.baidu.com/favicon.ico'
dl.download(url)
