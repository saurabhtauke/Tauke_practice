# code to extract titles of articels from website
# uses selenium to navigate the website
# class is called "js-article-title"
# uses beautiful soup to extract the title
# uses pandas to write the data to a csv file


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_titles(url):
    # create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # go to the page we want to scrape
    driver.get(url)

    # wait for the page to load
    time.sleep(2)

    # create a new BeautifulSoup object
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # find all the articles
    articles = soup.find_all( class_='js-article-title') # biobhysical journal
    articles = soup.find_all( class_='u-link-inherit') # nature physics 

    print(articles)

    # create a list to store the titles
    titles = []

    # loop through the articles and extract the titles
    for article in articles:
        title = article.text
        titles.append(title)

    # close the browser
    driver.close()

    # return the titles
    return titles


def write_titles(titles, filename):
    # create a dataframe with the titles
    df = pd.DataFrame(titles)

    # write the dataframe to a csv file
    df.to_csv(filename, index=False,mode='a')


journal_name = 'nature_physics'

# journal_url = 'https://www.sciencedirect.com/journal/biophysical-journal'
journal_url = 'https://www.nature.com/nphys'

'''####$^$&% make a list of common journals and their urls for archives'''

volume = 16
volume_id = 'volumes'

# issue = 12
issue_id = 'issues'

num_issues = 12

for issue in range(1, num_issues+1):

    gen_string = journal_url+'/'+volume_id+'/'+str(volume)+'/'+issue_id+'/'+str(issue)
    print(gen_string)

    # get the titles
    titles = get_titles(gen_string)

    # write the titles to a csv file
    file_name= 'titles'+'_'+ journal_name +'_'+'volume'+str(volume)+'_'+'.csv'
    write_titles(titles, file_name)

