import unittest

from SimpleCache2 import simple_cache
from SimpleCache2.FileCache import FileCache


class FileCacheTest(unittest.TestCase):

    def setUp(self):
        self.cache = FileCache()

    def test(self):
        print(self.cache.cache_dir)
        self.cache.set('test1', (1, 2), 10)
        g = self.cache.get('test1')
        self.assertEqual((1, 2), g)

    def test2(self):
        self.cache.set('test2', [1, 2], 10)
        g = self.cache.get('test2')
        self.assertEqual([1, 2], g)

    def test3(self):
        self.cache.set('test3', {"hello": "world"}, 10)
        g = self.cache.get('test3')
        self.assertEqual({"hello": "world"}, g)

    def test4(self):
        self.cache.set('test4', "string", 10)
        g = self.cache.get('test4')
        self.assertEqual("string", g)

    def test5(self):
        def testFunc(name):
            return f"hello world {name}"

        g = self.cache.call('test5', 10, testFunc, 'Bob')
        self.assertEqual("hello world Bob", g)
        pass

    def test6Decorator(self):
        @simple_cache(self.cache, 10)
        def testFunc(name):
            return f"hello world {name}"

        self.assertEqual(testFunc('Bob'), testFunc('Bob'))
        self.assertNotEqual(testFunc('Bob'), testFunc('Dan'))
        pass
