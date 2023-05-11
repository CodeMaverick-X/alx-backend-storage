#!/usr/bin/env python3
"""
contains a cache class
"""
import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorate stored method to count no of calls"""
    @wraps(method)
    def wrapped(*args, **kwargs) -> Any:
        """A wrapper function"""
        if "Cache.{}".format(method.__name__) == method.__qualname__:
            self = args[0]
            key = method.__qualname__
            if not self._redis.get(key):
                self._redis.set(key, 1)
            else:
                self._redis.incr(key)
        return method(*args, **kwargs)
    return wrapped


class Cache:
    """class that creates a cache mech"""
    def __init__(self):
        """instatiate"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store value in cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[str, bytes, int, float],
                                         Union[str, bytes, int, float]] = None
            ) -> Union[str, bytes, int, float]:
        """get value from the redis db"""
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    def get_str(key):
        """get str to automatically parametrize cache.get"""

        return self.get(key, str)

    def get_int(key):
        """get int to automatically parametrize cache.get"""
        return self.get(key, int)
