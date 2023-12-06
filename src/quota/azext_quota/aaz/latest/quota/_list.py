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
    "quota list",
)
class List(AAZCommand):
    """List current quota limits of all resources for the specified scope.

    :example: List quota limit for compute
        az quota list --scope /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Compute/locations/eastus

    :example: List quota limit for network
        az quota list --scope /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Network/locations/eastus

    :example: List quota limit machine learning service
        az quota list --scope /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.MachineLearningServices/locations/eastus
    """

    _aaz_info = {
        "version": "2023-02-01",
        "resources": [
            ["mgmt-plane", "/{scope}/providers/microsoft.quota/quotas", "2023-02-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

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
        _args_schema.scope = AAZStrArg(
            options=["--scope"],
            help="The target azure resource URI.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.QuotaList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class QuotaList(AAZHttpOperation):
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
                "/{scope}/providers/Microsoft.Quota/quotas",
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
                    "scope", self.ctx.args.scope,
                    skip_quote=True,
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.is_quota_applicable = AAZBoolType(
                serialized_name="isQuotaApplicable",
                flags={"read_only": True},
            )
            properties.limit = AAZObjectType()
            properties.name = AAZObjectType()
            properties.properties = AAZFreeFormDictType()
            properties.quota_period = AAZStrType(
                serialized_name="quotaPeriod",
                flags={"read_only": True},
            )
            properties.resource_type = AAZStrType(
                serialized_name="resourceType",
            )
            properties.unit = AAZStrType(
                flags={"read_only": True},
            )

            limit = cls._schema_on_200.value.Element.properties.limit
            limit.limit_object_type = AAZStrType(
                serialized_name="limitObjectType",
                flags={"required": True},
            )

            disc_limit_value = cls._schema_on_200.value.Element.properties.limit.discriminate_by("limit_object_type", "LimitValue")
            disc_limit_value.limit_type = AAZStrType(
                serialized_name="limitType",
            )
            disc_limit_value.value = AAZIntType(
                flags={"required": True},
            )

            name = cls._schema_on_200.value.Element.properties.name
            name.localized_value = AAZStrType(
                serialized_name="localizedValue",
                flags={"read_only": True},
            )
            name.value = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
