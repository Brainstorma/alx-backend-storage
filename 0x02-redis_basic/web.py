import requests
from functools import wraps
import redis

redis = redis.Redis()

def count_url_access(url):
    key = f'count:{url}'
    redis.incr(key)
    redis.expire(key, 10)

def cache_url(url):
    key = f'cache:{url}'
    if redis.exists(key):
        return redis.get(key)

    html = requests.get(url).text
    redis.setex(key, 10, html)
    return html

def get_page(url):
    count_url_access(url)
    return cache_url(url)

@app.route('/')
def index():
    return get_page('http://slowwly.robertomurray.co.uk')

@app.route('/count')
def count():
    url = 'http://slowwly.robertomurray.co.uk'
    count = int(redis.get(f'count:{url}'))
    return str(count)
