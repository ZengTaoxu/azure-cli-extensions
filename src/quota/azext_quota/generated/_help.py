# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['quota'] = '''
    type: group
    short-summary: Manage Azure Quota Extension API
'''

helps['quota usage'] = """
    type: group
    short-summary: Manage usage with quota
"""

helps['quota usage list'] = """
    type: command
    short-summary: "Get a list of current usage for all resources for the scope specified."
    examples:
      - name: Quotas_listUsagesForCompute
        text: |-
               az quota usage list --scope "subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Comp\
ute/locations/eastus"
      - name: Quotas_listUsagesForNetwork
        text: |-
               az quota usage list --scope "subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Netw\
ork/locations/eastus"
      - name: Quotas_listUsagesMachineLearningServices
        text: |-
               az quota usage list --scope "subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Mach\
ineLearningServices/locations/eastus"
"""

helps['quota usage show'] = """
    type: command
    short-summary: "Get the current usage of a resource."
    examples:
      - name: Quotas_UsagesRequest_ForCompute
        text: |-
               az quota usage show --resource-name "standardNDSFamily" --scope "subscriptions/00000000-0000-0000-0000-0\
00000000000/providers/Microsoft.Compute/locations/eastus"
      - name: Quotas_UsagesRequest_ForNetwork
        text: |-
               az quota usage show --resource-name "MinPublicIpInterNetworkPrefixLength" --scope \
"subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Network/locations/eastus"
"""

helps['quota list'] = """
    type: command
    short-summary: "Get a list of current quota limits of all resources for the specified scope. The response from \
this GET operation can be leveraged to submit requests to update a quota."
    examples:
      - name: Quotas_listQuotaLimitsForCompute
        text: |-
               az quota list --scope "subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Compute/lo\
cations/eastus"
      - name: Quotas_listQuotaLimitsForNetwork
        text: |-
               az quota list --scope "subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Network/lo\
cations/eastus"
      - name: Quotas_listQuotaLimitsMachineLearningServices
        text: |-
               az quota list --scope "subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.MachineLea\
rningServices/locations/eastus"
"""

helps['quota show'] = """
    type: command
    short-summary: "Get the quota limit of a resource. The response can be used to determine the remaining quota to \
calculate a new quota limit that can be submitted with a PUT request."
    examples:
      - name: Quotas_Get_Request_ForCompute
        text: |-
               az quota show --resource-name "standardNDSFamily" --scope "subscriptions/00000000-0000-0000-0000-0000000\
00000/providers/Microsoft.Compute/locations/eastus"
      - name: Quotas_UsagesRequest_ForNetwork
        text: |-
               az quota show --resource-name "MinPublicIpInterNetworkPrefixLength" --scope \
"subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Network/locations/eastus"
"""

helps['quota create'] = """
    type: command
    short-summary: "Create the quota limit for the specified resource with the requested value. To update the quota, \
follow these steps: 1. Use the GET operation for quotas and usages to determine how much quota remains for the \
specific resource and to calculate the new quota limit. These steps are detailed in [this \
example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/21836\
70). 2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed \
status of the request."
    parameters:
      - name: --limit-object
        short-summary: "The resource quota limit value."
        long-summary: |
            Usage: --limit-object value=XX limit-type=XX limit-object-type=XX
            value: Required. The quota/limit value
            limit-type: The quota or usages limit types.
            limit-object-type: Required. The limit object type.
    examples:
      - name: Quotas_PutRequest_ForNetwork
        text: |-
               az quota create --resource-name "MinPublicIpInterNetworkPrefixLength" --scope "subscriptions/00000000-00\
00-0000-0000-000000000000/providers/Microsoft.Network/locations/eastus" \
--limit-object value=10 limit-object-type=LimitValue --resource-type MinPublicIpInterNetworkPrefixLength
      - name: Quotas_PutRequest_ForNetwork_StandardSkuPublicIpAddressesResource
        text: |-
               az quota create --resource-name "StandardSkuPublicIpAddresses" --scope "subscriptions/00000000-0000-0000\
-0000-000000000000/providers/Microsoft.Network/locations/eastus" \
--limit-object value=10 limit-object-type=LimitValue --resource-type PublicIpAddresses
      - name: Quotas_Put_Request_ForCompute
        text: |-
               az quota create --resource-name "standardFSv2Family" --scope "subscriptions/00000000-0000-0000-0000-0000\
00000000/providers/Microsoft.Compute/locations/eastus" \
--limit-object value=10 limit-object-type=LimitValue
      - name: Quotas_Request_ForMachineLearningServices_LowPriorityResource
        text: |-
               az quota create  --resource-name "TotalLowPriorityCores" --scope "subscriptions/00000000-0000-0000-0000-\
000000000000/providers/Microsoft.MachineLearning/Services/locations/eastus" \
--limit-object value=10 limit-object-type=LimitValue --resource-type lowPriority
"""

helps['quota update'] = """
    type: command
    short-summary: "Update the quota limit for a specific resource to the specified value: 1. Use the Usages-GET and \
Quota-GET operations to determine the remaining quota for the specific resource and to calculate the new quota limit. \
These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using\
-the-new-quota-rest-api/ba-p/2183670). 2. Use this PUT operation to update the quota limit. Please check the URI in \
location header for the detailed status of the request."
    parameters:
      - name: --limit-object
        short-summary: "The resource quota limit value."
        long-summary: |
            Usage: --limit-object value=XX limit-type=XX limit-object-type=XX
            value: Required. The quota/limit value
            limit-type: The quota or usages limit types.
            limit-object-type: Required. The limit object type.
    examples:
      - name: Quotas_Request_PatchForCompute
        text: |-
               az quota update --resource-name "standardFSv2Family" --scope "subscriptions/00000000-0000-0000-0000-0000\
00000000/providers/Microsoft.Compute/locations/eastus" --limit-object value=10 limit-object-type=LimitValue
      - name: Quotas_Request_PatchForNetwork
        text: |-
               az quota update --resource-name "MinPublicIpInterNetworkPrefixLength" --scope "subscriptions/00000000-00\
00-0000-0000-000000000000/providers/Microsoft.Network/locations/eastus" \
--limit-object value=10 limit-object-type=LimitValue --resource-type MinPublicIpInterNetworkPrefixLength
"""

helps['quota wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the quota is met.
    examples:
      - name: Pause executing next line of CLI script until the quota is successfully created.
        text: |-
               az quota wait --resource-name "MinPublicIpInterNetworkPrefixLength" --scope "subscriptions/00000000-0000\
-0000-0000-000000000000/providers/Microsoft.Network/locations/eastus" --created
      - name: Pause executing next line of CLI script until the quota is successfully updated.
        text: |-
               az quota wait --resource-name "MinPublicIpInterNetworkPrefixLength" --scope "subscriptions/00000000-0000\
-0000-0000-000000000000/providers/Microsoft.Network/locations/eastus" --updated
"""

helps['quota request'] = """
    type: group
    short-summary: Manage quota request with quota
"""

helps['quota request status'] = """
    type: group
    short-summary: Manage quota request status with quota
"""

helps['quota request status list'] = """
    type: command
    short-summary: "For the specified scope, get the current quota requests for a one year period ending at the time \
is made. Use the **oData** filter to select quota requests."
    examples:
      - name: QuotaRequestHistory
        text: |-
               az quota request status list --scope "subscriptions/00000000-0000-0000-0000-000000000000/providers/M\
icrosoft.Compute/locations/eastus"
"""

helps['quota request status show'] = """
    type: command
    short-summary: "Get the quota request details and status by quota request ID for the resources of the resource \
provider at a specific location. The quota request ID **id** is returned in the response of the PUT operation."
    examples:
      - name: QuotaRequestFailed
        text: |-
               az quota request status show --id "00000000-0000-0000-0000-000000000000" --scope \
"subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Compute/locations/eastus"
      - name: QuotaRequestInProgress
        text: |-
               az quota request status show --id "00000000-0000-0000-0000-000000000000" --scope \
"subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Compute/locations/eastus"
      - name: QuotaRequestStatus
        text: |-
               az quota request status show --id "00000000-0000-0000-0000-000000000000" --scope \
"subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Compute/locations/eastus"
"""

helps['quota operation'] = """
    type: group
    short-summary: Manage quota operation with quota
"""

helps['quota operation list'] = """
    type: command
    short-summary: "List all the operations supported by the Microsoft.Quota resource provider."
    examples:
      - name: GetOperations
        text: |-
               az quota operation list
"""
