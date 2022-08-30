import unittest

from iot.ftps.client._version import VERSION, __version__


class TestVersion(unittest.TestCase):
    """package version testing"""

    def test_versions_match(self):
        self.assertEqual(VERSION, __version__)

    def test_version_structure(self):
        """major.minor.patch"""
        self.assertGreaterEqual(len(__version__), 5)
        self.assertGreaterEqual(len(VERSION), 5)
        split = VERSION.split(".")
        _splits = __version__.split(".")
        self.assertEqual(len(split), 3)
        self.assertEqual(len(_splits), 3)


if __name__ == "__main__":
    unittest.main()
