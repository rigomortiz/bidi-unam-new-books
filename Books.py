# coding=utf-8
import re
import json
import requests
from bs4 import BeautifulSoup


def get():
    page = requests.get("https://www.bidi.unam.mx/mdb/newadq.html")
    if page is None:
        return None
    soup = BeautifulSoup(page.text, 'html.parser')
    trs = soup.find(id='dtBasicExample').find('tbody').find_all('tr')
    books = []
    for tr in trs:
        tds = tr.find_all('td')
        link = tds[0].find('a').get('href')
        img = tds[0].find('img').get('src')
        data = tds[1].find('a').contents
        area = tds[2].find('small').prettify('latin-1').decode('utf8').replace('<small>\n ', '').replace('\n</small>', '')
        detail = []
        for c in data:
            try:
                if c.text != '':
                    detail.append(c.text[:-1])
            except Exception as e:
                text = re.sub(r'^\ *', "", c[:-1])
                if text != '':
                    detail.append(text.replace("\n\t  \t", "").replace("\n\t ", "").replace("\t", ""))

        book = {
            'link': link,
            'img': img,
            'data': detail,
            'area': area
        }
        books.append(book)

    return json.dumps(books, sort_keys=True, indent=4)


if __name__ == '__main__':
    print(get())
