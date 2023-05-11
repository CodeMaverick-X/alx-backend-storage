#!/usr/bin/env python3
"""
contains function get_page
get html content and return it

"""
import requests
import redis
from functools import wraps
from datetime import timedelta
from typing import Callable


def get_page(url: str) -> str:
    """Get page"""
    r = redis.Redis()
    count = r.incr("count:"+url)
    page = r.get('cache_page')
    if not page:
        page = requests.get(url, headers={"User-Agent": "Requests"}).content
        res = r.setex('cache_page', 10, page)

    return page
