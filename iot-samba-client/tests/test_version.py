import unittest

from iot.samba.client._version import VERSION, __version__


class TestVersion(unittest.TestCase):
    """package version testing"""

    def test_versions_match(self):
        self.assertEqual(VERSION, __version__)

    def test_version_structure(self):
        """major.minor.patch"""
        self.assertGreaterEqual(len(__version__), 5)
        self.assertIn(".", __version__)


if __name__ == "__main__":
    unittest.main()
