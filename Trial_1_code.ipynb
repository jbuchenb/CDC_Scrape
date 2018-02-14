from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# navigating to main page where material, and linked material needs to be scraped
driver = webdriver.Firefox()
url = 'https://www.cdc.gov/zika/whats-new.html'
driver.get(url)

driver.switch_to_default_content()

# --instructing driver to find the links on the page by partial text(cdc.gov) 
#or by class attribute(feed-item-title...) both are common to all links on the page

# --attempting this as my way of creating a loop that opens each link, 
# and scraps the body of the entire page before returning to the next page 
# and continuing

link_loop = driver.find_element_by_partial_link_text('cdc.gov').click() 
# could use either method
links= driver.find_elements_by_xpath('//a[@class="feed-itemtitle tp-link-policy"]')

#using links or link_loop as qualifier of the length for which 
#the loop should run. 
num_links = len[links]  #getting error on this link saying not scriptable
for i in range(num_links):
 # scraping body of text of the urls that have been clicked    
    body=driver.find_element_by_tag_name('body').get_attribute('innerText')
    print(body.text)

driver.close()
