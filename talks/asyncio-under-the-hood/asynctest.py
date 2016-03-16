import asyncio

from aioredis import create_connection


@asyncio.coroutine
def do(loop):
    redis = yield from create_connection(('localhost', 6379), loop=loop)
    start = loop.time()
    tasks = [asyncio.ensure_future(apply(redis, str(x).encode())) for x in range(10000)]
    yield from asyncio.wait(tasks)
    end = loop.time()
    print('Time spent:', end - start)
    redis.close()
    yield from redis.wait_closed()


@asyncio.coroutine
def apply(redis, num):
    key = b'foo' + num
    yield from redis.execute(b'set', key, num)
    result = yield from redis.execute(b'get', key)
    assert result == num


loop = asyncio.get_event_loop()
loop.run_until_complete(do(loop))
loop.stop()
