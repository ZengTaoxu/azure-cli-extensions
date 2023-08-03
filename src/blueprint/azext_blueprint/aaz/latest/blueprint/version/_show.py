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
    "blueprint version show",
    is_preview=True,
)
class Show(AAZCommand):
    """Get a published version of a blueprint.

    :example: Get a published management group blueprint
        az blueprint version show --management-group MyManagementGroup --blueprint-name MyBlueprint --version v2

    :example: Get a published subscription blueprint
        az blueprint version show --subscription MySubscription --blueprint-name MyBlueprint --version v2
    """

    _aaz_info = {
        "version": "2018-11-01-preview",
        "resources": [
            ["mgmt-plane", "/{resourcescope}/providers/microsoft.blueprint/blueprints/{}/versions/{}", "2018-11-01-preview"],
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
        _args_schema.blueprint_name = AAZStrArg(
            options=["--blueprint-name"],
            help="Name of the blueprint definition.",
            required=True,
        )
        _args_schema.resource_scope = AAZStrArg(
            options=["--resource-scope"],
            help="The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}').",
            required=True,
        )
        _args_schema.version_id = AAZStrArg(
            options=["--version-id"],
            help="Version of the published blueprint definition.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PublishedBlueprintsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PublishedBlueprintsGet(AAZHttpOperation):
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
                "/{resourceScope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId}",
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
                    "blueprintName", self.ctx.args.blueprint_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceScope", self.ctx.args.resource_scope,
                    skip_quote=True,
                    required=True,
                ),
                **self.serialize_url_param(
                    "versionId", self.ctx.args.version_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-11-01-preview",
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
            properties.blueprint_name = AAZStrType(
                serialized_name="blueprintName",
            )
            properties.change_notes = AAZStrType(
                serialized_name="changeNotes",
            )
            properties.description = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.parameters = AAZDictType()
            properties.resource_groups = AAZDictType(
                serialized_name="resourceGroups",
            )
            properties.status = AAZObjectType()
            properties.target_scope = AAZStrType(
                serialized_name="targetScope",
            )

            parameters = cls._schema_on_200.properties.parameters
            parameters.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.parameters.Element
            _element.allowed_values = AAZListType(
                serialized_name="allowedValues",
            )
            _element.default_value = AAZStrType(
                serialized_name="defaultValue",
            )
            _element.metadata = AAZObjectType(
                flags={"client_flatten": True},
            )
            _ShowHelper._build_schema_parameter_definition_metadata_read(_element.metadata)
            _element.type = AAZStrType(
                flags={"required": True},
            )

            allowed_values = cls._schema_on_200.properties.parameters.Element.allowed_values
            allowed_values.Element = AAZStrType()

            resource_groups = cls._schema_on_200.properties.resource_groups
            resource_groups.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.resource_groups.Element
            _element.depends_on = AAZListType(
                serialized_name="dependsOn",
            )
            _element.location = AAZStrType()
            _element.metadata = AAZObjectType(
                flags={"client_flatten": True},
            )
            _ShowHelper._build_schema_parameter_definition_metadata_read(_element.metadata)
            _element.name = AAZStrType()
            _element.tags = AAZDictType()

            depends_on = cls._schema_on_200.properties.resource_groups.Element.depends_on
            depends_on.Element = AAZStrType()

            tags = cls._schema_on_200.properties.resource_groups.Element.tags
            tags.Element = AAZStrType()

            status = cls._schema_on_200.properties.status
            status.last_modified = AAZStrType(
                serialized_name="lastModified",
                flags={"read_only": True},
            )
            status.time_created = AAZStrType(
                serialized_name="timeCreated",
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_parameter_definition_metadata_read = None

    @classmethod
    def _build_schema_parameter_definition_metadata_read(cls, _schema):
        if cls._schema_parameter_definition_metadata_read is not None:
            _schema.description = cls._schema_parameter_definition_metadata_read.description
            _schema.display_name = cls._schema_parameter_definition_metadata_read.display_name
            _schema.strong_type = cls._schema_parameter_definition_metadata_read.strong_type
            return

        cls._schema_parameter_definition_metadata_read = _schema_parameter_definition_metadata_read = AAZObjectType()

        parameter_definition_metadata_read = _schema_parameter_definition_metadata_read
        parameter_definition_metadata_read.description = AAZStrType()
        parameter_definition_metadata_read.display_name = AAZStrType(
            serialized_name="displayName",
        )
        parameter_definition_metadata_read.strong_type = AAZStrType(
            serialized_name="strongType",
        )

        _schema.description = cls._schema_parameter_definition_metadata_read.description
        _schema.display_name = cls._schema_parameter_definition_metadata_read.display_name
        _schema.strong_type = cls._schema_parameter_definition_metadata_read.strong_type


__all__ = ["Show"]
