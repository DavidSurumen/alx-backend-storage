#!/usr/bin/env python3
"""
Redis Operations Module
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Defines the methods to cache data in Redis
    """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores input data in redis using a random key

        Args:
            data: string | bytes | int | float

        Return:
            key: string that represents the key
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
