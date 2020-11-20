# Libraries
import bs4 as bs
from urllib.request import Request, urlopen
import pandas as pd
from selenium import webdriver
import time 

# List of links for men clothes
outer_links = ["https://www.balenciaga.com/kz/men/shirts", "https://www.balenciaga.com/kz/men/trousers", "https://www.balenciaga.com/kz/men/jackets", "https://www.balenciaga.com/kz/men/coats", "https://www.balenciaga.com/kz/men/t-shirts-polos"]
# Empty list which will be filled by dictionaries by second parser 
data = []

for i in outer_links:
    # Parser 1. Code that gets all the links and saves in urls array
    driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
    driver.get(i)
    # This condition checks if the page has a button to open additional items. If yes it will click on it.
    if outer_links.index(i) > 2:
        driver.find_element_by_class_name('viewmore-btn').click()
        driver.find_element_by_class_name('viewmore-btn').click()
        time.sleep(3)
    content = driver.page_source
    soup = bs.BeautifulSoup(content, 'lxml')
    block = soup.find('div', attrs={'class':'shelf-viewport'})
    unordered_list = block.find('ul', attrs={'class':'products container'})

    urls = []
    for h3 in unordered_list.findAll('h3', attrs={'class':'item-display-title'}):
        for a in h3.find_all('a', href=True):
            links = a['href']
            urls.append(links)
    driver.quit()

    # Parser 2. Code that takes links from urls array and opens each page to parse data
    for i in urls:
        site = i
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site,headers=hdr)
        page = urlopen(req)
        soup = bs.BeautifulSoup(page, 'lxml')

        # Price
        price_block = soup.find('div', attrs={'class':'itemPrice'})
        price_inner_block = price_block.find('span', attrs={'class':'price'})
        price = price_inner_block.find('span', attrs={'class':'value'}).text

        # Composition
        composition_block = soup.find('div', attrs={'class':'item-composition-value'})
        composition = composition_block.find('span', attrs={'class':'value'}).text

        page_data = {
            'Price': price,
            'Compositon': composition
        } 

        data.append(page_data)
        time.sleep(1)

# Analyzing part
# Initial lists for materials prices
cotton0 = []
polyester0 = []
lyocell0 = []
polyamide0 = []
wool0 = []
calfskin0 = []

# Loop which goes through the list and checks the consistency of material and appends them into initial lists for materials prices
for index in range(len(data)):
    for key in data[index]:
        if "Cotton" in (data[index]['Compositon']):
            cotton0.append(data[index]['Price'])
        if "Polyester" in (data[index]['Compositon']):
            polyester0.append(data[index]['Price'])
        if "Lyocell" in (data[index]['Compositon']):
            lyocell0.append(data[index]['Price'])
        if "Polyamide" in (data[index]['Compositon']):
            polyamide0.append(data[index]['Price'])
        if "Wool" in (data[index]['Compositon']):
            wool0.append(data[index]['Price'])
        if "Calfskin" in (data[index]['Compositon']):
            calfskin0.append(data[index]['Price'])

# Final lists for materials prices
cotton = []
polyester = []
lyocell = []
polyamide = []
wool = []
calfskin = []

# Part for removing a Unicode NoBreak Space character (\xa0)  
for i in cotton0: 
    new_string = i.replace('\xa0', "")
    cotton.append(new_string)
for i in polyester0: 
    new_string = i.replace('\xa0', "")
    polyester.append(new_string)
for i in lyocell0: 
    new_string = i.replace('\xa0', "")
    lyocell.append(new_string)
for i in polyamide0: 
    new_string = i.replace('\xa0', "")
    polyamide.append(new_string)
for i in wool0: 
    new_string = i.replace('\xa0', "")
    wool.append(new_string)
for i in calfskin0: 
    new_string = i.replace('\xa0', "")
    calfskin.append(new_string)

# Part for converting strings to integers
for i in range(0, len(cotton)): 
    cotton[i] = int(cotton[i])
for i in range(0, len(polyester)): 
    polyester[i] = int(polyester[i])
for i in range(0, len(lyocell)): 
    lyocell[i] = int(lyocell[i])
for i in range(0, len(polyamide)): 
    polyamide[i] = int(polyamide[i])
for i in range(0, len(wool)): 
    wool[i] = int(wool[i])
for i in range(0, len(calfskin)): 
    calfskin[i] = int(calfskin[i])

# Part to find a sum of prices for each material
cotton_sum = 0
for i in range(0, len(cotton)):
    cotton_sum = cotton_sum + cotton[i]
polyester_sum = 0
for i in range(0, len(polyester)):
    polyester_sum = polyester_sum + polyester[i]
lyocell_sum = 0
for i in range(0, len(lyocell)):
    lyocell_sum = lyocell_sum +  lyocell[i]
polyamide_sum = 0
for i in range(0, len(polyamide)):
    polyamide_sum = polyamide_sum + polyamide[i]
wool_sum = 0
for i in range(0, len(wool)):
    wool_sum = wool_sum + wool[i]
calfskin_sum = 0
for i in range(0, len(calfskin)):
    calfskin_sum = calfskin_sum + calfskin[i]

# Part to find an average of prices for each material
cotton_avg = cotton_sum / len(cotton)
polyester_avg = polyester_sum / len(polyester)
lyocell_avg = lyocell_sum / len(lyocell)
polyamide_avg = polyamide_sum / len(polyamide)
wool_avg = wool_sum / len(wool)
calfskin_avg = calfskin_sum / len(calfskin)

analyzed_data = {
    'Cotton': [cotton_avg],
    'Polyester': [polyester_avg],
    'Lyocell': [lyocell_avg],
    'Polyamide': [polyamide_avg],
    'Wool': [wool_avg],
    'Calfskin': [calfskin_avg]
}

# Output
df = pd.DataFrame(analyzed_data)
df = df.replace('\n',' ', regex=True)
df = df.replace('\r',' ', regex=True)
df.to_excel('analyze.xlsx', index=False)
