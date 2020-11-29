import random
from bs4 import BeautifulSoup
import requests



file = open("thousand.csv",'r')
array = []
for i in range(160):
	array.append(random.randint(1,840))
file_write = open("final_data.csv","w")
for i in range(1000):
	text = file.readline()
	file_write.write(text)
	if i in array:
		file_write.write(text)


		
page = requests.get("https://www.balenciaga.com/kz/all/accesories)
arr = []
containers = soup.findAll("a",{"class":"item-link"})
for link in containers:
    if 'href' in link.attrs:
        arr.append(link.attrs['href'])
arr = list(dict.fromkeys(arr))")
soup = BeautifulSoup(page.text,'html.parser')
for array in arr:
    page_details = requests.get(array)
    soup_d = BeautifulSoup(page_details.text,'html.parser')
    name = soup_d.find("h1",{"class":"modelName"}).text
    
    compositions = soup_d.find("p",{"class":"Composition"})
    composition = compositions.find("span",{"class":"value"}).text
    
    details = soup_d.find("ul",{"class":"item-description-list"})
    detail = details.findAll("li")
    x = "";
    for d in detail:
        x+=d.text.strip()+","
    
    product_id = soup_d.find("span",{"class":"item-mfc-value"}).text
    f.write(name.strip()+","+composition+","+x+product_id+"\n")

for b in array:
    page = requests.get(b)
    soup = BeautifulSoup(page.text,'html.parser')
    arr = []
    containers = soup.findAll("a",{"class":"item-link"})
    for link in containers:
        if 'href' in link.attrs:
            arr.append(link.attrs['href'])
    arr = list(dict.fromkeys(arr))

    for array in arr:
        page_details = requests.get(array)
        soup_d = BeautifulSoup(page_details.text,'html.parser')

        name = soup_d.find("h1",{"class":"modelName"}).text

        compositions = soup_d.find("p",{"class":"Composition"})
        composition = compositions.find("span",{"class":"value"}).text

        details = soup_d.find("ul",{"class":"item-description-list"})
        detail = details.findAll("li")
        x = "";
        for d in detail:
            x+=d.text.strip()+","

        product_id = soup_d.find("span",{"class":"item-mfc-value"}).text
        f.write(name.strip()+" , "+composition+" , "+x+product_id+"\n")

f.close()
