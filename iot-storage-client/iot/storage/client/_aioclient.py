"""wrapper for azure blob storage async interactions"""

import os
import tempfile
import time
from datetime import datetime, timedelta
from typing import List, Optional, Union

from azure.storage.blob import (
    ContentSettings,
    BlobSasPermissions,
    generate_blob_sas,
    generate_container_sas,
)
from azure.storage.blob.aio import BlobClient, BlobServiceClient, ContainerClient

from ._helpers import (
    generate_cloud_conn_str,
    generate_cloud_sas_url,
    generate_edge_conn_str,
    generate_edge_sas_url,
    generate_local_conn_str,
    generate_local_sas_url,
)
from ._types import CredentialType, LocationType


class IoTStorageClientAsync:
    """iot storage client async"""

    credential_type: str
    location_type: str
    account_name: str
    credential: str
    connection_string: str

    module: Optional[str] = None
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
        module: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[str] = None,
    ) -> None:
        self.credential_type = credential_type
        self.location_type = location_type
        self.account_name = account_name
        self.credential = credential
        self.module = module
        self.host = host
        self.port = port
        self.instantiate_service_client()

    def __repr__(self) -> str:
        return (
            "IoT Storage Client Async\n"
            "---------------------\n"
            f"credential type: {self.credential_type.lower()}\n"
            f"location type: {self.location_type.lower()}\n"
            f"account name: {self.account_name}\n"
            f"credential: {self.credential[0:5]}****"
        )

    def instantiate_service_client(self) -> None:
        """init service_client based on credential and location types"""
        if self.credential_type == CredentialType.CONNECTION_STRING:
            self.connection_string = self.credential
            self.service_client = BlobServiceClient.from_connection_string(
                self.credential
            )
        else:
            if self.location_type == LocationType.CLOUD_BASED:
                connection_string = generate_cloud_conn_str(
                    account=self.account_name,
                    account_key=self.credential
                    if self.credential_type == CredentialType.ACCOUNT_KEY
                    else None,
                    account_sas=self.credential
                    if self.credential_type == CredentialType.ACCOUNT_SAS
                    else None,
                )
                self.connection_string = connection_string
                self.service_client = BlobServiceClient.from_connection_string(
                    connection_string
                )
            if self.location_type == LocationType.EDGE_BASED:
                connection_string = generate_edge_conn_str(
                    host=self.host,
                    port=self.port,
                    account=self.account_name,
                    account_key=self.credential
                    if self.credential_type == CredentialType.ACCOUNT_KEY
                    else None,
                    account_sas=self.credential
                    if self.credential_type == CredentialType.ACCOUNT_SAS
                    else None,
                )
                self.connection_string = connection_string
                self.service_client = BlobServiceClient.from_connection_string(
                    connection_string
                )
            if self.location_type == LocationType.LOCAL_BASED:
                connection_string = generate_local_conn_str(
                    module=self.module,
                    port=self.port,
                    account=self.account_name,
                    account_key=self.credential
                    if self.credential_type == CredentialType.ACCOUNT_KEY
                    else None,
                    account_sas=self.credential
                    if self.credential_type == CredentialType.ACCOUNT_SAS
                    else None,
                )
                self.connection_string = connection_string
                self.service_client = BlobServiceClient.from_connection_string(
                    connection_string
                )

    async def container_exists(self, container_name: str) -> bool:
        """check if a container exists"""
        try:
            async with self.service_client:
                container_client = self.service_client.get_container_client(
                    container=container_name
                )
                exists = await container_client.exists()
                return exists
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def file_exists(self, container_name: str, file_name: str) -> bool:
        """check if a file exists"""
        try:
            async with self.service_client:
                blob_client = self.service_client.get_blob_client(
                    container=container_name, blob=file_name
                )
                exists = await blob_client.exists()
                return exists
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def create_container(self, container_name: str) -> bool:
        """create a new container"""
        try:
            async with self.service_client:
                container_client = self.service_client.get_container_client(
                    container=container_name
                )
                await container_client.create_container()
                return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def delete_container(self, container_name: str) -> bool:
        """delete a container"""
        try:
            async with self.service_client:
                container_client = self.service_client.get_container_client(
                    container=container_name
                )
                await container_client.delete_container()
                return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def download(self, container_name: str, source: str, dest: str) -> bool:
        """download a file or directory to a path on the local filesystem"""
        try:
            if not dest:
                raise Exception("a destination must be provided")

            blobs = await self.list_files(container_name, source, recursive=True)
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
                    await self.download_file(container_name, blob, blob_dest)
            else:
                await self.download_file(container_name, source, dest)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def download_file(self, container_name: str, source: str, dest: str) -> bool:
        """download a file to a path on the local filesystem"""
        try:
            if dest.endswith("."):
                dest += "/"
            blob_dest = dest + os.path.basename(source) if dest.endswith("/") else dest

            os.makedirs(os.path.dirname(blob_dest), exist_ok=True)

            async with self.service_client:
                blob_client = self.service_client.get_blob_client(
                    container=container_name, blob=source
                )

                if not dest.endswith("/"):
                    with open(blob_dest, "wb") as file:
                        data = await blob_client.download_blob()
                        file.write(data.readall())
                    return True
                return False
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def upload(self, container_name: str, source: str, dest: str) -> bool:
        """upload a file or directory to a path inside the container"""
        if os.path.isdir(source):
            return await self.upload_dir(container_name, source, dest)
        else:
            return await self.upload_file(container_name, source, dest)

    async def upload_dir(self, container_name: str, source: str, dest: str) -> bool:
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
                    await self.upload_file(container_name, file_path, blob_path)
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def upload_file(
        self,
        container_name: str,
        source: str,
        dest: str,
        content_type: Optional[str] = "application/octet-stream",
        overwrite: Optional[bool] = True,
    ) -> bool:
        """upload a single file to a path inside the container"""
        try:
            async with self.service_client:
                container_client = self.service_client.get_container_client(
                    container=container_name
                )

                with open(source, "rb") as data:
                    await container_client.upload_blob(
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

    async def delete_dir(self, container_name: str, path: str) -> bool:
        """remove a directory and its contents recursively"""
        try:
            blobs = await self.list_files(container_name, path, recursive=True)
            if not blobs:
                return True

            if not path == "" and not path.endswith("/"):
                path += "/"
            blobs = [path + blob for blob in blobs]

            async with self.service_client:
                container_client = self.service_client.get_container_client(
                    container=container_name
                )
                await container_client.delete_blobs(*blobs)
                return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def delete_file(self, container_name: str, path: str) -> bool:
        """remove a single file from a path inside the container"""
        try:
            async with self.service_client:
                container_client = self.service_client.get_container_client(
                    container=container_name
                )
                await container_client.delete_blob(path)
                return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def list_files(
        self, container_name: str, path: str, recursive: Optional[bool] = False
    ) -> Union[List[str], None]:
        """list files under a path, optionally recursive"""
        try:
            if not path == "" and not path.endswith("/"):
                path += "/"

            async with self.service_client:
                container_client = self.service_client.get_container_client(
                    container=container_name
                )
                blob_iter = await container_client.list_blobs(name_starts_with=path)

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

    async def list_dirs(
        self, container_name: str, path: str, recursive: Optional[bool] = False
    ) -> Union[List[str], None]:
        """list directories under a path, optionally recursive"""
        try:
            if not path == "" and not path.endswith("/"):
                path += "/"

            async with self.service_client:
                container_client = self.service_client.get_container_client(
                    container=container_name
                )
                blob_iter = await container_client.list_blobs(name_starts_with=path)

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

    async def copy_file(
        self, container_name: str, source: str, dest_container: str, dest: str
    ) -> bool:
        """copy a file between any location within the same storage account"""
        try:
            # download to tempfile
            temp_file = tempfile.NamedTemporaryFile()
            download_result = await self.download_file(
                container_name=container_name,
                source=source,
                dest=temp_file.name,
            )
            if not download_result:
                print(f"unable to download file: {container_name}/{source}")
                temp_file.close()
                return False

            # upload tempfile
            upload_result = await self.upload_file(
                container_name=dest_container,
                source=temp_file.name,
                dest=dest,
            )
            if not upload_result:
                print(f"unable to upload file: {dest_container}/{dest}")
                temp_file.close()
                return False

            # cleanup
            temp_file.close()
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            try:
                temp_file.close()
            except Exception:
                pass
            pass
        return False

    async def move_file(
        self, container_name: str, source: str, dest_container: str, dest: str
    ) -> bool:
        """move a file between any location within the same storage account"""
        try:
            copy_result = await self.copy_file(
                container_name, source, dest_container, dest
            )
            if not copy_result:
                print(
                    f"unable to move file: {container_name}/{source} -> {dest_container}/{dest}"
                )
                return False

            delete_result = await self.delete_file(container_name, source)
            if not delete_result:
                print(f"unable to delete file after copy: {container_name}/{source}")
                return False
            return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def copy_from_url(
        self,
        source_url: str,
        container_name: str,
        dest: str,
        timeout: Optional[int] = 100,
    ) -> bool:
        """copy a file from a URL to a path inside the container"""
        try:
            async with self.service_client:
                blob_client = self.service_client.get_blob_client(
                    container=container_name, blob=dest
                )
                await blob_client.start_copy_from_url(source_url)
                for i in range(10):
                    props = await blob_client.get_blob_properties()
                    print(f"copy status: {props.copy.status}")
                    if props.copy.status == "success":
                        # complete!
                        break
                    time.sleep(timeout / 10)

                if props.copy.status != "success":
                    # if not complete after `timeout` seconds,
                    # abort the operation safely
                    props = await blob_client.get_blob_properties()
                    print(f"timeout status: {props.copy.status}")
                    await blob_client.abort_copy(props.copy.id)
                    props = await blob_client.get_blob_properties()
                    print(f"abort status: {props.copy.status}")
                    return False
                return True
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return False

    async def generate_file_sas_url(
        self,
        container_name: str,
        source: str,
        read: Optional[bool] = True,
        write: Optional[bool] = False,
        delete: Optional[bool] = False,
        start: Optional[Union[datetime, str]] = None,
        expiry: Optional[Union[datetime, str]] = datetime.utcnow()
        + timedelta(minutes=15),
    ) -> Union[str, None]:
        """generate a SAS URL for a given file inside the container"""
        try:
            async with self.service_client:
                account_key = self.service_client.credential.account_key
                sas_token = generate_blob_sas(
                    account_name=self.account_name,
                    container_name=container_name,
                    blob_name=source,
                    account_key=account_key,
                    permission=BlobSasPermissions(
                        read=read,
                        add=write,
                        create=write,
                        delete=delete,
                        tag=write,
                    ),
                    start=start,
                    expiry=expiry,
                    ip=self.host,
                )
                if not sas_token:
                    print(
                        f"unable to generate SAS token: {self.account_name}/{container_name}/{source}"
                    )
                    return None

                if self.location_type == LocationType.CLOUD_BASED:
                    return generate_cloud_sas_url(
                        account=self.account_name,
                        account_sas=sas_token,
                        blob_path=f"{container_name}/{source}",
                    )
                if self.location_type == LocationType.EDGE_BASED:
                    return generate_edge_sas_url(
                        host=self.host,
                        port=self.port,
                        account=self.account_name,
                        account_sas=sas_token,
                        blob_path=f"{container_name}/{source}",
                    )
                if self.location_type == LocationType.LOCAL_BASED:
                    return generate_local_sas_url(
                        module=self.module,
                        port=self.port,
                        account=self.account_name,
                        account_sas=sas_token,
                        blob_path=f"{container_name}/{source}",
                    )
                return None
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return None

    async def generate_container_sas_url(
        self,
        container_name: str,
        read: Optional[bool] = True,
        write: Optional[bool] = False,
        delete: Optional[bool] = False,
        start: Optional[Union[datetime, str]] = None,
        expiry: Optional[Union[datetime, str]] = datetime.utcnow()
        + timedelta(minutes=15),
    ) -> Union[str, None]:
        """generate a SAS URL for a given storage account container"""
        try:
            async with self.service_client:
                account_key = self.service_client.credential.account_key
                sas_token = generate_container_sas(
                    account_name=self.account_name,
                    container_name=container_name,
                    account_key=account_key,
                    permission=BlobSasPermissions(
                        read=read,
                        add=write,
                        create=write,
                        delete=delete,
                        tag=write,
                    ),
                    start=start,
                    expiry=expiry,
                    ip=self.host,
                )
                if not sas_token:
                    print(
                        f"unable to generate SAS token: {self.account_name}/{container_name}"
                    )
                    return None

                if self.location_type == LocationType.CLOUD_BASED:
                    return generate_cloud_sas_url(
                        account=self.account_name,
                        account_sas=sas_token,
                        blob_path=container_name,
                    )
                if self.location_type == LocationType.EDGE_BASED:
                    return generate_edge_sas_url(
                        host=self.host,
                        port=self.port,
                        account=self.account_name,
                        account_sas=sas_token,
                        blob_path=container_name,
                    )
                if self.location_type == LocationType.LOCAL_BASED:
                    return generate_local_sas_url(
                        module=self.module,
                        port=self.port,
                        account=self.account_name,
                        account_sas=sas_token,
                        blob_path=container_name,
                    )
                return None
        except Exception as ex:
            print(f"unexpected exception occurred: {ex}")
            pass
        return None
