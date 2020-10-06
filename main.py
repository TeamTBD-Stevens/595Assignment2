from requests_html import HTMLSession
import pandas as pd

name, purpose = [], []


def get_info():
    session = HTMLSession()
    url = 'http://3.95.249.159:8000/random_company'
    content = session.get(url)
    i = 1
    while True:
        sector = 'body > ol > li:nth-child(' + str(i) + ')'
        results = content.html.find(sector)
        text = results[0].text.split()
        if text[0] == 'Name:':
            name.append(' '.join(text[1:]))
        if text[0] == 'Purpose:':
            purpose.append(' '.join(text[1:]))
            return 0
        i = i + 1


for times in range(50):
    get_info()

collect_info = pd.DataFrame({'Name': name, 'Purpose': purpose})
print(collect_info)


