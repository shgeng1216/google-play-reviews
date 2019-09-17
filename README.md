# Google-Play-reviews
## Extra Google Play reviews

### Essentials: <br>
   Python <br>
   Selenium Module in Python <br>
   Chrome Webdriver <br>
    
### Partial Output:<br>
   ![](https://github.com/shgeng1216/google-play-reviews/blob/master/output.png)
   
   
### Main Idea: <br>
#### 1. Get site codes
``` pyhton 
while 1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Simulate mouse slide to the end of page
    
    try:
        time.sleep(2)
        # Simulate to click "SHOW MORE" button 
        driver.find_element_by_xpath("//*[contains(@class,'U26fgb O0WRkf oG5Srb C0oVfc n9lfJ')]").click() 
    except:
        time.sleep(1)
        flag=flag+1
        print("TRYING scroll times:",flag)  # Counting scrolling times 
        
        # IF simulated more than 5 times sliding to the end of page and click the "SHOW MORE" button failed, we will try to use another Class name to simulate click actions.
        if flag >= 5:    
            try:
                time.sleep(1.5)
                driver.find_element_by_xpath("//*[contains(@class,'U26fgb O0WRkf oG5Srb C0oVfc n9lfJ M9Bg4d')]").click()
                secondloop=secondloop+1
                print("2st click link",secondloop)
            except:
                time.sleep(1)
                driver.execute_script("window.scrollTo(2, 30000);")
        # If scrolled up and down on the same page more than 20 times, it means 1). there is no more reviews 2) wrong with our code, which means our simualtion of mouse clicking is failture. We need to break out the loop.                    
        if flag >=20:  
            break
        page=page+1
        print("info page:", page)
        
        # At this time, I just tried to crawl first 10 pages' data. If you want to get whole site's information, you can just delete this IF STATEMENT. Only use flag to control the whole loop. 
        if page >=10:
            break
    else:
        flag=0
```

#### 2. Extract valuable information 
```
# Extracting info from their XPATHs. 
for ii in range(1,len(reviews)):
        fullreview= selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div'+str([ii])+'/div/div[2]/div[2]/span[2]/text()')
        if len(fullreview)==0:
            fullreview=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div'+str([ii])+'/div/div[2]/div[2]/span[1]/text()')

        username= selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div'+str([ii])+'/div/div[2]/div[1]/div[1]/span/text()')
        date=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div'+str([ii])+'/div/div[2]/div[1]/div[1]/div/span[2]//text()')
        rating=re.findall(r'aria-label="(.+?)"',str(etree.tostring(selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div'+str([ii])+'/div/div[2]/div[1]/div[1]/div/span[1]/div/div')[0], method='html')))
```


### Execution Environment
   Python 3.7 <br>
   Windows 10


### Difficulties and Solutions


   * 1. <br>
   **D**: Google sites are using JavaScript Render, which means content that we need is not present in the source code of the page. Therefore, BeatuifulSoup and RE libraries can not be our priorities.<br>
   **S**: Asynchronous crawling. using Selenium to crawl data.<br>
   * 2) <br>
   **D**: To view more reviews on Google Play webpage, people need to slide their mouse to the end of the pages. There is no direct button leading to the next page. No changes in URL.<br>
   **S**: Use Selenium to open a web browser, navigate to a page, and imitate human activitiess. <br>
   * 3) <br>
   **D**: When reviews are too long, they will be folded to a 'shorter version' with a apostrophe as ending. People need to click the "Full Reviews" button to load full reviews. "Full Reviews" and "Shorter version reviews" were stored in different "div" tags. However,short reviews had no info stored in "Full Reviews" div tag. In other words, if only extracted information from "Full Reviews" tag, it only get long reviews. For example, we have 5 reviews. 1st and 4th are long reviews and are folded for webpage displaying. If we extract reviews according to tag1(shorter version div), we can get 5 reviews, but the first and forth ones are partials displayed. If we extract info according to tag2(full reviews div), we can only get 2 reviews. The forth one will take place of the second review, which will mismatch with usernames, dates and ratings.<br> 
   **S**: Setting up a IF STATEMENT. If it was a empty list, extract data from the 'shorter edition tag', otherwise, pull out the info from 'full review' tag. <br>
   * 4) <br>
   **D**: When used 'Class Name' to extract info, it hard to match other info with "Full reviews", since they have been stored as lists and empty list has been replaced by next avaiable 'full review' list.<br>
   **S**: Rewritting codes. Extracting data from XPATHs rather than tag names. Finding the laws of locating every single item. I finally found that in a XPATH, div[1] means the first reviews, div[2] for the second reviews, Therefore, div[i] can represent any items. Futher explaination by using upper example, 1st and 4th are long reviews and 2nd, 3rd, 5th are short reviews. Ertracting info by using 'Full Reviews' XPATH, div[2] will give back a empty list, which is easy for us to identify and reassign for another value. <br>
   * 5) <br>
   **D**: Since it's hard to mark and identify empty lists, same issue will happen when I set up loops to extract info and put them in a cvs file.<br>
   **S**: Solved by using XPATHs and index to extract info.  
   * 6) <br>
   **D**: When using Selenium to mimic human activities of scrolling down mouse to the end of page several times, it appeared a "SHOW MORE" button. People must click this button to load more reviews. The class name of the first button is different from laters'. 
   **S**: Rewritting code. Locating XPATHs of these buttons and seeting IF STATEMENT to choose the right class name. Use Class name to extract info. At the meantime, simulate a smoothly upward mouse slide in order to load reviews successfuly.
   
### Future works 
   1) Try to use APIs to get access data. I didn't get any idea at the first place. If I had more time, I would love to give it a try.
   2) Use more concise statments.
      
 





