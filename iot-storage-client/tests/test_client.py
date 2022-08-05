import unittest

from iot.storage.client import IoTStorageClient


class TestClient(unittest.TestCase):
    """package client testing"""

    def test_account_key_cloud_based_init(self):
        storage_client = IoTStorageClient(
            credential_type="ACCOUNT_KEY",
            location_type="CLOUD_BASED",
            account_name="myStorageAccount",
            credential="myAccountKey",
        )
        self.assertEqual(storage_client.credential_type, "ACCOUNT_KEY")
        self.assertEqual(storage_client.location_type, "CLOUD_BASED")
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(storage_client.credential, "myAccountKey")

    def test_account_key_edge_based_init(self):
        storage_client = IoTStorageClient(
            credential_type="ACCOUNT_KEY",
            location_type="EDGE_BASED",
            account_name="myStorageAccount",
            credential="myAccountKey",
            host="127.0.0.1",
            port="10000",
        )
        self.assertEqual(storage_client.credential_type, "ACCOUNT_KEY")
        self.assertEqual(storage_client.location_type, "EDGE_BASED")
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(storage_client.credential, "myAccountKey")
        self.assertEqual(storage_client.host, "127.0.0.1")
        self.assertEqual(storage_client.port, "10000")

    def test_connection_string_cloud_based_init(self):
        storage_client = IoTStorageClient(
            credential_type="CONNECTION_STRING",
            location_type="CLOUD_BASED",
            account_name="myStorageAccount",
            credential="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1",
        )
        self.assertEqual(storage_client.credential_type, "CONNECTION_STRING")
        self.assertEqual(storage_client.location_type, "CLOUD_BASED")
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(
            storage_client.credential,
            "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1",
        )

    def test_connection_string_edge_based_init(self):
        storage_client = IoTStorageClient(
            credential_type="CONNECTION_STRING",
            location_type="EDGE_BASED",
            account_name="myStorageAccount",
            credential="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1",
            host="myIPAddress",
            port="myPort",
        )
        self.assertEqual(storage_client.credential_type, "CONNECTION_STRING")
        self.assertEqual(storage_client.location_type, "EDGE_BASED")
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(
            storage_client.credential,
            "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1",
        )
        self.assertEqual(storage_client.host, "myIPAddress")
        self.assertEqual(storage_client.port, "myPort")

    def test_invalid_location_type_init(self):
        storage_client = IoTStorageClient(
            credential_type="ACCOUNT_KEY",
            location_type="somewhere_over_the_rainbow",
            account_name="myStorageAccount",
            credential="myAccountKey",
        )
        self.assertEqual(storage_client.location_type, "INVALID")

    def test_invalid_credential_type_init(self):
        storage_client = IoTStorageClient(
            credential_type="street_cred",
            location_type="CLOUD_BASED",
            account_name="myStorageAccount",
            credential="myAccountKey",
        )
        self.assertEqual(storage_client.credential_type, "INVALID")


if __name__ == "__main__":
    unittest.main()
