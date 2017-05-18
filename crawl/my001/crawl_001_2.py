import urllib2
import urlparse
import re

def download(url,user_agent='wswp',proxy=None,num_retries=2):
    print 'Downloading:',url
    if user_agent == 'wswp':
        headers = {'User-agent':user_agent}
    else:
        headers = user_agent
    request = urllib2.Request(url,headers=headers)
    opener =urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print 'Download error:',e.reason
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500<=e.code<600:
                html =download(url,user_agent,proxy,num_retries-1)
    return html

def link_crawler(seed_url,link_regex,headers=None,max_depth=2,delay=1):
    crawl_queue = [seed_url]
    seen ={}
    while crawl_queue:
        url = crawl_queue.pop()
        ts = Throttle(delay)
        ts.wait(url)
        if headers ==None:
            html=download(url)
        else:
            html=download(url,headers)
        depth = seen[url]
        if depth != max_depath:
            for link in get_links(html):
                if re.match(link_regex,link):
                    link = urlparse.urljoin(seed_url,link)
                    if link not in seen:
                        seen[link]=depth+1 
                        crawl_queue.append(link)

def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',
            re.IGNORECASE)
    return webpage_regex.findall(html)


class Throttle:
    def __init__(self,delay):
        self.delay=delay
        self.domains=()

    def wait(self,url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

if __name__ == "__main__":
    url="http://www.mafengwo.cn"
    regex=".*"
    headers= {
        'host': "www.mafengwo.cn",
        'connection': "keep-alive",
        'cache-control': "no-cache",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'accept-language': "zh-CN,en-US;q=0.8,en;q=0.6"
        }
    link_crawler(url,regex,headers)

