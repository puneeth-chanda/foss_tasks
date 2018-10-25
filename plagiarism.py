from bs4 import BeautifulSoup
import requests
m=str(input("file name:"))
file1=open(r"/home/puneeth/Desktop/fossentry/"+m,"r")
a=file1.readline()
r=requests.get("http://www.google.com/search?btnG=1&q="+a)
data=r.text
soup=BeautifulSoup(data,"html.parser")
k=soup.select("h3")
for i in k:
	name=i.get_text()
	print(name)
	#

