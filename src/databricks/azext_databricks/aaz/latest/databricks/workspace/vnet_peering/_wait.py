# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "databricks workspace vnet-peering wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.databricks/workspaces/{}/virtualnetworkpeerings/{}", "2023-02-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the vnet peering.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["--workspace-name"],
            help="The name of the workspace.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                max_length=64,
                min_length=3,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VNetPeeringGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class VNetPeeringGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)
            if session.http_response.status_code in [204]:
                return self.on_204(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Databricks/workspaces/{workspaceName}/virtualNetworkPeerings/{peeringName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "peeringName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-02-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.allow_forwarded_traffic = AAZBoolType(
                serialized_name="allowForwardedTraffic",
            )
            properties.allow_gateway_transit = AAZBoolType(
                serialized_name="allowGatewayTransit",
            )
            properties.allow_virtual_network_access = AAZBoolType(
                serialized_name="allowVirtualNetworkAccess",
            )
            properties.databricks_address_space = AAZObjectType(
                serialized_name="databricksAddressSpace",
            )
            _WaitHelper._build_schema_address_space_read(properties.databricks_address_space)
            properties.databricks_virtual_network = AAZObjectType(
                serialized_name="databricksVirtualNetwork",
            )
            properties.peering_state = AAZStrType(
                serialized_name="peeringState",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.remote_address_space = AAZObjectType(
                serialized_name="remoteAddressSpace",
            )
            _WaitHelper._build_schema_address_space_read(properties.remote_address_space)
            properties.remote_virtual_network = AAZObjectType(
                serialized_name="remoteVirtualNetwork",
                flags={"required": True},
            )
            properties.use_remote_gateways = AAZBoolType(
                serialized_name="useRemoteGateways",
            )

            databricks_virtual_network = cls._schema_on_200.properties.databricks_virtual_network
            databricks_virtual_network.id = AAZStrType()

            remote_virtual_network = cls._schema_on_200.properties.remote_virtual_network
            remote_virtual_network.id = AAZStrType()

            return cls._schema_on_200

        def on_204(self, session):
            pass


class _WaitHelper:
    """Helper class for Wait"""

    _schema_address_space_read = None

    @classmethod
    def _build_schema_address_space_read(cls, _schema):
        if cls._schema_address_space_read is not None:
            _schema.address_prefixes = cls._schema_address_space_read.address_prefixes
            return

        cls._schema_address_space_read = _schema_address_space_read = AAZObjectType()

        address_space_read = _schema_address_space_read
        address_space_read.address_prefixes = AAZListType(
            serialized_name="addressPrefixes",
        )

        address_prefixes = _schema_address_space_read.address_prefixes
        address_prefixes.Element = AAZStrType()

        _schema.address_prefixes = cls._schema_address_space_read.address_prefixes


__all__ = ["Wait"]
