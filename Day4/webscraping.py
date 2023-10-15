import requests
from bs4 import BeautifulSoup

 
r = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(r.text, 'html.parser')

headings = []
scores = []
links = []

for i in soup.find_all('span', class_='titleline'):
    heading = i.find('a')
    if heading:
        headings.append(heading.get_text())
        links.append(heading['href'])

for i in soup.find_all('span', class_='score'):
    scores.append(i.get_text())

print("Headings: ", headings)
print("Scores: ", scores)
print("Links: ", links)