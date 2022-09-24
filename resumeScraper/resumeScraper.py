from bs4 import BeautifulSoup
import requests,openpyxl

#excel setup
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title='Skills'
sheet.append(['Skill','Profiency'])

#initial setup
resume=requests.get('https://skrb7f16.netlify.com/')
resume.raise_for_status()
RESUME=BeautifulSoup(resume.text,'html.parser')

#extract skills
skills=RESUME.find(id='skills').find_all(class_='content')
skillDict={}
for i in skills:
    temp=i.find_all('span',class_='heading')
    temp1=i.find_all('span',class_='row')
    for j,k in zip(temp,temp1):
        skillDict[j.text]=int(k.text.strip()[:2])
#Saving skills 
for i in skillDict:
    sheet.append([i,skillDict[i]])
print(excel.sheetnames)

excel.create_sheet("Project")


projects=RESUME.find(id='projects').find_all(class_='row')
projectDic={}
print(projects)
for i in projects:
    temp=i.find_all(class_='head')
    temp1=i.find_all(class_='body')
    print(temp1)
    for j,k in zip(temp,temp1):
        temp=k.text.strip().split('\n')
        print(temp)
        t=[]
        for i in temp:
            print(i.strip())
            t.append(i.strip())
        projectDic[j.text.strip()]=' '.join(t)
print(projectDic)
excel.active=excel['Project']
sheet=excel.active
for i in projectDic:
    sheet.append([i,projectDic[i]])

excel.save('skill.xlsx')