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


def generate_edge_sas_url(
    host: str,
    port: str,
    account: str,
    account_sas: str,
    blob_path: Optional[str] = None,
) -> str:
    """
    generate a SAS url for a child gateway device
    interacting with a parent gateway storage account
    """
    if not blob_path:
        return "http://{host}:{port}/{account}.blob.core.windows.net?{sas}".format(
            host=host,
            port=port,
            account=account,
            sas=account_sas,
        )
    return "http://{host}:{port}/{account}.blob.core.windows.net/{path}?{sas}".format(
        host=host,
        port=port,
        account=account,
        path=blob_path,
        sas=account_sas,
    )


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


def generate_local_sas_url(
    module: str,
    port: str,
    account: str,
    account_sas: str,
    blob_path: Optional[str] = None,
) -> str:
    """
    generate a SAS url for an edge gateway device
    interacting with a locally available storage account
    (AzureBlobStorageonIoTEdge)
    """
    if not blob_path:
        return "http://{module}:{port}/{account}.blob.core.windows.net?{sas}".format(
            module=module,
            port=port,
            account=account,
            sas=account_sas,
        )
    return "http://{module}:{port}/{account}.blob.core.windows.net/{path}?{sas}".format(
        module=module,
        port=port,
        account=account,
        path=blob_path,
        sas=account_sas,
    )


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


def generate_cloud_sas_url(
    account: str,
    account_sas: str,
    blob_path: Optional[str] = None,
) -> str:
    """
    generate a SAS url for an edge gateway device
    interacting with a cloud storage account
    """
    if not blob_path:
        return "https://{account}.blob.core.windows.net?{sas}".format(
            account=account,
            sas=account_sas,
        )
    return "https://{account}.blob.core.windows.net/{path}?{sas}".format(
        account=account,
        path=blob_path,
        sas=account_sas,
    )
