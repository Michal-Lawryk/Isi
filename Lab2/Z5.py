from bs4 import BeautifulSoup

with open('index.html') as fp:
    soup = BeautifulSoup(fp, features="lxml")
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    print(links)
