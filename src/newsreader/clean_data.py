from bs4 import BeautifulSoup as BS

with open('main_feed/feed.xml', 'rb') as file:
    soup = BS(file, "xml")

articles = []
items = soup.find_all('item')
for count,item in enumerate(items):
    articles.append({
                        'title':item.title.text.strip(), 
                        'link': item.link.text.strip(),
                        'desc': item.description.text.strip(), 
                        'date': item.pubDate.text.strip(),})
cleaned_data = [k['title'] for k in articles]
seen = set()
uniq = [x for x in cleaned_data if x not in seen and not seen.add(x)]   #set add() method returns None, need not
# print(articles)
print(cleaned_data)
