#!/usr/bin/env python3
"""
Title: Redis distribution
Description: redis exercises that demonstrates the various functionality
of redis module
Author: @a_idk
"""

import sys
from functools import wraps
from uuid import uuid4
from typing import Union, Optional, Callable
import redis


UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """ counting the cache class call frequency """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrap method """

        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ add input and store output """

    key = method.__qualname__
    inp = "".join([key, ":inputs"])
    outp = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrap method """

        self._redis.rpush(inp, str(args))
        out = method(self, *args, **kwargs)
        self._redis.rpush(outp, str(out))
        return out
    return wrapper


class Cache:
    """ Cache class """

    def __init__(self):
        """ initializing redis model (constructor) """

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        """ generate and store key """

        k = str(uuid4())  # generating key
        self._redis.mset({k: data})
        return k

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> UnionOfTypes:
        """ Get method """

        if fn:
            return fn(self._redis.get(key))

        data = self._redis.get(key)
        return data

    def get_str(self: bytes) -> str:
        """ getting a string """

        return self.decode("utf-8")

    def get_int(self: bytes) -> int:
        """ getting an int """

        return int.from_bytes(self, sys.byteorder)
