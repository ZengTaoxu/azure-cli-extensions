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
    "orbital spacecraft wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.orbital/spacecrafts/{}", "2022-03-01"],
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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.spacecraft_name = AAZStrArg(
            options=["-n", "--name", "--spacecraft-name"],
            help="Spacecraft ID.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.SpacecraftsGet(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class SpacecraftsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Orbital/spacecrafts/{spacecraftName}",
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
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "spacecraftName", self.ctx.args.spacecraft_name,
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
                    "api-version", "2022-03-01",
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
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
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

            properties = cls._schema_on_200.properties
            properties.links = AAZListType()
            properties.norad_id = AAZStrType(
                serialized_name="noradId",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.title_line = AAZStrType(
                serialized_name="titleLine",
            )
            properties.tle_line1 = AAZStrType(
                serialized_name="tleLine1",
            )
            properties.tle_line2 = AAZStrType(
                serialized_name="tleLine2",
            )

            links = cls._schema_on_200.properties.links
            links.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.links.Element
            _element.authorizations = AAZListType(
                flags={"read_only": True},
            )
            _element.bandwidth_m_hz = AAZFloatType(
                serialized_name="bandwidthMHz",
                flags={"required": True},
            )
            _element.center_frequency_m_hz = AAZFloatType(
                serialized_name="centerFrequencyMHz",
                flags={"required": True},
            )
            _element.direction = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.polarization = AAZStrType(
                flags={"required": True},
            )

            authorizations = cls._schema_on_200.properties.links.Element.authorizations
            authorizations.Element = AAZObjectType(
                flags={"read_only": True},
            )

            _element = cls._schema_on_200.properties.links.Element.authorizations.Element
            _element.expiration_date = AAZStrType(
                serialized_name="expirationDate",
                flags={"read_only": True},
            )
            _element.ground_station = AAZStrType(
                serialized_name="groundStation",
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


__all__ = ["Wait"]
