import asyncio
import random

class Storage:
    def __init__(self):
        self.data = []
        self.max_delay = 0
        self.error_probability = 0

    def get_max_delay(self):
        return self.max_delay
    
    def set_max_delay(self, max_delay):
        self.max_delay = max_delay
        return self

    def get_error_probability(self):
        return self.error_probability
    
    def set_error_probability(self, error_probability):
        self.error_probability = error_probability
        return self

    async def _simulate_connection(self):
        await random_sleep(self.max_delay)
        if random.random() < self.error_probability:
            raise RuntimeError("Connection error.")
          
    async def set(self, key, value):
        await self._simulate_connection()
        self.data = [[k, v] for [k, v] in self.data if k != key] + [[key, value]]
        return self

    async def get(self, key):
        await self._simulate_connection()
        vals =  [v for [k, v] in self.data if k == key]
        if vals == []:
            raise KeyError("The value for the key does not exists.")
        return vals[0]
    

def run(coroutine):
    return asyncio.run(coroutine)

def random_sleep(max_delay):
    return sleep(random.random() * max_delay)

def sleep(delay):
    return asyncio.sleep(delay)

def arun(coroutine):
    return asyncio.create_task(coroutine)

