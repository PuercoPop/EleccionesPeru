# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen, urlencode, URLError
import constants
import settings

from celery import Celery


celery = Celery('tasks')

@celery.task()
def onpe_crawl(url, post_code):
    request = Request( url, urlencode {'elegido': post_code})
    try:
        response = urlopen(request)
    except URLError:
        #log error here
        raise open_crawl.retry()
    
    parse_response(response)

    return

if __name__ == '__main__':
    celery.worker_main()
