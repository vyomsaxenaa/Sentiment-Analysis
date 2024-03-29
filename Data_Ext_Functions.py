import pandas as pd
from bs4 import BeautifulSoup
import requests
import openpyxl
path=r"C:\Users\Sid\Desktop\Vyom's Python\Input.xlsx"
class extraction:
    def __init__(self,path):
        self.path=path
    def read_excel(self):
        self.data=pd.read_excel(self.path)
        df=pd.DataFrame(self.data,columns=["URL"])
        self.data=df["URL"]
        return(self.data)
    def extract_text(self,data):
        count=0
        for i in range(len(self.data)):
            count+=1
            url=self.data[i]
            headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
            }
            res=requests.get(url,headers=headers)
            html_page=res.content
            soup=BeautifulSoup(html_page, "html.parser")
            self.text=soup.getText(strip=True)
            print(count)
            return(self.text)
    def save_text(self,text,data):
        with open("save_file.txt","a") as file:
            for i in range(len(self.data)):
                file.write(self.text+"\n")
            file.close()




        

