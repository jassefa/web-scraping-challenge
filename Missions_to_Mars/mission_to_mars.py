#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Module used to connect Python with MongoDb
import pymongo
import time 
# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# https://mars.nasa.gov/news/
nasa_news = 'https://mars.nasa.gov/news/'
browser.visit(nasa_news)


# In[4]:


html = browser.html
soup = bs(html, 'html.parser')


# In[5]:


# find title
title = soup.find(class_="slide").find(class_="content_title").text
title


# In[6]:


par = soup.find(class_="slide").find(class_="article_teaser_body")
par


# In[7]:


# www.jpl.nasa.gov/spaceimages/?search=&category=Mars
nasa_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(nasa_image)


# In[8]:


html = browser.html
soup = bs(html, 'html.parser')


# In[9]:


image = soup.find(id="full_image")["data-fancybox-href"]
base_nasa = "https://www.jpl.nasa.gov"
base_nasa_image = base_nasa + image
base_nasa_image


# In[29]:


# https://twitter.com/marswxreport?lang=en
twitter_w = 'https://twitter.com/marswxreport?lang=en'
browser.visit(twitter_w)

time.sleep(5)


# In[30]:


html = browser.html
soup = bs(html, 'html.parser')


# In[34]:


#t_weather = soup.find_all(class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
soup


# In[44]:


t_weather = soup.find_all("span")
t_weather


# In[47]:


for i in t_weather:
    if "InSight sol" in i.text:
        print(i.text)
        mars_t_weather = i.text
        break
       


# In[48]:


mars_t_weather


# In[ ]:


# https://space-facts.com/mars/
mars_facts_url = 'https://space-facts.com/mars/'
table = pd.read_html(mars_facts_url)
table[0]


# In[ ]:


df = table[0]
df.columns = ["Facts", "Value"]
df.set_index(["Facts"])
df


# In[ ]:


facts_html = df.to_html()
facts_html = facts_html.replace("\n","")
facts_html


# In[51]:


#https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
mars_str = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
short_url="https://astrogeology.usgs.gov"
browser.visit(mars_str)

time.sleep(5)


# In[52]:


html = browser.html
soup = bs(html, 'html.parser')


# In[53]:


m_images = soup.find_all("div", class_="item")
titles=[]
hemisphere_img_urls=[]


# In[59]:


for i in m_images:
    title = i.find('h3').text
    url = i.find('a')['href']
    hem_img_url= short_url+url
    hemisphere_img_urls.append({"title":title, "hem_img_url":hem_img_url})
    print(hem_img_url)
hemisphere_img_urls

