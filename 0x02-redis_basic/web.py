#!/usr/bin/env python3
"""
Title: Implementing an expiring web cache and tracker
Description: implement a get_page function
        (prototype: def get_page(url: str) -> str:).
        The core of the function is very simple.
        It uses the requests module to obtain the HTML
        content of a particular URL and returns it.
"""
import redis
import requests
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """ method that counts the frequency of url access """

    @wraps(method)
    def wrapper(url):
        """ wrap method """

        key = "cached:" + url
        data = store.get(key)
        if data:
            return data.decode("utf-8")

        # counting
        c_key = "count:" + url
        html = method(url)

        # storing process
        store.incr(c_key)
        store.set(key, html)
        store.expire(key, 10)

        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """

    content = requests.get(url)
    return content.text
