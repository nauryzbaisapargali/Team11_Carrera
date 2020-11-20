# Team11 Carrera's Project 1 

This repository includes 3 parser's for 3 parts of Balenciaga(https://www.balenciaga.com/kz) website.
First parser is Ulan's parser for men clothes
Second parser is Nauryzbay's parser for shoes
Third parser is a Zhalgaskhan's parser for women clothes
Additionally, there are anaysis code of Dayana and Ulan

## Tools

Code was written in Python 3 with Beautiful Soup and Selenium libraries along with Pandas library

## Usage

Each file with parser or analyzer code can be launched to parse and get result of analysis

## Description

## Description of Ulan’s methods for parsing:

My part was to parse the data from men’s clothes and accessories.  I used Pandas, Beautiful Soup and Selenium libraries for scraping. Firstly, there is a list which contains links for every type of cloth and accessory. From this list links one by one are opened by the loop which covers almost all of the program. I divided my program inside this loop to 2 parsers. First parser uses Beautiful Soup and Selenium libraries. Selenium takes the links and opens it in browser window, also there is a condition which checks the existence of button to open additional items (not all pages has this button), and Beautiful Soup parses links of each item and saves it in a list. Then window of browser closes. After the second parser starts to work. Second parser uses only Beautiful Soup. This parser takes one link for one item and parses its id, name, price, composition, country and model. Then all of these data will be saved in dictionary and this dictionary will be appended to outer list which will save all the dictionaries for each item. In this list each index is one row in csv file. Finally, Pandas creates data frame on the basis of the list and converts it to csv file.

## Description of Nauryzbay’s methods for parsing:

After we split the parts, I got the shoe department. Now it was necessary to find out how to parse the site (which language is better to use, which library is more convenient, etc.). Until that time, I had not encountered site parsing, and then I had to learn. I looked at several tutorials from You Tube, I also looked for ready-made codes from Google. But the video I watched turned out to be old and they also used the old "Beautiful soup" library. I found out the new version from my teammates Zhalgaskhan and he helped me by showing me which library he was using.
When I already understood the essence and started parsing, I found out that all the data that I need is in another link under the link. I thought to go to each site manually, but it will not be authorized. And I decided to add all these links to the array and enter them in turn. 
When I had already done everything and displayed a table for comparing whether the data in the site and in my table matched, I saw that there was not enough data. I started to analyze my code, but I couldn't find anything. Then I started looking on the site, and I found out that they take most of their data from ajax. But no matter how hard I tried, I could not take the link of these ajax. Out of hopelessness, I asked my friends what to do next, they said that the Selenium library easily solves this problem. And so it happened, I added all the links to another array. After I had all the links, I was left with the current to repeat the previous cycle. 
In the end, I had all the data about the shoes that was on the site. It was difficult for me, but also a very good experience for the future.

## Description of Zhalgaskhan’s methods for parsing:

## Description of Ulan’s methods for analyzing material / price dependency:

In the analysis to understand the connection between price and material type, I created a loop which will check composition and find a substring which consists the name of material. If an item has a name of material in its composition string, the price of this item will be appended to the list of prices of this type of material. Then, the sum of all prices for each type of material will be taken in order to find the average price for each type of material. Finally, all of these data will be saved in dictionary and transformed to data frame by Pandas library tools, then this data frame turned to excel file. In the final output in xlsx file I have a different number of materials and the average price for clothes which consists them. To create this data more understandable I just used Excel functionality and created a graph which ideally shows the connection between material and price.
  
## Description of Dayana’s methods for analyzing manufacturer country / price dependency:

Also, to us it is very important to analyze how the price depends on the country of origin. Before starting the analysis, it was necessary to prepare the data in a structured format. To do this, remove all columns, leaving only Country and Price. The price was in string format and I converted it to an integer. And also removed Mad in from all meanings, leaving only the name of the country. After I prepared myself the data in the required format, I began to analyze it. First, I calculated the amount of goods that came from the country, in order to understand where more goods are imported from. Then I calculated the average price of goods for the country.
