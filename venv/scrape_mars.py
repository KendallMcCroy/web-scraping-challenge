from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

# NASA Mars
def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
  
    news_title, news_p = mars_news(browser)

    mars_dict = {
        "news_title":news_title,
        "news_p":news_p,
        "img_url":img_url,
        "df":df,
        "hemisphere_images":hemisphere_image_urls
    }
        # "news-title": news_title, 
        # "news_p": news_p,
        # "featured_image": featured_image(browser),
        # "facts": mars_facts()
        # # "hemispheres": hemispheres(browser), 
        # # "last_modified": dt.datetime.now()
    

    browser.quit()
    return data 
    
    # url = "https://redplanetscience.com/"
    # browser.visit(url)

    # html = browser.html
    # soup = BeautifulSoup(html, "html.parser")
 
    # # response = requests.get(url)
    # # soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    # #Quit Brower.html
    # browser.quit()
    # return mars_data 