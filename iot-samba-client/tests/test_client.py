import tempfile
import unittest
from unittest import mock

from iot.samba.client import IoTSambaClient


class TestClient(unittest.TestCase):
    """package client testing"""

    @mock.patch("iot.samba.client._client.smbclient")
    def setUp(self, mock_smbclient):
        mock_smbclient.register_session.return_value = True
        self.samba_client = IoTSambaClient(
            smb_server="test_server",
            smb_host="test_host",
            smb_port=445,
            smb_user="test_user",
            smb_pass="test_pass",
        )
        self.assertEqual(self.samba_client.smb_server, "TEST_SERVER")
        self.assertEqual(self.samba_client.smb_host, "test_host")
        self.assertEqual(self.samba_client.smb_port, 445)
        self.assertEqual(self.samba_client.smb_user, "test_user")
        self.assertEqual(self.samba_client.smb_pass, "test_pass")

    def test_repr(self):
        repr_str = self.samba_client.__repr__()
        self.assertIsNotNone(repr_str)

    def test_is_connected(self):
        connected = self.samba_client.is_connected()
        self.assertIsNot(connected, True)

    def test_is_connected_fail(self):
        self.samba_client.smb_session = None
        connected = self.samba_client.is_connected()
        self.assertEqual(connected, False)

    def test_disconnect(self):
        disconnected = self.samba_client.disconnect()
        self.assertEqual(disconnected, None)

    @mock.patch("iot.samba.client._client.smbclient")
    def test_stat(self, mock_smbclient):
        self.samba_client.smb_host = "test_host"
        mock_smbclient.stat.return_value = "SmbStatResult"
        file_info = self.samba_client.stat(
            share="test_share",
            path="test/path",
            file="test.txt",
        )
        self.assertIsNotNone(file_info)

    def test_stat_fail(self):
        self.samba_client.smb_host = "test_host"
        file_info = self.samba_client.stat(
            share="test_share",
            path="test/path",
            file="test.txt",
        )
        self.assertIsNone(file_info)

    @mock.patch.object(IoTSambaClient, "download_file")
    def test_download_file(self, mock_download_file):
        mock_download_file.return_value = True
        download_result = self.samba_client.download_file(
            share="test_share",
            path="test/path",
            file="test.txt",
            dest="test/path/test.txt",
        )
        self.assertEqual(download_result, True)
        mock_download_file.assert_called_with(
            share="test_share",
            path="test/path",
            file="test.txt",
            dest="test/path/test.txt",
        )

    @mock.patch("iot.samba.client._client.smbclient")
    def test_download_file_fail(self, mock_smbclient):
        self.samba_client.smb_host = "test_host"
        temp_file = tempfile.NamedTemporaryFile()

        def side_effect(file_path, mode):
            return open(temp_file.name)

        mock_smbclient.open_file.side_effect = side_effect

        download_result = self.samba_client.download_file(
            share="test_share",
            path="test/path",
            file="test.txt",
            dest=temp_file.name,
        )
        temp_file.close()
        self.assertEqual(download_result, False)

    @mock.patch.object(IoTSambaClient, "upload_file")
    def test_upload_file(self, mock_upload_file):
        mock_upload_file.return_value = True
        upload_result = self.samba_client.upload_file(
            share="test_share",
            path="test/path",
            file="test.txt",
            source="test/path/test.txt",
        )
        self.assertEqual(upload_result, True)
        mock_upload_file.assert_called_with(
            share="test_share",
            path="test/path",
            file="test.txt",
            source="test/path/test.txt",
        )

    @mock.patch("iot.samba.client._client.smbclient")
    def test_upload_file_fail(self, mock_smbclient):
        self.samba_client.smb_host = "test_host"
        temp_file = tempfile.NamedTemporaryFile()

        def side_effect(file_path, mode):
            return open(temp_file.name)

        mock_smbclient.open_file.side_effect = side_effect

        upload_result = self.samba_client.upload_file(
            share="test_share",
            path="test/path",
            file="test.txt",
            source=temp_file.name,
        )
        temp_file.close()
        self.assertEqual(upload_result, False)

    @mock.patch.object(IoTSambaClient, "delete_file")
    def test_delete_file(self, mock_delete_file):
        mock_delete_file.return_value = True
        delete_result = self.samba_client.delete_file(
            share="test_share",
            path="test/path",
            file="test.txt",
        )
        self.assertEqual(delete_result, True)
        mock_delete_file.assert_called_with(
            share="test_share",
            path="test/path",
            file="test.txt",
        )

    @mock.patch("iot.samba.client._client.smbclient")
    def test_delete_file_success(self, mock_smbclient):
        self.samba_client.smb_host = "test_host"
        mock_smbclient.remove.return_value = None
        delete_result = self.samba_client.delete_file(
            share="test_share", path="test/path", file="test.txt"
        )
        self.assertEqual(delete_result, True)

    def test_delete_file_fail(self):
        self.samba_client.smb_host = "test_host"
        delete_result = self.samba_client.delete_file(
            share="test_share", path="test/path", file="test.txt"
        )
        self.assertEqual(delete_result, False)

    @mock.patch.object(IoTSambaClient, "move_file")
    def test_move_file(self, mock_move_file):
        mock_move_file.return_value = True
        move_result = self.samba_client.move_file(
            share="test_share",
            path="test/path",
            file="test.txt",
            new_path="new/test/path",
            new_file="new_test.txt",
        )
        self.assertEqual(move_result, True)
        mock_move_file.assert_called_with(
            share="test_share",
            path="test/path",
            file="test.txt",
            new_path="new/test/path",
            new_file="new_test.txt",
        )

    @mock.patch("iot.samba.client._client.smbclient")
    def test_move_file_success(self, mock_smbclient):
        self.samba_client.smb_host = "test_host"
        mock_smbclient.rename.return_value = None
        move_result = self.samba_client.move_file(
            share="test_share",
            path="test/path",
            file="test.txt",
            new_path="new/test/path",
            new_file="new_test.txt",
        )
        self.assertEqual(move_result, True)

    def test_move_file_fail(self):
        self.samba_client.smb_host = "test_host"
        move_result = self.samba_client.move_file(
            share="test_share",
            path="test/path",
            file="test.txt",
            new_path="new/test/path",
            new_file="new_test.txt",
        )
        self.assertEqual(move_result, False)

    @mock.patch.object(IoTSambaClient, "list_files")
    def test_list_files(self, mock_list_files):
        mock_list_files.return_value = ["test", "file"]
        files = self.samba_client.list_files(
            share="test_share",
            path="test/path",
            file_pattern="*",
        )
        self.assertEqual(files, ["test", "file"])
        mock_list_files.assert_called_with(
            share="test_share",
            path="test/path",
            file_pattern="*",
        )

    @mock.patch("iot.samba.client._client.smbclient")
    def test_list_files_success(self, mock_smbclient):
        self.samba_client.smb_host = "test_host"
        mock_smbclient.listdir.return_value = ["test", "file"]
        files = self.samba_client.list_files(
            share="test_share",
            path="test/path",
            file_pattern="*",
        )
        self.assertIsNotNone(files)

    def test_list_files_fail(self):
        self.samba_client.smb_host = "test_host"
        files = self.samba_client.list_files(
            share="test_share",
            path="test/path",
            file_pattern="*",
        )
        self.assertIsNone(files)


if __name__ == "__main__":
    unittest.main()
