import os
import json
import collections
from selenium import webdriver
# path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'main_feed/results_feed.txt')
# with open(path, 'r') as file:
#     lines = [file.readline() for line in range(7)] # get the first 7 links
#     file.close()
# print(lines)
option = webdriver.firefox.options.Options()
option.headless = True
driver = webdriver.Firefox(options = option)
class navigate_main_url:
    def __init__(self, link):
        driver.get(link)
    

#desktopcontrol1_newsdesktop3_lblcontent
