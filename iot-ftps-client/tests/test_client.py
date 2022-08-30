import tempfile
import unittest
from unittest import mock

from iot.ftps.client._client import IoTFTPSClient


class TestClient(unittest.TestCase):
    """package client testing"""

    @mock.patch("iot.ftps.client._client.ftplib")
    def setUp(self, mock_ftplib):
        mock_ftplib.FTP.return_value = True
        mock_ftplib.FTP_TLS.return_value = True
        self.ftps_client = IoTFTPSClient(ftps_host="test_host")
        self.assertEqual(self.ftps_client.ftps_host, "test_host")

        self.ssl_ftps_client = IoTFTPSClient(
            ftps_host="test_host",
            ftps_port=990,
            ftps_user="test_user",
            ftps_pass="test_pass",
            ssl_implicit=True,
        )
        self.assertEqual(self.ssl_ftps_client.ftps_host, "test_host")
        self.assertEqual(self.ssl_ftps_client.ftps_port, 990)
        self.assertEqual(self.ssl_ftps_client.ftps_user, "test_user")
        self.assertEqual(self.ssl_ftps_client.ftps_pass, "test_pass")
        self.assertEqual(self.ssl_ftps_client.ssl_implicit, True)

    def test_repr(self):
        repr_str = self.ftps_client.__repr__()
        self.assertIsNotNone(repr_str)
        ssl_repr_str = self.ssl_ftps_client.__repr__()
        self.assertIsNotNone(ssl_repr_str)

    def test_disconnect(self):
        disconnected = self.ftps_client.disconnect()
        self.assertIsNone(disconnected)
        ssl_disconnected = self.ssl_ftps_client.disconnect()
        self.assertIsNone(ssl_disconnected)

    @mock.patch("iot.ftps.client._client.ftplib")
    def test_download_file(self, mock_ftplib):
        dest_file = tempfile.NamedTemporaryFile()
        src_file = tempfile.NamedTemporaryFile()

        def side_effect(filename, command):
            _file = filename.split("RETR ")[-1]
            with open(_file, "rb") as src:
                bytes = src.read()
                print(f"{bytes}")
            print(f"{command}")

        mock_ftplib.FTP.retrbinary.side_effect = side_effect
        mock_ftplib.FTP_TLS.retrbinary.side_effect = side_effect

        download_result = self.ftps_client.download_file(
            source=src_file.name,
            dest=dest_file.name,
        )
        ssl_download_result = self.ssl_ftps_client.download_file(
            source=src_file.name,
            dest=dest_file.name,
        )
        dest_file.close()
        src_file.close()

        self.assertEqual(download_result, False)
        self.assertEqual(ssl_download_result, False)

    @mock.patch("iot.ftps.client._client.ftplib")
    def test_upload_file(self, mock_ftplib):
        dest_file = tempfile.NamedTemporaryFile()
        src_file = tempfile.NamedTemporaryFile()

        def side_effect(filename, command):
            _file = filename.split("STOR ")[-1]
            with open(_file, "rb") as src:
                bytes = src.read()
                print(f"{bytes}")
            print(f"{command}")

        mock_ftplib.FTP.storbinary.side_effect = side_effect
        mock_ftplib.FTP_TLS.storbinary.side_effect = side_effect

        upload_result = self.ftps_client.upload_file(
            source=src_file.name,
            dest=dest_file.name,
        )
        ssl_upload_result = self.ssl_ftps_client.upload_file(
            source=src_file.name,
            dest=dest_file.name,
        )
        dest_file.close()
        src_file.close()

        self.assertEqual(upload_result, False)
        self.assertEqual(ssl_upload_result, False)

    def test_delete_file(self):
        delete_result = self.ftps_client.delete_file("test/path.txt")
        ssl_delete_result = self.ssl_ftps_client.delete_file("test/path.txt")
        self.assertEqual(delete_result, False)
        self.assertEqual(ssl_delete_result, False)

    def test_move_file(self):
        move_result = self.ftps_client.move_file("test/path.txt", "dest/path.txt")
        ssl_move_result = self.ssl_ftps_client.move_file(
            "test/path.txt", "dest/path.txt"
        )
        self.assertEqual(move_result, False)
        self.assertEqual(ssl_move_result, False)
