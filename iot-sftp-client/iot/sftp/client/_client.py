"""wrapper for SFTP server interactions"""

import os
from typing import List, Optional, Union

import pysftp


class IoTSFTPClient:
    """iot sftp client"""

    sftp_host: str
    sftp_port: int
    sftp_user: str
    sftp_pass: str
    sftp_session: pysftp.Connection

    def __init__(
        self,
        sftp_host: str,
        sftp_port: int,
        sftp_user: str,
        sftp_pass: str,
    ) -> None:
        self.sftp_host = sftp_host
        self.sftp_port = sftp_port
        self.sftp_user = sftp_user
        self.sftp_pass = sftp_pass

    def __repr__(self) -> str:
        return (
            "IoT SFTP Client\n"
            "-------------------\n"
            f"host: {self.sftp_host}\n"
            f"port: {self.sftp_port}\n"
            f"user: {self.sftp_user}"
        )

    def instantiate_sftp_session(self):
        """init sftp_session based on input params"""
        try:
            self.sftp_session = pysftp.Connection(
                host=self.sftp_host,
                port=self.sftp_port,
                username=self.sftp_user,
                password=self.sftp_pass,
            )
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return

    def is_connected(self) -> bool:
        """checks if the current session is connected to the sftpclient"""
        try:
            return self.sftp_session is None
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def disconnect(self) -> None:
        """disconnect the current session from the sftpclient"""
        try:
            self.sftp_session.close()
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return

    def exists(self, path: str) -> bool:
        """
        checks if a file or directory exists on the SFTP
        server under a remote path
        """
        try:
            return self.stfp_session.exists(path)
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def download_file(self, source: str, dest: str) -> bool:
        """download a file to a path on the local filesystem"""
        try:
            self.sftp_session.get(source, dest)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def upload_file(self, source: str, dest: str) -> bool:
        """upload a file to a path inside the SFTP server"""
        try:
            self.sftp_session.put(source, dest, callback=None, confirm=False)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def delete_file(self, path: str) -> bool:
        """delete a file from under a path inside the SFTP server"""
        try:
            self.sftp_session.remove(path)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def move_file(self, source: str, dest: str) -> bool:
        """move a file inside the SFTP server to another path inside the SFTP server"""
        try:
            self.sftp_session.rename(source, dest)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def list_files(
        self, path: str, file_pattern: Optional[str] = None
    ) -> Union[List[str], None]:
        """list files under a path inside the SFTP server"""
        try:
            files = self.sftp_session.listdir(path)
            if not files:
                return None

            if file_pattern:
                return [f for f in files if file_pattern in f]
            return files
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return None
