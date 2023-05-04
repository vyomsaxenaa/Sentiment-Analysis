from bs4 import BeautifulSoup
import pandas as pd
import requests
import Data_Ext_Functions as fn
path=r"C:\Users\Sid\Desktop\Vyom's Python\Input.xlsx"
obj=fn.extraction(path)
#Reading excel file
read_file=obj.read_excel()
#Extracting text from URL
extract_file=obj.extract_text(read_file)
#Saving Extracted text
obj.save_text(read_file,extract_file)
