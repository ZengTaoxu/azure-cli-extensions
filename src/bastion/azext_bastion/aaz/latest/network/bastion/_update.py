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
    "network bastion update",
    is_preview=True,
)
class Update(AAZCommand):
    """Update a Azure Bastion host machine.

    :example: Update a Azure Bastion host machine to enable native client support.
        az network bastion update --name MyBastionHost --resource-group MyResourceGroup --enable-tunneling
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/bastionhosts/{}", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

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
            help="Name of the bastion host.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.disable_copy_paste = AAZBoolArg(
            options=["--disable-copy-paste"],
            help="Disable copy and paste for all sessions on this Azure Bastion resource.",
            nullable=True,
        )
        _args_schema.enable_ip_connect = AAZBoolArg(
            options=["--enable-ip-connect"],
            help="Enable IP-based Connections on this Azure Bastion resource.",
            nullable=True,
        )
        _args_schema.enable_tunneling = AAZBoolArg(
            options=["--enable-tunneling"],
            help="Enable Native Client Support on this Azure Bastion resource.",
            nullable=True,
        )
        _args_schema.scale_units = AAZIntArg(
            options=["--scale-units"],
            help="Scale units for the Bastion Host resource with the range of [2, 50].",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=50,
                minimum=2,
            ),
        )
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            help="SKU of this Bastion Host.",
            nullable=True,
            enum={"Basic": "Basic", "Standard": "Standard"},
        )

        # define Arg Group "Parameters"

        # define Arg Group "Properties"
        return cls._args_schema

    _args_sub_resource_update = None

    @classmethod
    def _build_args_sub_resource_update(cls, _schema):
        if cls._args_sub_resource_update is not None:
            _schema.id = cls._args_sub_resource_update.id
            return

        cls._args_sub_resource_update = AAZObjectArg()

        sub_resource_update = cls._args_sub_resource_update
        sub_resource_update.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
            nullable=True,
        )

        _schema.id = cls._args_sub_resource_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.BastionHostsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.BastionHostsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class BastionHostsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/bastionHosts/{bastionHostName}",
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
                    "bastionHostName", self.ctx.args.name,
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
                    "api-version", "2022-01-01",
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
            _UpdateHelper._build_schema_bastion_host_read(cls._schema_on_200)

            return cls._schema_on_200

    class BastionHostsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/bastionHosts/{bastionHostName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "bastionHostName", self.ctx.args.name,
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
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_bastion_host_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("disableCopyPaste", AAZBoolType, ".disable_copy_paste")
                properties.set_prop("enableIpConnect", AAZBoolType, ".enable_ip_connect")
                properties.set_prop("enableTunneling", AAZBoolType, ".enable_tunneling")
                properties.set_prop("scaleUnits", AAZIntType, ".scale_units")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".sku")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_sub_resource_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_bastion_host_read = None

    @classmethod
    def _build_schema_bastion_host_read(cls, _schema):
        if cls._schema_bastion_host_read is not None:
            _schema.etag = cls._schema_bastion_host_read.etag
            _schema.id = cls._schema_bastion_host_read.id
            _schema.location = cls._schema_bastion_host_read.location
            _schema.name = cls._schema_bastion_host_read.name
            _schema.properties = cls._schema_bastion_host_read.properties
            _schema.sku = cls._schema_bastion_host_read.sku
            _schema.tags = cls._schema_bastion_host_read.tags
            _schema.type = cls._schema_bastion_host_read.type
            return

        cls._schema_bastion_host_read = _schema_bastion_host_read = AAZObjectType()

        bastion_host_read = _schema_bastion_host_read
        bastion_host_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        bastion_host_read.id = AAZStrType()
        bastion_host_read.location = AAZStrType()
        bastion_host_read.name = AAZStrType(
            flags={"read_only": True},
        )
        bastion_host_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        bastion_host_read.sku = AAZObjectType()
        bastion_host_read.tags = AAZDictType()
        bastion_host_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_bastion_host_read.properties
        properties.disable_copy_paste = AAZBoolType(
            serialized_name="disableCopyPaste",
        )
        properties.dns_name = AAZStrType(
            serialized_name="dnsName",
        )
        properties.enable_file_copy = AAZBoolType(
            serialized_name="enableFileCopy",
        )
        properties.enable_ip_connect = AAZBoolType(
            serialized_name="enableIpConnect",
        )
        properties.enable_shareable_link = AAZBoolType(
            serialized_name="enableShareableLink",
        )
        properties.enable_tunneling = AAZBoolType(
            serialized_name="enableTunneling",
        )
        properties.ip_configurations = AAZListType(
            serialized_name="ipConfigurations",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.scale_units = AAZIntType(
            serialized_name="scaleUnits",
        )

        ip_configurations = _schema_bastion_host_read.properties.ip_configurations
        ip_configurations.Element = AAZObjectType()

        _element = _schema_bastion_host_read.properties.ip_configurations.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_bastion_host_read.properties.ip_configurations.Element.properties
        properties.private_ip_allocation_method = AAZStrType(
            serialized_name="privateIPAllocationMethod",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_ip_address = AAZObjectType(
            serialized_name="publicIPAddress",
            flags={"required": True},
        )
        cls._build_schema_sub_resource_read(properties.public_ip_address)
        properties.subnet = AAZObjectType(
            flags={"required": True},
        )
        cls._build_schema_sub_resource_read(properties.subnet)

        sku = _schema_bastion_host_read.sku
        sku.name = AAZStrType()

        tags = _schema_bastion_host_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_bastion_host_read.etag
        _schema.id = cls._schema_bastion_host_read.id
        _schema.location = cls._schema_bastion_host_read.location
        _schema.name = cls._schema_bastion_host_read.name
        _schema.properties = cls._schema_bastion_host_read.properties
        _schema.sku = cls._schema_bastion_host_read.sku
        _schema.tags = cls._schema_bastion_host_read.tags
        _schema.type = cls._schema_bastion_host_read.type

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Update"]
