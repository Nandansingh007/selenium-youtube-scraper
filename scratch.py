#to get the data from the website
import requests
#work with htm file not javasript file
from bs4 import BeautifulSoup




YOUTUBE_TRENDING_URL='https://www.youtube.com/feed/trending'

response = requests.get(YOUTUBE_TRENDING_URL)

#checking whether the response from the website yes/No
print('Status Code', response.status_code)