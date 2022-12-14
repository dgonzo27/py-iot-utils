import unittest

from iot.lru.cache import IoTLRUCache


class TestCache(unittest.TestCase):
    """package cache testing"""

    def setUp(self):
        self.lru_cache = IoTLRUCache(capacity=4)
        self.assertEqual(self.lru_cache.capacity, 4)

    def test_repr(self):
        repr_str = self.lru_cache.__repr__()
        self.assertIsNotNone(repr_str)

    def test_put_and_get(self):
        self.lru_cache.put(key=1, value="test")
        self.assertEqual(len(self.lru_cache.cache), 1)
        self.assertEqual(self.lru_cache.get(key=1), "test")
        self.assertEqual(self.lru_cache.get(12), -1)

        # test eviction
        self.lru_cache.put(key=2, value="test2")
        self.lru_cache.put(key=3, value="test3")
        self.lru_cache.put(key=4, value="test4")
        self.lru_cache.put(key=5, value="test5")
        self.assertEqual(self.lru_cache.get(1), -1)
