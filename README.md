# Google-Play-reviews
## Extra Google Play reviews

### Essentials:<br>
    Python <br>
    Selenium Module in Python <br>
    Chrome Webdriver <br>
    
### Partial Output:<br>

### Execution Environment
   Python 3.7
   Windows 10


### Notes
   a. Difficulties
      1) Google sites are using JavaScript Render, which means content that we need is not present in the source code of the page. Therefore, BeatuifulSoup and RE libraries can not be our priorities.
      2) To view more reviews on Google Play webpage, people need to slide their mouse to the end of the pages. There is no direct button leading to the next page. No changes in URL.
      3) When reviews are too long, they will be fold to a shorter edition with a apostrophe as ending. People need to click the "Full Reviews" button to load full reviews. "Full Reviews" and "Shorter Edition reviews" were stored in different "div" tags. However,short reviews had no info stored in "Full Reviews" div tag. In other words, if only extracted information from "Full Reviews" tag, it can only get long reviews. For example, we have 5 reviews. 1st and 4th are long reviews. If we extract reviews according to tag1(shorter editon div), we can get 5 reviews, but the first and forth ones are partials reviews. If we extract info according to tag2(full reviews div), we can only get 2 reviews. The forth one will take place of the second review, which will mismatch with usernames, dates and ratings.
      4)                                                                                                                                            
      
      I only extracted information in the "Full Reviews" tag,                                                             
      
       
      
      
      
      
      
      
      
      
      When tracking the loading information of webpages, I found several XHR files get updated when more reviews came up on the screen. New Request URLs and 





