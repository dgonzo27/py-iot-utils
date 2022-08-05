"""client related types"""


class CredentialType:
    """iot storage client credential types for authentication"""

    ACCOUNT_KEY = "ACCOUNT_KEY"
    CONNECTION_STRING = "CONNECTION_STRING"


class LocationType:
    """iot storage client location types for storage accounts"""

    CLOUD_BASED = "CLOUD_BASED"
    EDGE_BASED = "EDGE_BASED"
