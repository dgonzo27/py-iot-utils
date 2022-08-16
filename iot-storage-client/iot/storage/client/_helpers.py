"""helper functions for iot-storage-client"""

from typing import Optional


def generate_edge_conn_str(
    host: str,
    port: str,
    account: str,
    account_key: Optional[str] = None,
    account_sas: Optional[str] = None,
) -> str:
    """
    generate a connection string for a child gateway device
    interacting with a parent gateway storage account
    """
    if not account_key and not account_sas:
        return "Please provide your storage account key or SAS token"

    protocol = "DefaultEndpointsProtocol=http;"
    endpoint = f"BlobEndpoint=http://{host}:{port}/{account};"

    if account_key:
        credential = f"AccountName={account};AccountKey={account_key};"
    else:
        credential = f"SharedAccessSignature={account_sas};"
    return f"{protocol}{endpoint}{credential}"


def generate_local_conn_str(
    module: str,
    port: str,
    account: str,
    account_key: Optional[str] = None,
    account_sas: Optional[str] = None,
) -> str:
    """
    generate a connection string for an edge gateway device
    interacting with a locally available storage account
    (AzureBlobStorageonIoTEdge)
    """
    if not account_key and not account_sas:
        return "Please provide your storage account key or SAS token"

    protocol = "DefaultEndpointsProtocol=http;"
    endpoint = f"BlobEndpoint=http://{module}:{port}/{account};"

    if account_key:
        credential = f"AccountName={account};AccountKey={account_key};"
    else:
        credential = f"SharedAccessSignature={account_sas};"
    return f"{protocol}{endpoint}{credential}"


def generate_cloud_conn_str(
    account: str,
    account_key: Optional[str] = None,
    account_sas: Optional[str] = None,
) -> str:
    """
    generate a connection string for an edge gateway device
    interacting with a cloud storage account
    """
    if not account_key and not account_sas:
        return "Please provide your storage account key or SAS token"

    protocol = "DefaultEndpointsProtocol=https;"
    endpoint = f"BlobEndpoint=https://{account}.blob.core.windows.net;"

    if account_key:
        credential = f"AccountName={account};AccountKey={account_key};"
    else:
        credential = f"SharedAccessSignature={account_sas};"
    return f"{protocol}{endpoint}{credential}"
