import unittest
from unittest import mock

from iot.storage.client import IoTStorageClient, CredentialType, LocationType


class TestCloudKeyClient(unittest.TestCase):
    """package client testing"""

    @mock.patch("iot.storage.client._client.BlobServiceClient")
    def setUp(self, mock_BlobServiceClient):
        mock_BlobServiceClient.BlobServiceClient.return_value = True
        self.storage_client = IoTStorageClient(
            credential_type=CredentialType.ACCOUNT_KEY,
            location_type=LocationType.CLOUD_BASED,
            account_name="myStorageAccount",
            credential="myAccountKey",
        )
        self.assertEqual(
            self.storage_client.credential_type, CredentialType.ACCOUNT_KEY
        )
        self.assertEqual(self.storage_client.location_type, LocationType.CLOUD_BASED)
        self.assertEqual(self.storage_client.account_name, "myStorageAccount")
        self.assertEqual(self.storage_client.credential, "myAccountKey")

    def test_repr(self):
        repr_str = self.storage_client.__repr__()
        self.assertIsNotNone(repr_str)

    @mock.patch("iot.storage.client._client.BlobServiceClient")
    @mock.patch("iot.storage.client._client.ContainerClient")
    def test_container_exists(self, mock_BlobServiceClient, mock_ContainerClient):
        def side_effect(container):
            return container

        mock_BlobServiceClient.get_container_client.side_effect = side_effect
        mock_ContainerClient.exists.return_value = True
        exists = self.storage_client.container_exists(container_name="test")
        self.assertIsNot(exists, False)

    def test_container_exists_fail(self):
        self.storage_client.service_client = None
        exists = self.storage_client.container_exists(container_name="test")
        self.assertEqual(exists, False)

    @mock.patch("iot.storage.client._client.BlobServiceClient")
    @mock.patch("iot.storage.client._client.BlobClient")
    def test_file_exists(self, mock_BlobServiceClient, mock_BlobClient):
        def side_effect(container, blob):
            return f"{container}/{blob}"

        mock_BlobServiceClient.get_blob_client.side_effect = side_effect
        mock_BlobClient.exists.return_value = True
        exists = self.storage_client.file_exists(
            container_name="test", file_name="blob"
        )
        self.assertIsNot(exists, False)

    def test_file_exists_fail(self):
        self.storage_client.service_client = None
        exists = self.storage_client.file_exists(
            container_name="test", file_name="blob"
        )
        self.assertEqual(exists, False)

    @mock.patch("iot.storage.client._client.BlobServiceClient")
    @mock.patch("iot.storage.client._client.BlobClient")
    def test_download(self, mock_BlobServiceClient, mock_BlobClient):
        def side_effect(container, blob):
            return f"{container}/{blob}"

        mock_BlobServiceClient.get_blob_client.side_effect = side_effect
        mock_BlobClient.download_blob.return_value = True
        download_result = self.storage_client.download(
            container_name="test",
            source="blob",
            dest="dest",
        )
        self.assertEqual(download_result, False)


