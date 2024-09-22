
from bs4 import BeautifulSoup
import os
import pandas as pd

d = { 'title': [], 'price': [], 'links': []}

# Corrected the folder name from "date" to "data"
for file in os.listdir("data"):
    try:
        with open(f"data/{file}", encoding="utf-8") as f:  # Use 'utf-8' to handle encoding properly
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")
        
        t = soup.find("h2")
        title = t.get_text()
        
        
        l = t.find("a")
        link = "https://amazon.com/" + l['href']
        
        p = soup.find("span", attrs={"class": "a-offscreen"})
        price = p.get_text()
        d['title'].append(title)
        d['price'].append(price)
        d['links'].append(link)
        
    except Exception as e:
        print(e)    

df = pd.DataFrame(data=d)
df.to_csv("data.csv")