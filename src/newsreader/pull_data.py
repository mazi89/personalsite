import os
import json
import requests

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

response = requests.get(main_url)
with open('main_feed/feed.xml', 'ab') as file:
    file.write(response.content)

# response = requests.get(second_url)
# with open('second_feed/feed.xml', 'wb') as file:
#     file.write(response.content)