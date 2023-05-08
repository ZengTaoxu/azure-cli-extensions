# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AuthenticationMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The mode of client authentication."""

    TOKEN = "Token"
    AAD = "AAD"


class AzureHybridBenefit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether Azure Hybrid Benefit is opted in."""

    TRUE = "True"
    FALSE = "False"
    NOT_APPLICABLE = "NotApplicable"


class ConnectivityStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the connectivity status of the connected cluster."""

    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    OFFLINE = "Offline"
    EXPIRED = "Expired"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class LastModifiedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that last modified the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class PrivateLinkState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Property which describes the state of private link on a connected cluster resource."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current deployment state of connectedClusters."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    UPDATING = "Updating"
    DELETING = "Deleting"
    ACCEPTED = "Accepted"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the connected cluster. The type 'SystemAssigned, includes a
    system created identity. The type 'None' means no identity is assigned to the connected
    cluster.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
