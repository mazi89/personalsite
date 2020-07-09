import os
import json
import collections
from selenium import webdriver
from selenium import common
# path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'main_feed/results_feed.txt')
# with open(path, 'r') as file:
#     lines = [file.readline() for line in range(7)] # get the first 7 links
#     file.close()
# print(lines)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

links = ['http://www.hiiraan.com/news4/2020/July/179009/jawar_mohammed_the_ethiopian_media_mogul_taking_on_abiy_ahmed.aspx', 
        'http://www.hiiraan.com/news4/2020/July/179008/emirates_sacks_more_pilots_blames_covid_19.aspx']
class navigate_main_url:
    def __init__(self, link):
        option = webdriver.firefox.options.Options()
        option.headless = True
        self.driver = webdriver.Firefox(options = option)
        self.driver.get(link)
        self.driver.implicitly_wait(5)
        self.site = self.driver.current_url
        methods = ['hiiraan',]
        domain = self.site.split('.')[1]
        self.method_to_call = methods.index(domain)
        self.article_data = []
        eval(f'self.{methods[self.method_to_call]}()')

    def hiiraan(self):
        content = self.driver.find_elements_by_xpath('//*[@id="desktopcontrol1_newsdesktop3_lblcontent"]/*')
        self.article_data = [{f'{x.tag_name}:{x.text}'} for x in content if x.text]
        self.driver.close()
        self.driver.quit()
        return self.article_data

articles = {}    
with open(os.path.join(BASE_DIR, 'newsreader/main_feed/articles/hiiraan.txt'), 'w+') as file:
    for link in links:
        # print(navigate_main_url(link).article_data)
        articles[link] = navigate_main_url(link).article_data
        file.write(f'{link}{articles[link]}\n\n')
file.close()

print('*'*100)

print('file has been written to')

print('*'*100)
