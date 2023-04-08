import requests
from bs4 import BeautifulSoup
import time


def find_articles():
    url = "https://www.theverge.com/"
    req = requests.get(url)

    soup = BeautifulSoup(req.content, "html.parser")

    # print(soup.prettify())
    headlines = soup.find('ol', class_='relative')
    for h in headlines:
        article_names = h.find(
            'a', class_='group-hover:shadow-underline-franklin')
        author = h.find(
            'a', class_='text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8')
        pub_time = h.find('span', class_='text-gray-63 dark:text-gray-94')
        s = "https://www.theverge.com"
        alink = (s+article_names['href'])
        print(f"{article_names.text}")
        print(f"{author.text}")
        print(f"{pub_time.text}")
        print(f"{alink}")
        print("")


if __name__ == '__main__':
    while True:
        find_articles()
        time_wait = 24
        time.sleep(time_wait*3600)
