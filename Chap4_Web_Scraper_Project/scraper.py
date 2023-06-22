import requests
from bs4 import BeautifulSoup

url = "https://pixelford.com"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
blogs = soup.find_all('article', class_="post-155")

for blog in blogs:
    title = blog.find('h2', class_="entry-title").get_text()
    
    text_tag = blog.find('div', class_="entry-content").get_text()
    print(f'{title} - {text_tag}')



#

