"""least recently used (LRU) cache"""

from collections import OrderedDict
from typing import Any


class IoTLRUCache:
    """iot lru cache"""

    cache: OrderedDict
    capacity: int

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def __repr__(self) -> str:
        return (
            "IoT LRU Cache\n"
            "-----------------\n"
            f"capacity: {self.capacity}\n"
            f"remaining capacity: {self.capacity - len(self.cache)}"
        )

    def get(self, key: Any) -> Any:
        """retrieve the value of a key if it exists, default returns -1"""
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=True)
        return self.cache[key]

    def put(self, key: Any, value: Any) -> None:
        """update the value of a key if it exists, or add the key-value pair to the cache"""
        if len(self.cache) == self.capacity and key not in self.cache:
            # evict the LRU key if the cache has reached its capacity
            self.cache.pop(next(iter(self.cache.items()))[0])
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
