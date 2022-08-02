"""wrapper for azure blob storage interactions"""

import os
from typing import List, Optional, Union

from azure.storage.blob import (
    BlobClient,
    BlobServiceClient,
    ContainerClient,
    ContentSettings,
)


class CredentialType:
    """iot storage client credential types for authentication"""

    ACCOUNT_KEY = "ACCOUNT_KEY"
    CONNECTION_STRING = "CONNECTION_STRING"


class LocationType:
    """iot storage client location types for storage accounts"""

    CLOUD_BASED = "CLOUD_BASED"
    EDGE_BASED = "EDGE_BASED"


class IoTStorageClient:
    """iot storage client"""

    credential_type: str
    location_type: str
    account_name: str
    credential: str

    host: Optional[str] = None
    port: Optional[str] = None

    service_client: BlobServiceClient
    container_client: ContainerClient
    blob_client: BlobClient

    def __init__(
        self,
        credential_type: str,
        location_type: str,
        account_name: str,
        credential: str,
        host: Optional[str] = None,
        port: Optional[str] = None,
    ) -> None:
        self.credential_type = credential_type
        self.location_type = location_type
        self.account_name = account_name
        self.credential = credential
        self.host = host
        self.port = port
        self.instantiate_service_client()

    def __repr__(self) -> str:
        return (
            "IoT Storage Client\n"
            "---------------------\n"
            f"credential type: {self.credential_type.lower()}\n"
            f"location type: {self.location_type.lower()}\n"
            f"account name: {self.account_name}\n"
            f"credential: {self.credential[0:5]}****"
        )

    def instantiate_service_client(self) -> None:
        """init service_client based on credential and location types"""
        if self.credential_type == CredentialType.CONNECTION_STRING:
            self.service_client = BlobServiceClient.from_connection_string(
                self.credential
            )
        elif self.credential_type == CredentialType.ACCOUNT_KEY:
            if self.location_type == LocationType.CLOUD_BASED:
                self.service_client = BlobServiceClient(
                    account_url=f"https://{self.account_name}.blob.core.windows.net",
                    credential=self.credential,
                )
            elif self.location_type == LocationType.EDGE_BASED:
                self.service_client = BlobServiceClient(
                    account_url=f"http://{self.host}:{self.port}/{self.account_name}.blob.core.windows.net",
                    credential=self.credential,
                )
            else:
                print(
                    "invalid location type, please use one of LocationType[CLOUD_BASED, EDGE_BASED]"
                )
        else:
            print(
                "invalid credential type, please use one of CredentialType[ACCOUNT_KEY, CONNECTION_STRING"
            )

    def container_exists(self, container_name: str) -> bool:
        """check if a container exists"""
        try:
            container_client = self.service_client.get_container_client(
                container=container_name
            )
            return container_client.exists()
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def file_exists(self, container_name: str, file_name: str) -> bool:
        """check if a file exists"""
        try:
            blob_client = self.service_client.get_blob_client(
                container=container_name, blob=file_name
            )
            return blob_client.exists()
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def download(self, container_name: str, source: str, dest: str) -> bool:
        """download a file or directory to a path on the local filesystem"""
        try:
            if not dest:
                raise Exception("a destination must be provided")

            blobs = self.list_files(container_name, source, recursive=True)
            if blobs:
                # if source is a directory, dest must also be a directory
                if not source == "" and not source.endswith("/"):
                    source += "/"
                if not dest.endswith("/"):
                    dest += "/"

                # append the directory name from source to the destination
                dest += os.path.basename(os.path.normpath(source)) + "/"
                blobs = [source + blob for blob in blobs]
                for blob in blobs:
                    blob_dest = dest + os.path.relpath(blob, source)
                    self.download_file(container_name, blob, blob_dest)
            else:
                self.download_file(container_name, source, dest)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def download_file(self, container_name: str, source: str, dest: str) -> bool:
        """download a file to a path on the local filesystem"""
        try:
            if dest.endswith("."):
                dest += "/"
            blob_dest = dest + os.path.basename(source) if dest.endswith("/") else dest

            os.makedirs(os.path.dirname(blob_dest), exist_ok=True)
            blob_client = self.service_client.get_blob_client(
                container=container_name, blob=blob_dest
            )

            if not dest.endswith("/"):
                with open(blob_dest, "wb") as file:
                    data = blob_client.download_blob()
                    file.write(data.readall())
                return True
            return False
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def upload(self, container_name: str, source: str, dest: str) -> bool:
        """upload a file or directory to a path inside the container"""
        if os.path.isdir(source):
            return self.upload_dir(container_name, source, dest)
        else:
            return self.upload_file(container_name, source, dest)

    def upload_dir(self, container_name: str, source: str, dest: str) -> bool:
        """upload a directory to a path inside the container"""
        try:
            prefix = "" if dest == "" else dest + "/"
            prefix + os.path.basename(source) + "/"
            for root, dirs, files in os.walk(source):
                for name in files:
                    dir_part = os.path.relpath(root, source)
                    dir_part = "" if dir_part == "." else dir_part + "/"
                    file_path = os.path.join(root, name)
                    blob_path = prefix + dir_part + name
                    self.upload_file(container_name, file_path, blob_path)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def upload_file(
        self,
        container_name: str,
        source: str,
        dest: str,
        content_type: Optional[str] = "application/octet-stream",
        overwrite: Optional[bool] = True,
    ) -> bool:
        """upload a single file to a path inside the container"""
        try:
            container_client = self.service_client.get_container_client(
                container_name=container_name
            )

            with open(source, "rb") as data:
                container_client.upload_blob(
                    name=dest,
                    data=data,
                    overwrite=overwrite,
                    content_settings=ContentSettings(content_type=content_type),
                )
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def delete_dir(self, container_name: str, path: str) -> bool:
        """remove a directory and its contents recursively"""
        try:
            blobs = self.list_files(container_name, path, recursive=True)
            if not blobs:
                return True

            if not path == "" and not path.endswith("/"):
                path += "/"
            blobs = [path + blob for blob in blobs]

            container_client = self.service_client.get_container_client(
                container_name=container_name
            )
            container_client.delete_blobs(*blobs)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def delete_file(self, container_name: str, path: str) -> bool:
        """remove a single file from a path inside the container"""
        try:
            container_client = self.service_client.get_container_client(
                container=container_name
            )
            container_client.delete_blob(path)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    def list_files(
        self, container_name: str, path: str, recursive: Optional[bool] = False
    ) -> Union[List[str], None]:
        """list files under a path, optionally recursive"""
        try:
            if not path == "" and not path.endswith("/"):
                path += "/"

            container_client = self.service_client.get_container_client(
                container=container_name
            )
            blob_iter = container_client.list_blobs(name_starts_with=path)

            files = []
            for blob in blob_iter:
                relative_path = os.path.relpath(blob.name, path)
                if recursive or not "/" in relative_path:
                    files.append(relative_path)
            return files
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return None

    def list_dirs(
        self, container_name: str, path: str, recursive: Optional[bool] = False
    ) -> Union[List[str], None]:
        """list directories under a path, optionally recursive"""
        try:
            if not path == "" and not path.endswith("/"):
                path += "/"

            container_client = self.service_client.get_container_client(
                container=container_name
            )
            blob_iter = container_client.list_blobs(name_starts_with=path)

            dirs = []
            for blob in blob_iter:
                relative_dir = os.path.dirname(os.path.relpath(blob.name, path))
                if (
                    relative_dir
                    and (recursive or not "/" in relative_dir)
                    and not relative_dir in dirs
                ):
                    dirs.append(relative_dir)
            return dirs
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return None
