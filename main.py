import requests
from bs4 import BeautifulSoup
url ='https://codewithharry.com'
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
# Print all paragraphs
paras = soup.find_all('p')
# print(paras)

#Print all anchors
anchors = soup.find_all('a')
# print(anchors)

#Print first paragraph
para = soup.find('p')['class']
# print(para)

#Print all p elemtns with class lead
#print(soup.find_all('p',class_='text-sm'))

#Print all links on the page
all_links=set()
for link in anchors:
    if (link.get('href')!='/'):
        link="https://codewithharry.com"+link.get('href')
        all_links.add(link)
        print(link)