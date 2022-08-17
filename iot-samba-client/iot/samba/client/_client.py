"""wrapper for samba file share interactions"""

import os
import socket
from typing import List, Optional, Union

import smbclient
from smbprotocol.session import Session


class IoTSambaClient:
    """iot samba client"""

    smb_server: str
    smb_host: str
    smb_port: int
    smb_user: str
    smb_pass: str

    smb_session: Session
    local_ip: str

    def __init__(
        self,
        smb_server: str,
        smb_host: str,
        smb_port: int,
        smb_user: str,
        smb_pass: str,
    ) -> None:
        self.smb_server = smb_server.upper()
        self.smb_host = smb_host
        self.smb_port = smb_port
        self.smb_user = smb_user
        self.smb_pass = smb_pass
        self.instantiate_smb_session()

    def __repr__(self) -> str:
        return (
            "IoT Samba Client\n"
            "-------------------\n"
            f"server: {self.smb_server}\n"
            f"host: {self.smb_host}:{self.smb_port}"
        )

    def instantiate_smb_session(self) -> None:
        """init smb_session based on input params"""
        hostname = socket.gethostname()
        self.local_ip = socket.gethostbyname(hostname)

        smbclient.ClientConfig(username=self.smb_user, password=self.smb_pass)
        self.smb_session = smbclient.register_session(
            server=self.smb_host,
            username=self.smb_user,
            password=self.smb_pass,
            port=self.smb_port,
            connection_timeout=30,
        )

    def is_connected(self) -> bool:
        """checks if the current session is connected to the smbclient"""
        try:
            if self.smb_session is None:
                return False
            return self.smb_session._connected
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def disconnect(self) -> None:
        """disconnect the current session from the smbclient"""
        try:
            self.smb_session.disconnect()
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass

    def stat(
        self,
        share: str,
        path: str,
        file: Optional[str] = "",
    ) -> Union[smbclient.SMBStatResult, None]:
        """returns file information for a given path"""
        try:
            stat_path = "\\\\{host}\\{share}\\{path}\\{file}".format(
                host=self.smb_host,
                share=share,
                path=path,
                file=file,
            )
            return smbclient.stat(stat_path)
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return None

    def download_file(
        self,
        share: str,
        path: str,
        file: str,
        dest: str,
    ) -> bool:
        """download a file to a path on the local filesystem"""
        try:
            file_path = "\\\\{host}\\{share}\\{path}\\{file}".format(
                host=self.smb_host,
                share=share,
                path=path,
                file=file,
            )
            if dest.endswith("."):
                dest += "/"
            blob_dest = (
                dest + os.path.basename(file_path) if dest.endswith("/") else dest
            )

            os.makedirs(os.path.dirname(blob_dest), exist_ok=True)
            with smbclient.open_file(file_path, mode="rb") as fd:
                file_bytes = fd.read()

            if not dest.endswith("/"):
                with open(blob_dest, "wb") as file:
                    file.write(file_bytes)
                return True
            return False
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def upload_file(
        self,
        share: str,
        path: str,
        file: str,
        source: str,
    ) -> bool:
        """upload a file to a path inside the samba server"""
        try:
            with open(source, "rb") as fd:
                file_bytes = fd.read()

            file_path = "\\\\{host}\\{share}\\{path}\\{file}".format(
                host=self.smb_host,
                share=share,
                path=path,
                file=file,
            )
            with smbclient.open_file(file_path, mode="wb") as file:
                file.write(file_bytes)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def delete_file(
        self,
        share: str,
        path: str,
        file: str,
    ) -> bool:
        """remove a single file from a path inside the samba server"""
        try:
            file_path = "\\\\{host}\\{share}\\{path}\\{file}".format(
                host=self.smb_host,
                share=share,
                path=path,
                file=file,
            )
            smbclient.remove(file_path)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def move_file(
        self,
        share: str,
        path: str,
        file: str,
        new_path: str,
        new_file: str,
    ) -> bool:
        """move a file inside the samba server to another path inside the samba server"""
        try:
            file_path = "\\\\{host}\\{share}\\{path}\\{file}".format(
                host=self.smb_host,
                share=share,
                path=path,
                file=file,
            )
            dest_path = "\\\\{host}\\{share}\\{path}\\{file}".format(
                host=self.smb_host,
                share=share,
                path=new_path,
                file=new_file,
            )
            smbclient.rename(file_path, dest_path)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def list_files(
        self, share: str, path: str, file_pattern: str
    ) -> Union[List[str], None]:
        """list files under a path inside the samba server"""
        try:
            list_path = "\\\\{host}\\{share}\\{path}\\".format(
                host=self.smb_host,
                share=share,
                path=path,
            )
            return smbclient.listdir(list_path, file_pattern)
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return None
