import requests
from bs4 import BeautifulSoup
import time
from csv import writer


def find_articles():
    url = "https://www.theverge.com/"
    req = requests.get(url)

    soup = BeautifulSoup(req.content, "html.parser")

    # print(soup.prettify())
    headlines = soup.find('ol', class_='relative')
    with open("articles.csv", 'w', encoding='utf8', newline="") as f:
        thewriter = writer(f)
        header = ['id', 'URL', 'headline', 'author', 'date']
        thewriter.writerow(header)
        for index, h in enumerate(headlines):
            article_names = h.find(
                'a', class_='group-hover:shadow-underline-franklin')
            author = h.find(
                'a', class_='text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8')
            pub_time = h.find('span', class_='text-gray-63 dark:text-gray-94')
            s = "https://www.theverge.com"
            alink = (s+article_names['href'])
            f.write(f"{index}")
            f.write(f"{alink}")
            f.write(f"{article_names.text}")
            f.write(f"{author.text}")
            f.write(f"{pub_time.text}")
            f.write(f"{alink}")
            article = [index, alink, article_names.text,
                       author.text, pub_time.text]
            print(article)
            thewriter.writerow(article)


# if __name__=='__main__':
#   while True:
find_articles()
# time_wait=24
# time.sleep(time_wait*3600)
