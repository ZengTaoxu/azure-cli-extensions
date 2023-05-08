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
    "workloads monitor wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.workloads/monitors/{}", "2023-04-01"],
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
        _args_schema.monitor_name = AAZStrArg(
            options=["-n", "--name", "--monitor-name"],
            help="Name of the SAP monitor resource.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.MonitorsGet(ctx=self.ctx)()
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

    class MonitorsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/monitors/{monitorName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "monitorName", self.ctx.args.monitor_name,
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
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-04-01",
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
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.app_location = AAZStrType(
                serialized_name="appLocation",
            )
            properties.errors = AAZObjectType()
            _WaitHelper._build_schema_error_read(properties.errors)
            properties.log_analytics_workspace_arm_id = AAZStrType(
                serialized_name="logAnalyticsWorkspaceArmId",
            )
            properties.managed_resource_group_configuration = AAZObjectType(
                serialized_name="managedResourceGroupConfiguration",
            )
            properties.monitor_subnet = AAZStrType(
                serialized_name="monitorSubnet",
            )
            properties.msi_arm_id = AAZStrType(
                serialized_name="msiArmId",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.routing_preference = AAZStrType(
                serialized_name="routingPreference",
            )
            properties.storage_account_arm_id = AAZStrType(
                serialized_name="storageAccountArmId",
                flags={"read_only": True},
            )
            properties.zone_redundancy_preference = AAZStrType(
                serialized_name="zoneRedundancyPreference",
            )

            managed_resource_group_configuration = cls._schema_on_200.properties.managed_resource_group_configuration
            managed_resource_group_configuration.name = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_error_read = None

    @classmethod
    def _build_schema_error_read(cls, _schema):
        if cls._schema_error_read is not None:
            _schema.code = cls._schema_error_read.code
            _schema.details = cls._schema_error_read.details
            _schema.inner_error = cls._schema_error_read.inner_error
            _schema.message = cls._schema_error_read.message
            _schema.target = cls._schema_error_read.target
            return

        cls._schema_error_read = _schema_error_read = AAZObjectType()

        error_read = _schema_error_read
        error_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_read.details = AAZListType(
            flags={"read_only": True},
        )
        error_read.inner_error = AAZObjectType(
            serialized_name="innerError",
            flags={"read_only": True},
        )
        error_read.message = AAZStrType(
            flags={"read_only": True},
        )
        error_read.target = AAZStrType(
            flags={"read_only": True},
        )

        details = _schema_error_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_read(details.Element)

        inner_error = _schema_error_read.inner_error
        inner_error.inner_error = AAZObjectType(
            serialized_name="innerError",
        )
        cls._build_schema_error_read(inner_error.inner_error)

        _schema.code = cls._schema_error_read.code
        _schema.details = cls._schema_error_read.details
        _schema.inner_error = cls._schema_error_read.inner_error
        _schema.message = cls._schema_error_read.message
        _schema.target = cls._schema_error_read.target


__all__ = ["Wait"]
