from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
import requests 


def init_browser():
    # Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_mars_news():
    browser= init_browser()
    Mars_data= {}


    # Visit site to get Mars Latest News
    url='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    # Create a soup object to get the Latest Mars news
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_title= soup.find("div", class_='bottom_gradient').text
    mars_p= soup.find('div', class_= 'article_teaser_body').text
    browser.quite
    return mars_title, mars_p
# Scraping for a picture of Mars
def scrape_Mars_Space_Inages():

    #Visit the website
    image_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response= requests.get(image_url)
    # Creating a soup object
    soup= BeautifulSoup(response.text,'html.parser')
    image_mars= soup.find('img', class_='thumb')['src']
    #Scraping the image url
    Main_url='https://www.jpl.nasa.gov'
    #Combininng the site base url to the image url 
    Full_image= Main_url + image_mars
    Full_image
    return Full_image
# Scraping to get the lates wheater on Mars
def scrape_Mars_Weather():
    Mars_weather_url='https://twitter.com/marswxreport?lang=en'
    # Open the site
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(Mars_weather_url)
    weather_html = browser.html
    weather_soup = BeautifulSoup(weather_html, 'html.parser')
    mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
    mars_weather_tweet
    # Search for a specific tag on the page
    pattern = re.compile(r'sol')
    mars_weather = weather_soup.find('span', text=pattern).text
    mars_weather
    browser.quite
    return mars_weather

def scrape_Mars_Facts():

    #Open the site
    table_url='https://space-facts.com/mars/'
    #Find the table on the site 
    table=pd.read_html(table_url)
    #Select the right table 
    df=table[1]
    #Convert table to html
    Mars_html=df.to_html()
    #Strip the unwated lines 
    Mars_html=Mars_html.replace('\n','')
    #Save it as an Html
    df.to_html('Mars_table.html')

def scrape_Mars_Hemispheres():
    Mars_Hem_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    Mars_response= requests.get(Mars_Hem_url)
    Mars_pic=BeautifulSoup(Mars_response.text, "html.parser")
    M_results=Mars_pic.find_all('div', class_='item')
    Mars_results=[]
    for Mars in M_results :
    
        #Find the tile 
        Mars_title= Mars.find('div', class_='description').text
        #Find the images
        Mars_img= Mars.find('img', class_='thumb')['src']
        #Add base url to make full image
        Full_image= Mars_Hem_url + Mars_img
        Mars_results.append({'title': Mars_title, 'img_url': Full_image})
    return Mars_results



def info_all():
    mars_title, mars_p = scrape_mars_news(),
    Full_image= scrape_Mars_Space_Inages(),
    mars_weather= scrape_Mars_Weather(),
    Mars_table.html= scrape_Mars_Facts,
    Mars_results= scrape_Mars_Hemispheres()



    #Store the data
    Mars_data={
        "mars_title":mars_title,
        "mars_p": mars_p,
        "Full_image": Full_image,
        "mars_weather": mars_weather,
        "Mars_results": Mars_results

    }


    return Mars_data




    



