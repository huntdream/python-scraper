import requests
from bs4 import BeautifulSoup

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'https://www.5ewin.com'
}


def crawl_data(username):
    query = requests.get('https://www.5ewin.com/api/search/player/1/16?keywords=' + username, headers).json()
    url = query['data']['user']['list'][0]['domain']
    print(url)
    page = requests.get('https://www.5ewin.com/data/player/' + url, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    stats = soup.find('ul', class_='stat-data').find_all('span', class_='val')
    data = {
        'username': soup.find('h1', class_='username').contents[0].strip(),
        'rank': stats[0].string,
        'matches': stats[2].string,
        'rws': stats[3].string,
        'rating': stats[4].string,
        'score': stats[5].string
    }
    print(data)


if __name__ == '__main__':
    player = '天涯岂是无归意'
    crawl_data(player)
