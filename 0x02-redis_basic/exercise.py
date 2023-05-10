#!/usr/bin/env python
"""
contains a cache class
"""
import redis
import uuid
from typing import Union


class Cache:
    """class that creates a cache mech"""
    def __init__(self):
        """instatiate"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store value in cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn:
            Union[
                Callable[[bytes],
                         Union[str, bytes, int, float]], None] = None)\
            -> Union[str, bytes, int, float, None]:
        """Returns a stored data"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, int, float, None]:
        """Returns a stored data as string"""
        return self.get(key, str)

    def get_int(self, key: str) -> Union[str, bytes, int, float, None]:
        """Returns a stored data as int"""
        return self.get(key, int)
