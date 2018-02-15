from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import re
import linkGrabber

###creating csv file to write data to
with open('cdc_link.csv', 'w') as f:
    f.write("page_body")

    # grabs all links on webpage
links = linkGrabber.Links('https://www.cdc.gov/zika/whats-new.html')
pretty_links= links.find(pretty=True)
#print(gb)



driver = webdriver.Firefox()
driver.get('https://www.cdc.gov/zika/whats-new.html')

### Trying to grab 'body' of each associated linked webpage
page_body = driver.find_element_by_css_selector('body')
time.sleep(5)



###attempt at loop to grab body of each link in 'links' variable list
with open('cdc_link.csv', 'a') as f:
    for i in links:
        f.write(page_body(pretty=True))
    
driver.close

#page_body.send_keys(Keys.CONTROL +'a')
