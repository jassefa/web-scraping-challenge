# Module used to connect Python with MongoDb
import pymongo
import time 
# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs


def scrape():
    browser = Browser("chrome", executable_path="C:/Users/j68im/Desktop/web-scraping-challenge/Missions_to_Mars/chromedriver", headless=False)
    
    # https://mars.nasa.gov/news/
    nasa_news = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_news)
    html = browser.html
    soup = bs(html, 'html.parser')
    # find title
    news_title = soup.find(class_="slide").find(class_="content_title").text
    news_title
    # find paragragh
    
    par = soup.find('div', class_='article_teaser_body').text
    par
    # www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    nasa_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(nasa_image)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    image = soup.find(id="full_image")["data-fancybox-href"]
    base_nasa = "https://www.jpl.nasa.gov"
    base_nasa_image = base_nasa + image
    base_nasa_image
    # https://twitter.com/marswxreport?lang=en
    twitter_w = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_w)
    time.sleep(5)
    html = browser.html
    soup = bs(html, 'html.parser')
    t_weather = soup.find_all("span")
    t_weather
    for i in t_weather:
        if "InSight sol" in i.text:
            print(i.text)
            mars_t_weather = i.text
            break
    mars_t_weather
    # https://space-facts.com/mars/
    mars_facts_url = 'https://space-facts.com/mars/'
    table = pd.read_html(mars_facts_url)
    table[0]
    df = table[0]
    df.columns = ["Facts", "Value"]
    df.set_index(["Facts"])
    df
    facts_html = df.to_html()
    facts_html = facts_html.replace("\n","")
    facts_html
    #https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    mars_str = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    short_url="https://astrogeology.usgs.gov"
    browser.visit(mars_str)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    m_images = soup.find_all("div", class_="item")
    titles=[]
    hemisphere_img_urls=[]
    for i in m_images:
        title = i.find('h3').text
        url = i.find('a')['href']
        hem_img_url= short_url+url
        hemisphere_img_urls.append({"title":title, "hem_img_url":hem_img_url})
        print(hem_img_url)
    hemisphere_img_urls
    web_scrape_dict = {"title":news_title, 
                        "par":par,
                        "base_nasa_image":base_nasa_image,
                        "mars_t_weather":mars_t_weather,
                        "Facts":facts_html,
                        "images": hemisphere_img_urls,
                        "image_title":titles                      
                        }
    browser.quit() 
    return web_scrape_dict

if __name__ == "__main__":
     # If running as script, print scraped data
    print(scrape()) 