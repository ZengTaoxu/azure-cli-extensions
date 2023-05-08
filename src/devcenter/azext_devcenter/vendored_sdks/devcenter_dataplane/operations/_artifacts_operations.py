# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ArtifactsOperations(object):
    """ArtifactsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~dev_center_dataplane_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_environment(
        self,
        environment_name,  # type: str
        user_id="me",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ArtifactListResult"]
        """Lists the artifacts for an environment.

        :param environment_name: The name of the environment.
        :type environment_name: str
        :param user_id: The AAD object id of the user. If value is 'me', the identity is taken from the
         authentication context.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ArtifactListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~dev_center_dataplane_client.models.ArtifactListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ArtifactListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2022-11-11-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_environment.metadata['url']  # type: ignore
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'projectName': self._serialize.url("self._config.project_name", self._config.project_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                    'userId': self._serialize.url("user_id", user_id, 'str', max_length=36, min_length=2, pattern=r'^[a-zA-Z0-9]{8}-([a-zA-Z0-9]{4}-){3}[a-zA-Z0-9]{12}$|^me$'),
                    'environmentName': self._serialize.url("environment_name", environment_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'projectName': self._serialize.url("self._config.project_name", self._config.project_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                    'userId': self._serialize.url("user_id", user_id, 'str', max_length=36, min_length=2, pattern=r'^[a-zA-Z0-9]{8}-([a-zA-Z0-9]{4}-){3}[a-zA-Z0-9]{12}$|^me$'),
                    'environmentName': self._serialize.url("environment_name", environment_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ArtifactListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_environment.metadata = {'url': '/projects/{projectName}/users/{userId}/environments/{environmentName}/artifacts'}  # type: ignore

    def list_by_path(
        self,
        environment_name,  # type: str
        artifact_path,  # type: str
        user_id="me",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ArtifactListResult"]
        """Lists the artifacts for an environment at a specified path, or returns the file at the path.

        :param environment_name: The name of the environment.
        :type environment_name: str
        :param artifact_path: The path of the artifact.
        :type artifact_path: str
        :param user_id: The AAD object id of the user. If value is 'me', the identity is taken from the
         authentication context.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ArtifactListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~dev_center_dataplane_client.models.ArtifactListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ArtifactListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2022-11-11-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_path.metadata['url']  # type: ignore
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'projectName': self._serialize.url("self._config.project_name", self._config.project_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                    'userId': self._serialize.url("user_id", user_id, 'str', max_length=36, min_length=2, pattern=r'^[a-zA-Z0-9]{8}-([a-zA-Z0-9]{4}-){3}[a-zA-Z0-9]{12}$|^me$'),
                    'environmentName': self._serialize.url("environment_name", environment_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                    'artifactPath': self._serialize.url("artifact_path", artifact_path, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'projectName': self._serialize.url("self._config.project_name", self._config.project_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                    'userId': self._serialize.url("user_id", user_id, 'str', max_length=36, min_length=2, pattern=r'^[a-zA-Z0-9]{8}-([a-zA-Z0-9]{4}-){3}[a-zA-Z0-9]{12}$|^me$'),
                    'environmentName': self._serialize.url("environment_name", environment_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                    'artifactPath': self._serialize.url("artifact_path", artifact_path, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ArtifactListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_path.metadata = {'url': '/projects/{projectName}/users/{userId}/environments/{environmentName}/artifacts/{artifactPath}'}  # type: ignore
