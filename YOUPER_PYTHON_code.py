
from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
import requests
import json
from lxml import etree
import csv


url = "https://play.google.com/store/apps/details?id=br.com.youper&hl=en_US&showAllReviews=true"
driver = webdriver.Chrome()
driver.get(url)

flag=0
page=0
secondloop=0
while 1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    try:
      
        time.sleep(2)
        driver.find_element_by_xpath("//*[contains(@class,'U26fgb O0WRkf oG5Srb C0oVfc n9lfJ')]").click() 
    except:
        time.sleep(1)
        flag=flag+1
        print("TRYING scroll times:",flag)
        if flag >= 5:
            try:

                time.sleep(1.5)
                driver.find_element_by_xpath("//*[contains(@class,'U26fgb O0WRkf oG5Srb C0oVfc n9lfJ M9Bg4d')]").click()
                secondloop=secondloop+1
                print("2st click link",secondloop)
            except:
                time.sleep(1)
                driver.execute_script("window.scrollTo(2, 30000);")
                               
        if flag >=20:  
            break
        page=page+1
        print("info page:", page)
        if page >=20:
            break
    else:
        flag=0


reviews=driver.find_elements_by_xpath("//*[@jsname='fk8dgd']//div[@class='d15Mdf bAhLNe']")
print("There are "+str(len(reviews))+" reviews avaliable")
print("Writing the data...")

selector= etree.HTML(driver.page_source)
fullreviews=[]
usernames=[]
dates=[]
ratings=[]

for ii in range(1,len(reviews)):
        fullreview= selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div'+str([ii])+'/div/div[2]/div[2]/span[2]/text()')
        if len(fullreview)==0:
            fullreview=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div'+str([ii])+'/div/div[2]/div[2]/span[1]/text()')


        username= selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div'+str([ii])+'/div/div[2]/div[1]/div[1]/span/text()')
        date=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div'+str([ii])+'/div/div[2]/div[1]/div[1]/div/span[2]//text()')
        rating=re.findall(r'aria-label="(.+?)"',str(etree.tostring(selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div'+str([ii])+'/div/div[2]/div[1]/div[1]/div/span[1]/div/div')[0], method='html')))
        

        fullreviews.append(fullreview)
        usernames.append(username)
        dates.append(date)
        ratings.append(rating)


with open('output.csv','w',encoding='utf-8', newline ='') as f:
	writer = csv.writer(f)
	writer.writerows(zip(usernames,dates,ratings,fullreviews))

driver.quit()
