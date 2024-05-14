'''
Resource used : 
https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a
https://www.thepythoncode.com/article/automated-browser-testing-with-edge-and-selenium-in-python
'''


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import pandas as pd

import time

def create_dataset(keyword: str, location: str, n_jobs: int) -> pd.DataFrame:
    '''
    Creates dataset by scraping data from glassdoor website
    
    Parameters:
    
    Returns:

    '''

    #Creating a dataframe to store the data
    jobs_df = pd.DataFrame(columns=['Company Name', 'Title', 'Rating', 'Location', 'Salary Est.', 'Description'])

    #Creating a webdriver object for MS Edge
    browser = webdriver.Edge('driver\msedgedriver.exe')

    url = 'https://www.glassdoor.co.in/Job'
    
    browser.get(url)
    time.sleep(5)
    browser.maximize_window()
    jobs = []

    #Populating the search texts
    browser.find_element_by_id('searchBar-jobTitle').send_keys(keyword)
    browser.find_element_by_id('searchBar-location').send_keys(location)
    browser.find_element_by_id('searchBar-location').send_keys(Keys.ENTER)
    # browser.find_element_by_xpath('//*[@id="UtilityNav"]/div/button').click()

    
    time.sleep(5)

create_dataset('data science', 'india', 1000).to_csv('Data/jobs_data.csv', index = False)