class TestClientInit(unittest.TestCase):
    """package client init-based testing"""

    def test_account_key_cloud_based_init(self):
        storage_client = IoTStorageClient(
            credential_type=CredentialType.ACCOUNT_KEY,
            location_type=LocationType.CLOUD_BASED,
            account_name="myStorageAccount",
            credential="myAccountKey",
        )
        self.assertEqual(storage_client.credential_type, CredentialType.ACCOUNT_KEY)
        self.assertEqual(storage_client.location_type, LocationType.CLOUD_BASED)
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(storage_client.credential, "myAccountKey")

    def test_account_key_edge_based_init(self):
        storage_client = IoTStorageClient(
            credential_type=CredentialType.ACCOUNT_KEY,
            location_type=LocationType.EDGE_BASED,
            account_name="myStorageAccount",
            credential="myAccountKey",
            host="127.0.0.1",
            port="10000",
        )
        self.assertEqual(storage_client.credential_type, CredentialType.ACCOUNT_KEY)
        self.assertEqual(storage_client.location_type, LocationType.EDGE_BASED)
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(storage_client.credential, "myAccountKey")
        self.assertEqual(storage_client.host, "127.0.0.1")
        self.assertEqual(storage_client.port, "10000")

    def test_account_key_local_based_init(self):
        storage_client = IoTStorageClient(
            credential_type=CredentialType.ACCOUNT_KEY,
            location_type=LocationType.LOCAL_BASED,
            account_name="myStorageAccount",
            credential="myAccountKey",
            module="AzureBlobStorageonIoTEdge",
            host="127.0.0.1",
            port="10000",
        )
        self.assertEqual(storage_client.credential_type, CredentialType.ACCOUNT_KEY)
        self.assertEqual(storage_client.location_type, LocationType.LOCAL_BASED)
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(storage_client.credential, "myAccountKey")
        self.assertEqual(storage_client.module, "AzureBlobStorageonIoTEdge")
        self.assertEqual(storage_client.host, "127.0.0.1")
        self.assertEqual(storage_client.port, "10000")

    def test_account_sas_cloud_based_init(self):
        storage_client = IoTStorageClient(
            credential_type=CredentialType.ACCOUNT_SAS,
            location_type=LocationType.CLOUD_BASED,
            account_name="myStorageAccount",
            credential="?sv=2020-12-12&ss=bfqt&srt=sc&sp=rwdlacupiytfx&se=2030-12-12T00:00:00Z&st=2020-12-12T00:00:00Z&spr=https,http&sig=myAccountSAS",
        )
        self.assertEqual(storage_client.credential_type, CredentialType.ACCOUNT_SAS)
        self.assertEqual(storage_client.location_type, LocationType.CLOUD_BASED)
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(
            storage_client.credential,
            "?sv=2020-12-12&ss=bfqt&srt=sc&sp=rwdlacupiytfx&se=2030-12-12T00:00:00Z&st=2020-12-12T00:00:00Z&spr=https,http&sig=myAccountSAS",
        )

    def test_account_sas_edge_based_init(self):
        storage_client = IoTStorageClient(
            credential_type=CredentialType.ACCOUNT_SAS,
            location_type=LocationType.EDGE_BASED,
            account_name="myStorageAccount",
            credential="?sv=2020-12-12&ss=bfqt&srt=sc&sp=rwdlacupiytfx&se=2030-12-12T00:00:00Z&st=2020-12-12T00:00:00Z&spr=https,http&sig=myAccountSAS",
            host="127.0.0.1",
            port="10000",
        )
        self.assertEqual(storage_client.credential_type, CredentialType.ACCOUNT_SAS)
        self.assertEqual(storage_client.location_type, LocationType.EDGE_BASED)
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(
            storage_client.credential,
            "?sv=2020-12-12&ss=bfqt&srt=sc&sp=rwdlacupiytfx&se=2030-12-12T00:00:00Z&st=2020-12-12T00:00:00Z&spr=https,http&sig=myAccountSAS",
        )
        self.assertEqual(storage_client.host, "127.0.0.1")
        self.assertEqual(storage_client.port, "10000")

    def test_account_sas_local_based_init(self):
        storage_client = IoTStorageClient(
            credential_type=CredentialType.ACCOUNT_SAS,
            location_type=LocationType.LOCAL_BASED,
            account_name="myStorageAccount",
            credential="?sv=2020-12-12&ss=bfqt&srt=sc&sp=rwdlacupiytfx&se=2030-12-12T00:00:00Z&st=2020-12-12T00:00:00Z&spr=https,http&sig=myAccountSAS",
            module="AzureBlobStorageonIoTEdge",
            host="127.0.0.1",
            port="10000",
        )
        self.assertEqual(storage_client.credential_type, CredentialType.ACCOUNT_SAS)
        self.assertEqual(storage_client.location_type, LocationType.LOCAL_BASED)
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(
            storage_client.credential,
            "?sv=2020-12-12&ss=bfqt&srt=sc&sp=rwdlacupiytfx&se=2030-12-12T00:00:00Z&st=2020-12-12T00:00:00Z&spr=https,http&sig=myAccountSAS",
        )
        self.assertEqual(storage_client.module, "AzureBlobStorageonIoTEdge")
        self.assertEqual(storage_client.host, "127.0.0.1")
        self.assertEqual(storage_client.port, "10000")

    def test_connection_string_cloud_based_init(self):
        storage_client = IoTStorageClient(
            credential_type=CredentialType.CONNECTION_STRING,
            location_type=LocationType.CLOUD_BASED,
            account_name="myStorageAccount",
            credential="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1",
        )
        self.assertEqual(
            storage_client.credential_type, CredentialType.CONNECTION_STRING
        )
        self.assertEqual(storage_client.location_type, LocationType.CLOUD_BASED)
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(
            storage_client.credential,
            "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1",
        )

    def test_connection_string_edge_based_init(self):
        storage_client = IoTStorageClient(
            credential_type=CredentialType.CONNECTION_STRING,
            location_type=LocationType.EDGE_BASED,
            account_name="myStorageAccount",
            credential="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1",
            host="myIPAddress",
            port="myPort",
        )
        self.assertEqual(
            storage_client.credential_type, CredentialType.CONNECTION_STRING
        )
        self.assertEqual(storage_client.location_type, LocationType.EDGE_BASED)
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(
            storage_client.credential,
            "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1",
        )
        self.assertEqual(storage_client.host, "myIPAddress")
        self.assertEqual(storage_client.port, "myPort")

    def test_connection_string_local_based_init(self):
        storage_client = IoTStorageClient(
            credential_type=CredentialType.CONNECTION_STRING,
            location_type=LocationType.LOCAL_BASED,
            account_name="myStorageAccount",
            credential="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1",
            module="AzureBlobStorageonIoTEdge",
            host="127.0.0.1",
            port="10000",
        )
        self.assertEqual(
            storage_client.credential_type, CredentialType.CONNECTION_STRING
        )
        self.assertEqual(storage_client.location_type, LocationType.LOCAL_BASED)
        self.assertEqual(storage_client.account_name, "myStorageAccount")
        self.assertEqual(
            storage_client.credential,
            "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1",
        )
        self.assertEqual(storage_client.module, "AzureBlobStorageonIoTEdge")
        self.assertEqual(storage_client.host, "127.0.0.1")
        self.assertEqual(storage_client.port, "10000")


if __name__ == "__main__":
    unittest.main()
