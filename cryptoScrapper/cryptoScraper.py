import re
from bs4 import BeautifulSoup
import requests,openpyxl

excel=openpyxl.Workbook()
sheet=excel.active
sheet.append(['Name','Tag','Price','Change'])
class CryptoScrapper:

    def __init__(self,url) -> None:
        self.url=url

    def action(self):
        self.crypto=requests.get(self.url)
        self.pricePage=BeautifulSoup(self.crypto.text,'html.parser')
        self.rows=self.pricePage.find_all(role='row')
        self.rows=self.rows[1:]
        for i in self.rows:
            temp=i.find_all('div',class_=re.compile(r'css-*?'))
            temp2=i.find_all(class_='chakra-text')

            realArr=[]
            for j in temp2:
                realArr.append(j.text)
            realArr=realArr[:3]
        
            temp1=""
            for j in temp:
                if(j.text==' ' or j.text=='\n'):continue
                temp1+="\t"+j.text
                
            temp1=temp1.strip().split('\t')
            temp1=temp1[3:-1]
            realArr.append(temp1[1])
            
            realArr[2],realArr[3]=realArr[3],realArr[2]
            sheet.append(realArr)





c=CryptoScrapper('https://crypto.com/price')
c.action()


for i in range(250):
    c.url='https://crypto.com/price?page='+str(i)
    c.action()

excel.save('crypto.xlsx')


"""Initial implementation without class if anyone wants just for one page"""
# crypto=requests.get('https://crypto.com/price')
# crypto.raise_for_status()

# pricePage=BeautifulSoup(crypto.text,'html.parser')
# rows=pricePage.find_all(role='row')
# rows=rows[1:]
# for i in rows:
#     temp=i.find_all('div',class_=re.compile(r'css-*?'))
#     temp1=""
#     for j in temp:
#         if(j.text==' ' or j.text=='\n'):continue
#         temp1+="\t"+j.text
        
#     temp1=temp1.strip().split('\t')
#     temp1=temp1[3:-1]
#     change=temp1[2]
#     if change.find('+')>-1:
#         change=change[change.find('+'):]
#     else:
#         change=change[change.find('-'):]
#     temp1[2]=change
#     print(temp1)
#     sheet.append(temp1)