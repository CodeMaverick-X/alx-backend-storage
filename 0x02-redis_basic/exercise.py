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
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store value in cache"""
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
