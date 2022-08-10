import os
import tempfile
import unittest

from iot.storage.client import IoTStorageClient

CONTAINER_ONE = "container-one"
CONTAINER_TWO = "container-two"
FILE_ONE = "file-one.json"
FILE_TWO = "file-two.json"

INTEGRATION_TESTS = os.getenv("INTEGRATION_TESTS")
ACCOUNT_NAME = os.getenv("ACCOUNT_NAME")
ACCOUNT_KEY = os.getenv("ACCOUNT_KEY")
CNX_STR = os.getenv("CNX_STR")


class TestIntegrationClient(unittest.TestCase):
    """package client integration testing"""

    def setUp(self):
        if INTEGRATION_TESTS is not None:
            self.ak_storage_client = IoTStorageClient(
                credential_type="ACCOUNT_KEY",
                location_type="CLOUD_BASED",
                account_name=ACCOUNT_NAME,
                credential=ACCOUNT_KEY,
            )
            self.cnx_storage_client = IoTStorageClient(
                credential_type="CONNECTION_STRING",
                location_type="CLOUD_BASED",
                account_name=ACCOUNT_NAME,
                credential=CNX_STR,
            )

    def test_ak_container_exists(self):
        if INTEGRATION_TESTS == True:
            container_one_exists = self.ak_storage_client.container_exists(
                CONTAINER_ONE
            )
            container_two_exists = self.ak_storage_client.container_exists(
                CONTAINER_TWO
            )
            container_rando_exists = self.ak_storage_client.container_exists("random")
            self.assertEqual(container_one_exists, True)
            self.assertEqual(container_two_exists, True)
            self.assertEqual(container_rando_exists, False)

    def test_cnx_container_exists(self):
        if INTEGRATION_TESTS == True:
            container_one_exists = self.cnx_storage_client.container_exists(
                CONTAINER_ONE
            )
            container_two_exists = self.cnx_storage_client.container_exists(
                CONTAINER_TWO
            )
            container_rando_exists = self.cnx_storage_client.container_exists("random")
            self.assertEqual(container_one_exists, True)
            self.assertEqual(container_two_exists, True)
            self.assertEqual(container_rando_exists, False)

    def test_ak_file_exists(self):
        if INTEGRATION_TESTS == True:
            file_one_exists = self.ak_storage_client.file_exists(
                CONTAINER_ONE, FILE_ONE
            )
            file_two_exists = self.ak_storage_client.file_exists(
                CONTAINER_TWO, FILE_TWO
            )
            file_rando_exists = self.ak_storage_client.file_exists(
                CONTAINER_ONE, "random.txt"
            )
            self.assertEqual(file_one_exists, True)
            self.assertEqual(file_two_exists, True)
            self.assertEqual(file_rando_exists, False)

    def test_cnx_file_exists(self):
        if INTEGRATION_TESTS == True:
            file_one_exists = self.cnx_storage_client.file_exists(
                CONTAINER_ONE, FILE_ONE
            )
            file_two_exists = self.cnx_storage_client.file_exists(
                CONTAINER_TWO, FILE_TWO
            )
            file_rando_exists = self.cnx_storage_client.file_exists(
                CONTAINER_ONE, "random.txt"
            )
            self.assertEqual(file_one_exists, True)
            self.assertEqual(file_two_exists, True)
            self.assertEqual(file_rando_exists, False)

    def test_ak_file_download(self):
        if INTEGRATION_TESTS == True:
            temp_file = tempfile.NamedTemporaryFile()
            download_result = self.ak_storage_client.download_file(
                CONTAINER_ONE, FILE_ONE, temp_file.name
            )
            self.assertEqual(download_result, True)
            self.assertIsNotNone(temp_file)
            temp_file.close()

    def test_cnx_file_download(self):
        if INTEGRATION_TESTS == True:
            temp_file = tempfile.NamedTemporaryFile()
            download_result = self.cnx_storage_client.download_file(
                CONTAINER_TWO, FILE_TWO, temp_file.name
            )
            self.assertEqual(download_result, True)
            self.assertIsNotNone(temp_file)
            temp_file.close()
