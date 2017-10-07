import requests
from bs4 import BeautifulSoup


def get_novels(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36'}
    page = requests.get(url, headers=header)
    souped = BeautifulSoup(page.content, 'html.parser')
    title = souped.find('h1').get_text()
    f.write(title + '\n')
    print(title)
    rawContent = souped.find('div', id='content').get_text()
    content = rawContent.split('找本站')[0].replace(u'\xa0', u' ').strip()
    # print(content)
    f.write('    '+content+'\n\n')
    nextChapter = 'http://www.biquge.cm' + souped.find(text='下一章').parent.get('href')
    if 'html' in nextChapter:
        print(nextChapter)
        get_novels(nextChapter)
    else:
        print('No New Chapter')
        f.close()


target = 'http://www.biquge.cm/8/8804/6609337.html'
f = open('1.txt', 'w+')
get_novels(target)
