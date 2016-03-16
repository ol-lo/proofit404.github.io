from time import time

from redis import StrictRedis


def do():
    redis = StrictRedis()
    start = time()
    for x in range(10000):
        apply(redis, str(x).encode())
    end = time()
    print('Time spent:', end - start)


def apply(redis, num):
    key = b'foo' + num
    redis.execute_command('set', key, num)
    result = redis.execute_command('get', key)
    assert result == num


do()
