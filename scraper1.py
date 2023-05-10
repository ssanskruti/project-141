from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

star_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(star_url)
time.sleep(10)

headers=["V Mag","Proper name","Bayer designation","Distance","Spectral","Mass","Radius","Luminosity"]
stars_data=[]


def scrape():
        print("scraping_data")
        soup=BeautifulSoup(browser.page_source,"html.parser")
       
        table_body=soup.find("tbody")
        
        rows=table_body.find_all("tr")
        for row in rows:
            cols=row.find_all('td')
            cols=(x.text.strip() for x in cols)
       
        stars_data.append(cols)
        
    

scrape()
star_df=pd.DataFrame(stars_data,columns=headers)
star_df.to_csv("scraped_data.csv",index=True,index_label="id")
