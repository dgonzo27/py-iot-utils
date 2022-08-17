import unittest
from unittest import mock

from iot.sftp.client import IoTSFTPClient


class TestClient(unittest.TestCase):
    """package client testing"""

    @mock.patch("iot.sftp.client._client.pysftp")
    def setUp(self, mock_pysftp):
        mock_pysftp.Connection.return_value = True
        self.sftp_client = IoTSFTPClient(
            sftp_host="test_host",
            sftp_port=22,
            sftp_user="test_user",
            sftp_pass="test_pass",
        )
        self.assertEqual(self.sftp_client.sftp_host, "test_host")
        self.assertEqual(self.sftp_client.sftp_port, 22)
        self.assertEqual(self.sftp_client.sftp_user, "test_user")
        self.assertEqual(self.sftp_client.sftp_pass, "test_pass")

    @mock.patch.object(IoTSFTPClient, "exists")
    def test_exists(self, mock_exists):
        mock_exists.return_value = True
        exists = self.sftp_client.exists(path="test/path")
        self.assertEqual(exists, True)
        mock_exists.assert_called_with(path="test/path")

    @mock.patch.object(IoTSFTPClient, "download_file")
    def test_download_file(self, mock_download_file):
        mock_download_file.return_value = True
        download_result = self.sftp_client.download_file(source="test", dest="path")
        self.assertEqual(download_result, True)
        mock_download_file.assert_called_with(source="test", dest="path")

    @mock.patch.object(IoTSFTPClient, "upload_file")
    def test_upload_file(self, mock_upload_file):
        mock_upload_file.return_value = True
        upload_result = self.sftp_client.upload_file(source="test", dest="path")
        self.assertEqual(upload_result, True)
        mock_upload_file.assert_called_with(source="test", dest="path")

    @mock.patch.object(IoTSFTPClient, "delete_file")
    def test_delete_file(self, mock_delete_file):
        mock_delete_file.return_value = True
        delete_result = self.sftp_client.delete_file(path="test/path")
        self.assertTrue(delete_result, True)
        mock_delete_file.assert_called_with(path="test/path")

    @mock.patch.object(IoTSFTPClient, "move_file")
    def test_move_file(self, mock_move_file):
        mock_move_file.return_value = True
        move_result = self.sftp_client.move_file(source="test", dest="path")
        self.assertEqual(move_result, True)
        mock_move_file.assert_called_with(source="test", dest="path")

    @mock.patch.object(IoTSFTPClient, "list_files")
    def test_list_files(self, mock_list_files):
        mock_list_files.return_value = ["test", "files"]
        files = self.sftp_client.list_files(path="test", file_pattern="path")
        self.assertEqual(files, ["test", "files"])
        mock_list_files.assert_called_with(path="test", file_pattern="path")


if __name__ == "__main__":
    unittest.main()
