# Google-Play-reviews
## Extra Google Play reviews

### Essentials: <br>
   Python <br>
   Selenium Module in Python <br>
   Chrome Webdriver <br>
    
### Partial Output:<br>

### Execution Environment
   Python 3.7 <br>
   Windows 10


### Difficulties and Solutions


   * 1) <br>
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
      
      
 





