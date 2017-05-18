import urllib2
import urlparse
import re

def download(url,user_agent='wswp',proxy=None,num_retries=2):
    print 'Downloading:',url
    headers = {'User-agent':user_agent}
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

def link_crawler(seed_url,link_regex):
    crawl_queue = [seed_url]
    seen =set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html=download(url)
        for link in get_links(html):
            if re.match(link_regex,link):
                link = urlparse.urljoin(seed_url,link)
                if link not in seen:
                    seen.add(link)
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

