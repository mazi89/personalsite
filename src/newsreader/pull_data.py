import os
import json
from selenium import webdriver
  

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
# element = driver.find_elements_by_xpath("/rss/channel/item")
# for el in element:
#     print("Title: \t\t",el.find_element_by_tag_name('title').text)
#     print("Description: \t\t",el.find_element_by_tag_name('description').text)
#     print("Link: \t\t",el.find_element_by_tag_name('link').text)
#     print("Date: \t\t",el.find_element_by_tag_name('pubDate').text)
#     print()
class Walk_through_XML:
    def __init__(self, driver):
        site_is_xml = 'xml' in driver.current_url
        if site_is_xml == False: raise Exception('XML Site not passed, please check URL')
        self.top_level_elem = driver.find_element_by_xpath('/*').tag_name
        self.root_elem = driver.find_element_by_xpath('/*/child::*').tag_name
        self.parent_elems = []
        self.child_elems = []
        self.articles= []
        self.search_for_tags = ['date','title','link','desc']
        self.exclude = ['image', 'copyright']
        
    def get_parent_elems(self):
        elem = self.root_elem
        self.parents = parents = driver.find_elements_by_xpath(f'//{elem}/*')
        count_list = [x.tag_name for x in parents]
        set_ = set(count_list)
        count_dict = {}
        for x in count_list:
            if x in count_dict:
                count_dict[x] += 1
            else:
                count_dict[x] = 1
        ele = driver.find_elements_by_xpath(f'//{parents[8].tag_name}[1]/*')
        print_ = [[x.tag_name, x.text] for x in ele]
        print(count_dict)
        # for parent in parents:
            # if parent.tag_name not in self.exclude:
                # self.child_elems = children = driver.find_elements_by_xpath(f'//{parent.tag_name}/*')
                # print(parent.tag_name)
                # break
                # seen = []
                # if len(children):
                    # for child in children:
                        # if child.tag_name not in self.exclude:
                        #     descendants = driver.find_elements_by_xpath(f'//{child.tag_name}/*')
                        #     if len(descendants):
                        #         print("Inception")
                        # if (child.tag_name in self.search_for_tags):
                        #     print(parent.tag_name)
                        #     break
                            # print(driver.find_elements_by_xpath(f'//{child.tag_name}/*'))
                        # break
                            # articles.append({"title":child.})
        pass
        # return driver.find_element_by_xpath('/*').tag_name
        
    def get_child_elems(self):

        return driver.find_element_by_xpath('/*/child::*').tag_name

    def convert_single_elem_list(self, elem_list):
        if len(elem_list) < 2:
            for elem in elem_list:
                return elem
        return None
print('*'*100)
# child = driver.find_elements_by_xpath('/*/child::*/*')
# [print(x.tag_name) for x in child]
Walk_through_XML(driver).get_parent_elems()
# element = driver.find_element_by_xpath('//item')
# print(driver.find_elements_by_xpath(f'//{element.tag_name}/child::*')[2].tag_name)
print('*'*100)
# root_rss_elements = driver.find_elements_by_xpath('/rss/child::*')
# child_elem = Walk_through_XML().convert_single_elem_list(root_rss_elements)
# child_top_element = driver.find_elements_by_xpath(f'//{child_elem.tag_name}/child::*')
# child_elem = Walk_through_XML().convert_single_elem_list(child_top_element)
# print(child_top_element)
# parent = driver.find_elements_by_xpath(f'//{.tag_name}/parent::*') 
# print()
driver.quit()
