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


def call_history(method: Callable) -> Callable:
    """ decorator function to store history of inputs and outputs for
    a particular function."""
    @functools.wraps(method)
    def wrapper(self, *args):
        """wrapper for call_history decorator."""
        inputs = method.__qualname__ + ':inputs'
        outputs = method.__qualname__ + ':outputs'

        # store inputs in the inputs list
        if args is not None:
            self._redis.rpush(inputs, str(args))

        # call the function to obtain its output
        result = method(self, *args)

        # store output in outputs list
        self._redis.rpush(outputs, result)

        # return the result of the call back to the decorated function
        return result
    return wrapper


def replay(fn: Callable) -> None:
    """displays the history of calls for a particular function."""
    # create a redis instance
    rd_obj = redis.Redis()

    # get the keys
    func = fn.__qualname__
    inputs_key = func + ':inputs'
    outputs_key = func + ':outputs'

    # get the number of times a function has been called
    count = rd_obj.get(func)
    if count is not None:
        count = int(count)
    else:
        count = 0

    # display count
    print('{} was called {} time{}{}'.
          format(func, count, 's' if count != 1 else '',
                ':' if count > 0 else ''))

    # display function call history
    for key, val in zip(rd_obj.lrange(inputs_key, 0, -1),
                        rd_obj.lrange(outputs_key, 0, -1)):
        print('{}(*{}) -> {}'.format(func,
                                     key.decode('utf-8'),
                                     val.decode('utf-8')))


class Cache:
    """
    Defines the methods to cache data in Redis
    """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
