# Libraries
import bs4 as bs
from urllib.request import Request, urlopen
import pandas as pd
from selenium import webdriver
import time 

# List of links for men clothes
outer_links = ["https://www.balenciaga.com/kz/men/scarves-caps-men", "https://www.balenciaga.com/kz/men/kids", "https://www.balenciaga.com/kz/men/trousers", "https://www.balenciaga.com/kz/men/shirts", "https://www.balenciaga.com/kz/men/jackets", "https://www.balenciaga.com/kz/men/knitwear", "https://www.balenciaga.com/kz/men/denim", "https://www.balenciaga.com/kz/men/jewelry-men", "https://www.balenciaga.com/kz/men/men-belts", "https://www.balenciaga.com/kz/men/keyrings-men", "https://www.balenciaga.com/kz/men/coats", "https://www.balenciaga.com/kz/men/bags", "https://www.balenciaga.com/kz/men/t-shirts-polos", "https://www.balenciaga.com/kz/men/accessories", "https://www.balenciaga.com/kz/men/small-leather-goods-men", "https://www.balenciaga.com/kz/men/glasses"]
# Empty list which will be filled by dictionaries by second parser 
data = []

for i in outer_links:
    # Parser 1. Code that gets all the links and saves in "urls" array
    driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
    driver.get(i)
    # This condition checks if the page has a button to open additional items. If yes it will click on it.
    if outer_links.index(i) > 9:
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

        # id
        id_block = soup.find('div', attrs={'class':'item-mfc'})
        id_full = id_block.find('span', attrs={'class':'item-mfc-value'}).text
        id_short = id_full[11:]
        
        # Name
        name_block = soup.find('div', attrs={'class':'item-variants-panel attributes-panel'})
        name_inner_block = name_block.find('div', attrs={'class':'item-main attributes-panel-content-data'})
        name = name_inner_block.find('h1', attrs={'class':'modelName inner'}).text

        # Price
        price_block = soup.find('div', attrs={'class':'itemPrice'})
        price_inner_block = price_block.find('span', attrs={'class':'price'})
        price = price_inner_block.find('span', attrs={'class':'value'}).text

        # Composition
        composition_block = soup.find('div', attrs={'class':'item-composition-value'})
        composition = composition_block.find('span', attrs={'class':'value'}).text

        # Description
        description_block = soup.find('div', attrs={'class':'item-description'})
        description_list = description_block.find('ul', attrs={'class':'item-description-list'})
        description = []
        for li in description_list.find_all('li'):
            desc_info = li.get_text()
            desc = desc_info.strip()
            description.append(desc)

        country = ""
        model = ""

        for i in description:
            row_text = i
            if row_text[0:4] == "Made":
                country = row_text
            if row_text[0:5] == "Model":
                model = row_text
            else:
                continue

        page_data = {
            'ID': id_short,
            'Name': name,
            'Price': price,
            'Compositon': composition,
            'Country': country,
            'Model': model
        } 

        data.append(page_data)
        time.sleep(1)

# Output
df = pd.DataFrame(data)
df = df.replace('\n',' ', regex=True)
df = df.replace('\r',' ', regex=True)
df.to_csv('final.csv', index=False)
