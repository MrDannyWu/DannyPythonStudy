import requests
from pathlib import Path
import os

class DownloadFile():

    def download(self,url):
        file_path = '/home/dannywu/Downloads'
        print(file_path)
        file_path = Path(file_path)
        data = requests.get(url)
        if (file_path.exists()):
            #name = str(file_path) + '/' + 'baidu.ico'
            #print(name)
            with open(str(file_path) + '/v0.8.1.tar.gz','wb') as f:
                f.write(data.content)
            print("Finished!")
        else:
            os.mkdir(file_path)
            with open(str(file_path) + '/v0.8.1.tar.gz','wb') as f:
                f.write(data.content)
            print("Finished!")


dl = DownloadFile()
url = 'https://github.com/zayronxio/Macos-sierra-CT/archive/v0.8.1.tar.gz'
print("Downloading...")
dl.download(url)
print("Finished!")
