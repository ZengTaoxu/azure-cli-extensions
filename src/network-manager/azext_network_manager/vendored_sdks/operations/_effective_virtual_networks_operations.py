# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_by_network_manager_request(
    subscription_id: str,
    resource_group_name: str,
    network_manager_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    top: Optional[int] = None,
    skip_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-05-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/listEffectiveVirtualNetworks')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "networkManagerName": _SERIALIZER.url("network_manager_name", network_manager_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if top is not None:
        query_parameters['$top'] = _SERIALIZER.query("top", top, 'int', maximum=20, minimum=1)
    if skip_token is not None:
        query_parameters['$skipToken'] = _SERIALIZER.query("skip_token", skip_token, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )

class EffectiveVirtualNetworksOperations(object):
    """EffectiveVirtualNetworksOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.network.v2021_05_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_by_network_manager(
        self,
        resource_group_name: str,
        network_manager_name: str,
        parameters: "_models.EffectiveVirtualNetworksParameter",
        top: Optional[int] = None,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.EffectiveVirtualNetworksListResult":
        """List effective virtual networks in a network manager.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param network_manager_name: The name of the network manager.
        :type network_manager_name: str
        :param parameters: Effective Virtual Networks Parameter.
        :type parameters:
         ~azure.mgmt.network.v2021_05_01_preview.models.EffectiveVirtualNetworksParameter
        :param top: An optional query parameter which specifies the maximum number of records to be
         returned by the server.
        :type top: int
        :param skip_token: SkipToken is only used if a previous operation returned a partial result. If
         a previous response contains a nextLink element, the value of the nextLink element will include
         a skipToken parameter that specifies a starting point to use for subsequent calls.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EffectiveVirtualNetworksListResult, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2021_05_01_preview.models.EffectiveVirtualNetworksListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EffectiveVirtualNetworksListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'EffectiveVirtualNetworksParameter')

        request = build_list_by_network_manager_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            network_manager_name=network_manager_name,
            content_type=content_type,
            json=_json,
            top=top,
            skip_token=skip_token,
            template_url=self.list_by_network_manager.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('EffectiveVirtualNetworksListResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_by_network_manager.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/listEffectiveVirtualNetworks'}  # type: ignore

