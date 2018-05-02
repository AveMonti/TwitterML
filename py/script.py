#script
import config
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twitt import Twitt
import request

#Exception
from selenium.common.exceptions import StaleElementReferenceException
#VAR
driver = webdriver.Chrome("/Users/mateuszchojnacki/Applications/chromedriver")
dictionaryValue = {}

def login_twitter(username,password):
    driver.get("https://twitter.com/login")

    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    username_field.send_keys(username)
    driver.implicitly_wait(1)

    password_field.send_keys(password)
    driver.implicitly_wait(1)

    driver.find_element_by_class_name("EdgeButtom--medium").click()
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "li.trend-item.js-trend-item.context-trend-item")))
    finally:
        getTredHash()

def openHashtag(hashtag):
    inputElement = driver.find_element_by_id("search-query")
    inputElement.send_keys(hashtag)
    driver.find_element_by_class_name("nav-search").click()
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "li.AdaptiveFiltersBar-item.u-borderUserColor")))
    finally:
        theLatestHashtag = driver.find_elements_by_css_selector("li.AdaptiveFiltersBar-item.u-borderUserColor")
        theLatestHashtag[1].click()
        time.sleep(2)
        getValueFromTweet()

def getTredHash():
    trendHashTag = driver.find_elements_by_css_selector("li.trend-item.js-trend-item.context-trend-item")
    trendHashTag[0].click()
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "li.AdaptiveFiltersBar-item.u-borderUserColor")))
    finally:
        theLatestHashtag = driver.find_elements_by_css_selector("li.AdaptiveFiltersBar-item.u-borderUserColor")
        theLatestHashtag[1].click()
        getValueFromTweet()
        time.sleep(2)

def getValueFromTweet():
    while True:
        twitts = driver.find_elements_by_css_selector("div.js-original-tweet")
        for twitt in twitts:
            try:
                idValue = twitt.get_attribute("data-tweet-id")
                pathValue = twitt.get_attribute("data-permalink-path")
                if idValue not in dictionaryValue: #if key exist in dictionary
                    print(idValue + "\n" + pathValue)
                    driverForTweet = webdriver.Chrome("/Users/mateuszchojnacki/Applications/chromedriver")
                    driverForTweet.get("https://twitter.com/" + pathValue)
                    time.sleep(1)
                    twittValue = driverForTweet.find_element_by_css_selector("p.TweetTextSize.TweetTextSize--jumbo.js-tweet-text.tweet-text").text
                    print("\n \n"+twittValue+"\n")
                    driverForTweet.close()
                    dictionaryValue.setdefault(idValue, twittValue)
                    #ToDo send value to NodeJS server by Post
                    request.addTwitts(idValue,twittValue)
            except StaleElementReferenceException:
                break
        print(dictionaryValue)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(9)




if __name__ == "__main__":
    username = config.DATACOUP_USERNAME
    password = config.DATACOUP_PASSWORD
    login_twitter(username,password)
    getTredHash()
