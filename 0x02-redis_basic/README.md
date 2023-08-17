# 0x02-redis_basic

This repository contains tasks for learning basic usage of Redis, an open-source in-memory data structure store.

## Tasks

### 0. Writing strings to Redis

The [0-redis_server](0-redis_server) bash script starts a Redis server in a Docker container.

### 1. Reading from Redis and printing

The [1-redis_op.py](1-redis_op.py) Python script connects to the Redis server started in task 0 and reads/prints data from it.

It prints the following:

- The string "Redis client connected to the server" when connected
- The values stored in Redis for the following keys:
  - __holbertonschools__: The value stored for key __holbertonschools__
  - __lemen__: The value stored for key __lemen__
  - __happy__: The value stored for key __happy__

### 2. Incrementing values

The [2-redis_op.py](2-redis_op.py) Python script connects to the Redis server and increments the values stored for keys __lemen__ and __happy__.

It prints the following:

- The string "Redis client connected to the server" when connected
- The values stored after incrementing:
  - __lemen__: The incremented value stored for key __lemen__
  - __happy__: The incremented value stored for key __happy__  

### 3. Storing lists

The [3-redis_lists.py](3-redis_lists.py) Python script connects to the Redis server and stores the following as lists:

- The list __holbertonschools__: with the values "Todd", "John", "Bob"
- The list __users__: with the values "Bret", "Samantha", "Bob"

It prints the following:

- The string "Redis client connected to the server" when connected  
- The lists stored in Redis

### 4. Retrieving lists 

The [4-redis_sort.py](4-redis_sort.py) Python script connects to the Redis server and retrieves the lists stored in task 3. 

It sorts the __holbertonschools__ list and stores it as __holbertonschools_sorted__.

It prints the following:

- The string "Redis client connected to the server" when connected
- The sorted __holbertonschools_sorted__ list
- The __users__ list

### 5. Implementing an expiring web cache and tracker

The [web.py](web.py) Python script implements a web cache that tracks how many times a page has been accessed.

It implements the following:

- A GET route at `/` that displays the number of times the root path `/` has been accessed
- A GET route at `/count` that increments and displays the count for the root path `/`
- A expiration time of 10 seconds for the count - after 10 seconds without a request, the count resets to 0

Run it with `$ python3 web.py` to test the caching and tracking.

### 6. Implementing the LRU algorithm

The [100-most_connections.py](100-most_connections.py) Python script implements an LRU (Least Recently Used) algorithm to delete keys when a Redis server maxmemory limit is reached.

It prints the following:

- When maxmemory is reached, it displays `LRU started` 
- When a key is deleted, it displays `LRU: Delete key <key>` replacing <key> with the deleted key name

Run it simultaneously with the [100-generator.py](100-generator.py) script to test LRU deleting keys.

## Resources

- [Redis documentation](https://redis.io/documentation)
- [Redis commands](https://redis.io/commands/)
- [Redis Python client](https://github.com/redis/redis-py)
- [Docker Hub Redis image](https://hub.docker.com/_/redis/)


## Tasks To Complete

+ [x] 0. **Writing strings to Redis**<br/>[exercise.py](exercise.py) contains a Python script that meets the following requirements:
  + Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.
  + Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g. using `uuid`), store the input data in Redis using the random key and return the key.
  + Type-annotate `store` correctly. Remember that `data` can be a `str`, `bytes`, `int` or `float`.

+ [x] 1. **Reading from Redis and recovering original type**<br/>[exercise.py](exercise.py) contains a Python script with the following updates to the previous task:
  + Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store `"a"` as a UTF-8 string, it will be returned as `b"a"` when retrieved from the server.
  + In this exercise we will create a `get` method that take a `key` string argument and an optional `Callable` argument named `fn`. This callable will be used to convert the data back to the desired format.
  + Remember to conserve the original `Redis.get` behavior if the key does not exist.
  + Also, implement 2 new methods: `get_str` and `get_int` that will automatically parametrize `Cache.get` with the correct conversion function.
  + The following code should not raise an Exception:
    ```python
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
    ```

+ [x] 2. **Incrementing values**<br/>[exercise.py](exercise.py) contains a Python script with the following updates to the previous task:
  + Familiarize yourself with the `INCR` command and its python equivalent.
  + In this task, we will implement a system to count how many times methods of the `Cache` class are called.
  + Above `Cache` define a `count_calls` decorator that takes a single `method` `Callable` argument and returns a `Callable`.
  + As a key, use the qualified name of `method` using the `__qualname__` dunder method.
  + Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.
  + Remember that the first argument of the wrapped function will be `self` which is the instance itself, which lets you access the Redis instance.
  + **Protip**: when defining a decorator it is useful to use `functool.wraps` to conserve the original function’s name, docstring, etc. Make sure you use it as described [here](https://docs.python.org/3.7/library/functools.html#functools.wraps).
  + Decorate `Cache.store` with `count_calls`.

+ [x] 3. **Storing lists**<br/>[exercise.py](exercise.py) contains a Python script with the following updates to the previous task:
  + Familiarize yourself with redis commands `RPUSH`, `LPUSH`, `LRANGE`, etc.
  + In this task, we will define a `call_history` decorator to store the history of inputs and outputs for a particular function.
  + Everytime the original function will be called, we will add its input parameters to one list in redis, and store its output into another list.
  + In `call_history`, use the decorated function’s qualified name and append `":inputs"` and `":outputs"` to create input and output list keys, respectively.
  + `call_history` has a single parameter named `method` that is a `Callable` and returns a `Callable`.
  + In the new function that the decorator will return, use `rpush` to append the input arguments. Remember that Redis can only store strings, bytes and numbers. Therefore, we can simply use `str(args)` to normalize. We can ignore potential `kwargs` for now.
  + Execute the wrapped function to retrieve the output. Store the output using `rpush` in the `"...:outputs"` list, then return the output.
  + Decorate `Cache.store` with `call_history`.

+ [x] 4. **Retrieving lists**<br/>[exercise.py](exercise.py) contains a Python script with the following updates to the previous task:
  + In this task, we will implement a `replay` function to display the history of calls of a particular function.
  + The output generated should look like this:
    ```py
    >>> cache = Cache()
    >>> cache.store("foo")
    >>> cache.store("bar")
    >>> cache.store(42)
    >>> replay(cache.store)
    Cache.store was called 3 times:
    Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
    Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
    Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
    ```

+ [x] 5. **Implementing an expiring web cache and tracker**<br/>[web.py](web.py) contains a Python script that meets the following requirements:
  + In this tasks, we will implement a `get_page` function (prototype: `def get_page(url: str) -> str:`). The core of the function is very simple. It uses the `requests` module to obtain the HTML content of a particular URL and returns it.
  + Start in a new file named [web.py](web.py) and do not reuse the code written in [exercise.py](exercise.py).
  + Inside `get_page` track how many times a particular URL was accessed in the key `"count:{url}"` and cache the result with an expiration time of 10 seconds.
  + **Tip**: Use [http://slowwly.robertomurray.co.uk](http://slowwly.robertomurray.co.uk) to simulate a slow response and test your caching.
  + **Bonus**: implement this use case with decorators.

