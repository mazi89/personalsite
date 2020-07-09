import os
import json
import collections
from selenium import webdriver
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))

main_url = get_secret('url')
# second_url = get_secret('sec_url')
option = webdriver.firefox.options.Options()
option.headless = True
driver = webdriver.Firefox(options = option)
driver.get(main_url)
# driver.get("http://feeds.bbci.co.uk/news/world/rss.xml") ! not a legit XML site
# driver.get("https://www.buzzfeed.com/world.xml")

class Walk_through_XML:
    def __init__(self, driver):
        site_is_xml = 'xml' in driver.current_url
        if site_is_xml == False: raise Exception('XML Site not passed, please check URL')
        self.top_level_elem = driver.find_element_by_xpath('/*').tag_name
        if self.top_level_elem == ('html' or 'HTML'): raise Exception('XML Site not passed, please check URL')
        self.root_elem = driver.find_element_by_xpath('/*/child::*').tag_name
        self.parent_elems = []
        self.search_for_tags = ['date','title','link','desc']
        self.exclude = ['image', 'copyright', 'language']
################################################################################# 
# driver grabs root of outter xml element then 
# data is sanitized by creating a list of tag_names
# a dict with the count of each tag names is setup
# the dict is referenced to set the range of the inner loop for the xpath
    def get_elems(self):
        self.parents = driver.find_elements_by_xpath(f'//{self.root_elem}/*')
        count_list = [x.tag_name for x in self.parents] # O(n)
        count_dict = collections.Counter(count_list) # O(n)
        for parent in self.parents: # O(n)
            results = []
            with open(os.path.join(BASE_DIR, 'newsreader/main_feed/results_feed.txt'), 'w+') as file:
                if count_dict[parent.tag_name] > 1 and parent.tag_name not in self.exclude: # O(n)
                    for i in range(count_dict[parent.tag_name]+1): #O(4n^2)
                        ele = driver.find_elements_by_xpath(f'//{parent.tag_name}[{i}]/*') 
                        if ele:
                                results.append([{f'{child.tag_name}':f'{child.text}'} for child in ele]) #O(4n^3)
                                file.write(f'{results[-1]} \n')
                                file.close()
        print("file has been written to!")
        return         

print('*'*100)

Walk_through_XML(driver).get_elems()

print('*'*100)

driver.close()
driver.quit()


