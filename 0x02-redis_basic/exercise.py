#!/usr/bin/env python3
"""
Redis Operations Module
"""
import redis
import uuid
from typing import Union, Callable
import functools


def count_calls(method: Callable) -> Callable:
    """ decorator function to count the function calls """
    @functools.wraps(method)
    def wrapper(self, data):
        """This is the wrapper function for count_calls decorator"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, data)
    return wrapper


class Cache:
    """
    Defines the methods to cache data in Redis
    """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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

    def get(self, key: str, fn: Callable = None) -> \
            Union[str, bytes, int, float]:
        """
        Retrieves a value from a redis data store, in orginal form
        """
        data = self._redis.get(key)
        # if key does not exist return None -original Redis.get behaviour
        return fn(data) if fn is not None and data is not None else data

    def get_str(self, key: str) -> str:
        """
        Retrieves a string value from a redis data store
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieves an int value from a redis data store
        """
        return self.get(key, lambda x: int(x))
