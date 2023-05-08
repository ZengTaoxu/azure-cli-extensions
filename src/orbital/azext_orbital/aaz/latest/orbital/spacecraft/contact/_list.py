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
    "orbital spacecraft contact list",
)
class List(AAZCommand):
    """List contacts by spacecraft.

    :example: List Contacts
        az orbital spacecraft contact list -g <resource-group> --spacecraft-name <spacecraft-name>
    """

    _aaz_info = {
        "version": "2022-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.orbital/spacecrafts/{}/contacts", "2022-03-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

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
            options=["--spacecraft-name"],
            help="Spacecraft ID.",
            required=True,
        )
        _args_schema.skiptoken = AAZStrArg(
            options=["--skiptoken"],
            help="An opaque string that the resource provider uses to skip over previously-returned results. This is used when a previous list operation call returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.ContactsList(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ContactsList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Orbital/spacecrafts/{spacecraftName}/contacts",
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
                    "$skiptoken", self.ctx.args.skiptoken,
                ),
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.antenna_configuration = AAZObjectType(
                serialized_name="antennaConfiguration",
                flags={"read_only": True},
            )
            properties.contact_profile = AAZObjectType(
                serialized_name="contactProfile",
                flags={"required": True},
            )
            properties.end_azimuth_degrees = AAZFloatType(
                serialized_name="endAzimuthDegrees",
                flags={"read_only": True},
            )
            properties.end_elevation_degrees = AAZFloatType(
                serialized_name="endElevationDegrees",
                flags={"read_only": True},
            )
            properties.error_message = AAZStrType(
                serialized_name="errorMessage",
                flags={"read_only": True},
            )
            properties.ground_station_name = AAZStrType(
                serialized_name="groundStationName",
                flags={"required": True},
            )
            properties.maximum_elevation_degrees = AAZFloatType(
                serialized_name="maximumElevationDegrees",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.reservation_end_time = AAZStrType(
                serialized_name="reservationEndTime",
                flags={"required": True},
            )
            properties.reservation_start_time = AAZStrType(
                serialized_name="reservationStartTime",
                flags={"required": True},
            )
            properties.rx_end_time = AAZStrType(
                serialized_name="rxEndTime",
                flags={"read_only": True},
            )
            properties.rx_start_time = AAZStrType(
                serialized_name="rxStartTime",
                flags={"read_only": True},
            )
            properties.start_azimuth_degrees = AAZFloatType(
                serialized_name="startAzimuthDegrees",
                flags={"read_only": True},
            )
            properties.start_elevation_degrees = AAZFloatType(
                serialized_name="startElevationDegrees",
                flags={"read_only": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.tx_end_time = AAZStrType(
                serialized_name="txEndTime",
                flags={"read_only": True},
            )
            properties.tx_start_time = AAZStrType(
                serialized_name="txStartTime",
                flags={"read_only": True},
            )

            antenna_configuration = cls._schema_on_200.value.Element.properties.antenna_configuration
            antenna_configuration.destination_ip = AAZStrType(
                serialized_name="destinationIp",
                flags={"read_only": True},
            )
            antenna_configuration.source_ips = AAZListType(
                serialized_name="sourceIps",
                flags={"read_only": True},
            )

            source_ips = cls._schema_on_200.value.Element.properties.antenna_configuration.source_ips
            source_ips.Element = AAZStrType(
                flags={"read_only": True},
            )

            contact_profile = cls._schema_on_200.value.Element.properties.contact_profile
            contact_profile.id = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
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

            return cls._schema_on_200


__all__ = ["List"]
