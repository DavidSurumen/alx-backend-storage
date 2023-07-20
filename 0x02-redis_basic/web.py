#!/usr/bin/env python3
"""
Advanced Task Module -Implementing an expiring web cache and tracker
"""
import requests
import redis
from typing import Callable
import functools


redis_store = redis.Redis()


def track_requests(func: Callable) -> Callable:
    """decorator to track number of times a url has been accessed."""
    @functools.wraps(func)
    def wrapper(url):
        key = 'count:{}'.format(url)
        redis_store.incr(key)
        return func(url)
    return wrapper


def data_cacher(func: Callable) -> Callable:
    """decorator to cache reponse to url requests."""
    @functools.wraps(func)
    def wrapper(url):
        # cache server response
        if redis_store.get(url) is None:
            resp = func(url)
            redis_store.setex(url, 10, resp)

        return redis_store.get(url).decode('utf-8')
    return wrapper


@data_cacher
@track_requests
def get_page(url: str) -> str:
    """
    obtains HTML content of a particular URL and returns it.
    """
    res = requests.get(url)
    return res.text
