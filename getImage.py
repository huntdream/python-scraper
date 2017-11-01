import requests
from bs4 import BeautifulSoup

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36',
    'Referer': ''
}


def get_urls(url):
    """获取首页图片链接"""

    urls = []
    page = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
    links = page.select('ul#pins li span a')
    for link in links:
        urls.append(link.get('href'))
    get_pages(urls)


def get_pages(urls):
    """获取图集图片数量"""

    for url in urls:
        page = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
        image_counts = page.select('div.pagenavi span')[-2].get_text()
        get_images(url, int(image_counts))


def get_images(url, counts):
    """获取单张图片链接"""

    for x in range(1, counts + 1):
        target = url + '/' + str(x)
        print(url)
        page = BeautifulSoup(requests.get(target, headers=headers).content, 'html.parser')
        image_url = page.select('div.main-image img')[0].get('src')
        save_pic(image_url)


def save_pic(image_url):
    """保存图片至本地"""

    try:
        img = requests.get(image_url, headers=headers, timeout=10)
        imgname = image_url.split('/')[-1]
        with open('./image/' + imgname, 'wb+') as f:
            f.write(img.content)
            print(imgname)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_urls(site_url)
