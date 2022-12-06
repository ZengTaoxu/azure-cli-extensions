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
    "databricks workspace create",
)
class Create(AAZCommand):
    """Create a new workspace.

    :example: Create a workspace
        az databricks workspace create --resource-group MyResourceGroup --name MyWorkspace --location westus --sku standard

    :example: Create a workspace with managed identity for storage account
        az databricks workspace create --resource-group MyResourceGroup --name MyWorkspace --location eastus2euap --sku premium --prepare-encryption
    """

    _aaz_info = {
        "version": "2022-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.databricks/workspaces/{}", "2022-04-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the workspace.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                max_length=64,
                min_length=3,
            ),
        )
        _args_schema.location = AAZResourceLocationArg(
            help="Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.managed_resource_group = AAZStrArg(
            options=["--managed-resource-group"],
            help="The managed resource group to create. It can be either a name or a resource ID.",
            # required=True,
        )
        _args_schema.enable_no_public_ip = AAZBoolArg(
            options=["--enable-no-public-ip"],
            help="Flag to enable the no public ip feature.",
        )
        _args_schema.prepare_encryption = AAZBoolArg(
            options=["--prepare-encryption"],
            help="Flag to enable the Managed Identity for managed storage account to prepare for CMK encryption.",
        )
        _args_schema.require_infrastructure_encryption = AAZBoolArg(
            options=["--require-infrastructure-encryption"],
            help="Flag to enable the DBFS root file system with secondary layer of encryption with platform managed keys for data at rest.",
        )
        _args_schema.public_network_access = AAZStrArg(
            options=["--public-network-access"],
            help="The configuration to set whether network access from public internet to the endpoints are allowed. Allowed values: Disabled, Enabled.",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.required_nsg_rules = AAZStrArg(
            options=["--required-nsg-rules"],
            help="The type of Nsg rule for internal use only.  Allowed values: AllRules, NoAzureDatabricksRules, NoAzureServiceRules.",
            enum={"AllRules": "AllRules", "NoAzureDatabricksRules": "NoAzureDatabricksRules", "NoAzureServiceRules": "NoAzureServiceRules"},
        )
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            help="The SKU tier name.  Allowed values: premium, standard, trial.",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Custom VNET"

        _args_schema = cls._args_schema
        _args_schema.private_subnet = AAZStrArg(
            options=["--private-subnet"],
            arg_group="Custom VNET",
            help="The name of a Private Subnet within the Virtual Network.",
        )
        _args_schema.public_subnet = AAZStrArg(
            options=["--public-subnet"],
            arg_group="Custom VNET",
            help="The name of a Public Subnet within the Virtual Network.",
        )
        _args_schema.vnet = AAZResourceIdArg(
            options=["--vnet"],
            arg_group="Custom VNET",
            help="Virtual Network name or resource ID.",
            fmt=AAZResourceIdArgFormat(
                template="/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.Network/virtualNetworks/{}"
            )
        )

        # define Arg Group "Parameters"

        # define Arg Group "Properties"

        # define Arg Group "Sku"
        return cls._args_schema

    _args_workspace_custom_string_parameter_create = None

    @classmethod
    def _build_args_workspace_custom_string_parameter_create(cls, _schema):
        if cls._args_workspace_custom_string_parameter_create is not None:
            _schema.value = cls._args_workspace_custom_string_parameter_create.value
            return

        cls._args_workspace_custom_string_parameter_create = AAZObjectArg()

        workspace_custom_string_parameter_create = cls._args_workspace_custom_string_parameter_create
        workspace_custom_string_parameter_create.value = AAZStrArg(
            options=["value"],
            help="The value which should be used for this field.",
            required=True,
        )

        _schema.value = cls._args_workspace_custom_string_parameter_create.value

    def _execute_operations(self):
        self.pre_operations()
        yield self.WorkspacesCreateOrUpdate(ctx=self.ctx)()
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

    class WorkspacesCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Databricks/workspaces/{workspaceName}",
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
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-04-01-preview",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("managedResourceGroupId", AAZStrType, ".managed_resource_group", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("parameters", AAZObjectType)
                properties.set_prop("publicNetworkAccess", AAZStrType, ".public_network_access")
                properties.set_prop("requiredNsgRules", AAZStrType, ".required_nsg_rules")

            parameters = _builder.get(".properties.parameters")
            if parameters is not None:
                parameters.set_prop("customPrivateSubnetName", AAZObjectType)
                parameters.set_prop("customPublicSubnetName", AAZObjectType)
                parameters.set_prop("customVirtualNetworkId", AAZObjectType)
                parameters.set_prop("enableNoPublicIp", AAZObjectType)
                parameters.set_prop("prepareEncryption", AAZObjectType)
                parameters.set_prop("requireInfrastructureEncryption", AAZObjectType)

            custom_private_subnet_name = _builder.get(".properties.parameters.customPrivateSubnetName")
            if custom_private_subnet_name is not None:
                custom_private_subnet_name.set_prop("value", AAZStrType, ".private_subnet", typ_kwargs={"flags": {"required": True}})

            custom_public_subnet_name = _builder.get(".properties.parameters.customPublicSubnetName")
            if custom_public_subnet_name is not None:
                custom_public_subnet_name.set_prop("value", AAZStrType, ".public_subnet", typ_kwargs={"flags": {"required": True}})

            custom_virtual_network_id = _builder.get(".properties.parameters.customVirtualNetworkId")
            if custom_virtual_network_id is not None:
                custom_virtual_network_id.set_prop("value", AAZStrType, ".vnet", typ_kwargs={"flags": {"required": True}})

            enable_no_public_ip = _builder.get(".properties.parameters.enableNoPublicIp")
            if enable_no_public_ip is not None:
                enable_no_public_ip.set_prop("value", AAZBoolType, ".enable_no_public_ip", typ_kwargs={"flags": {"required": True}})

            prepare_encryption = _builder.get(".properties.parameters.prepareEncryption")
            if prepare_encryption is not None:
                prepare_encryption.set_prop("value", AAZBoolType, ".prepare_encryption", typ_kwargs={"flags": {"required": True}})

            require_infrastructure_encryption = _builder.get(".properties.parameters.requireInfrastructureEncryption")
            if require_infrastructure_encryption is not None:
                require_infrastructure_encryption.set_prop("value", AAZBoolType, ".require_infrastructure_encryption", typ_kwargs={"flags": {"required": True}})

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".sku", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

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

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.sku = AAZObjectType()
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.authorizations = AAZListType()
            properties.created_by = AAZObjectType(
                serialized_name="createdBy",
            )
            _build_schema_created_by_read(properties.created_by)
            properties.created_date_time = AAZStrType(
                serialized_name="createdDateTime",
                flags={"read_only": True},
            )
            properties.disk_encryption_set_id = AAZStrType(
                serialized_name="diskEncryptionSetId",
            )
            properties.encryption = AAZObjectType()
            properties.managed_disk_identity = AAZObjectType(
                serialized_name="managedDiskIdentity",
            )
            _build_schema_managed_identity_configuration_read(properties.managed_disk_identity)
            properties.managed_resource_group_id = AAZStrType(
                serialized_name="managedResourceGroupId",
                flags={"required": True},
            )
            properties.parameters = AAZObjectType()
            properties.private_endpoint_connections = AAZListType(
                serialized_name="privateEndpointConnections",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_network_access = AAZStrType(
                serialized_name="publicNetworkAccess",
            )
            properties.required_nsg_rules = AAZStrType(
                serialized_name="requiredNsgRules",
            )
            properties.storage_account_identity = AAZObjectType(
                serialized_name="storageAccountIdentity",
            )
            _build_schema_managed_identity_configuration_read(properties.storage_account_identity)
            properties.ui_definition_uri = AAZStrType(
                serialized_name="uiDefinitionUri",
            )
            properties.updated_by = AAZObjectType(
                serialized_name="updatedBy",
            )
            _build_schema_created_by_read(properties.updated_by)
            properties.workspace_id = AAZStrType(
                serialized_name="workspaceId",
                flags={"read_only": True},
            )
            properties.workspace_url = AAZStrType(
                serialized_name="workspaceUrl",
                flags={"read_only": True},
            )

            authorizations = cls._schema_on_200_201.properties.authorizations
            authorizations.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.authorizations.Element
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"required": True},
            )
            _element.role_definition_id = AAZStrType(
                serialized_name="roleDefinitionId",
                flags={"required": True},
            )

            encryption = cls._schema_on_200_201.properties.encryption
            encryption.entities = AAZObjectType(
                flags={"required": True},
            )

            entities = cls._schema_on_200_201.properties.encryption.entities
            entities.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            entities.managed_services = AAZObjectType(
                serialized_name="managedServices",
            )

            managed_disk = cls._schema_on_200_201.properties.encryption.entities.managed_disk
            managed_disk.key_source = AAZStrType(
                serialized_name="keySource",
                flags={"required": True},
            )
            managed_disk.key_vault_properties = AAZObjectType(
                serialized_name="keyVaultProperties",
                flags={"required": True},
            )
            managed_disk.rotation_to_latest_key_version_enabled = AAZBoolType(
                serialized_name="rotationToLatestKeyVersionEnabled",
            )

            key_vault_properties = cls._schema_on_200_201.properties.encryption.entities.managed_disk.key_vault_properties
            key_vault_properties.key_name = AAZStrType(
                serialized_name="keyName",
                flags={"required": True},
            )
            key_vault_properties.key_vault_uri = AAZStrType(
                serialized_name="keyVaultUri",
                flags={"required": True},
            )
            key_vault_properties.key_version = AAZStrType(
                serialized_name="keyVersion",
                flags={"required": True},
            )

            managed_services = cls._schema_on_200_201.properties.encryption.entities.managed_services
            managed_services.key_source = AAZStrType(
                serialized_name="keySource",
                flags={"required": True},
            )
            managed_services.key_vault_properties = AAZObjectType(
                serialized_name="keyVaultProperties",
            )

            key_vault_properties = cls._schema_on_200_201.properties.encryption.entities.managed_services.key_vault_properties
            key_vault_properties.key_name = AAZStrType(
                serialized_name="keyName",
                flags={"required": True},
            )
            key_vault_properties.key_vault_uri = AAZStrType(
                serialized_name="keyVaultUri",
                flags={"required": True},
            )
            key_vault_properties.key_version = AAZStrType(
                serialized_name="keyVersion",
                flags={"required": True},
            )

            parameters = cls._schema_on_200_201.properties.parameters
            parameters.aml_workspace_id = AAZObjectType(
                serialized_name="amlWorkspaceId",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.aml_workspace_id)
            parameters.custom_private_subnet_name = AAZObjectType(
                serialized_name="customPrivateSubnetName",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.custom_private_subnet_name)
            parameters.custom_public_subnet_name = AAZObjectType(
                serialized_name="customPublicSubnetName",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.custom_public_subnet_name)
            parameters.custom_virtual_network_id = AAZObjectType(
                serialized_name="customVirtualNetworkId",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.custom_virtual_network_id)
            parameters.enable_no_public_ip = AAZObjectType(
                serialized_name="enableNoPublicIp",
            )
            _build_schema_workspace_custom_boolean_parameter_read(parameters.enable_no_public_ip)
            parameters.encryption = AAZObjectType()
            parameters.load_balancer_backend_pool_name = AAZObjectType(
                serialized_name="loadBalancerBackendPoolName",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.load_balancer_backend_pool_name)
            parameters.load_balancer_id = AAZObjectType(
                serialized_name="loadBalancerId",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.load_balancer_id)
            parameters.nat_gateway_name = AAZObjectType(
                serialized_name="natGatewayName",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.nat_gateway_name)
            parameters.prepare_encryption = AAZObjectType(
                serialized_name="prepareEncryption",
            )
            _build_schema_workspace_custom_boolean_parameter_read(parameters.prepare_encryption)
            parameters.public_ip_name = AAZObjectType(
                serialized_name="publicIpName",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.public_ip_name)
            parameters.require_infrastructure_encryption = AAZObjectType(
                serialized_name="requireInfrastructureEncryption",
            )
            _build_schema_workspace_custom_boolean_parameter_read(parameters.require_infrastructure_encryption)
            parameters.resource_tags = AAZObjectType(
                serialized_name="resourceTags",
            )
            parameters.storage_account_name = AAZObjectType(
                serialized_name="storageAccountName",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.storage_account_name)
            parameters.storage_account_sku_name = AAZObjectType(
                serialized_name="storageAccountSkuName",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.storage_account_sku_name)
            parameters.vnet_address_prefix = AAZObjectType(
                serialized_name="vnetAddressPrefix",
            )
            _build_schema_workspace_custom_string_parameter_read(parameters.vnet_address_prefix)

            encryption = cls._schema_on_200_201.properties.parameters.encryption
            encryption.type = AAZStrType(
                flags={"read_only": True},
            )
            encryption.value = AAZObjectType()

            value = cls._schema_on_200_201.properties.parameters.encryption.value
            value.key_name = AAZStrType(
                serialized_name="KeyName",
            )
            value.key_source = AAZStrType(
                serialized_name="keySource",
            )
            value.keyvaulturi = AAZStrType()
            value.keyversion = AAZStrType()

            resource_tags = cls._schema_on_200_201.properties.parameters.resource_tags
            resource_tags.type = AAZStrType(
                flags={"read_only": True},
            )

            private_endpoint_connections = cls._schema_on_200_201.properties.private_endpoint_connections
            private_endpoint_connections.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.private_endpoint_connections.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties.private_endpoint_connections.Element.properties
            properties.private_endpoint = AAZObjectType(
                serialized_name="privateEndpoint",
            )
            properties.private_link_service_connection_state = AAZObjectType(
                serialized_name="privateLinkServiceConnectionState",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            private_endpoint = cls._schema_on_200_201.properties.private_endpoint_connections.Element.properties.private_endpoint
            private_endpoint.id = AAZStrType(
                flags={"read_only": True},
            )

            private_link_service_connection_state = cls._schema_on_200_201.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
            private_link_service_connection_state.action_required = AAZStrType(
                serialized_name="actionRequired",
            )
            private_link_service_connection_state.description = AAZStrType()
            private_link_service_connection_state.status = AAZStrType(
                flags={"required": True},
            )

            sku = cls._schema_on_200_201.sku
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.tier = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
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

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


def _build_schema_workspace_custom_string_parameter_create(_builder):
    if _builder is None:
        return
    _builder.set_prop("value", AAZStrType, ".value", typ_kwargs={"flags": {"required": True}})


_schema_created_by_read = None


def _build_schema_created_by_read(_schema):
    global _schema_created_by_read
    if _schema_created_by_read is not None:
        _schema.application_id = _schema_created_by_read.application_id
        _schema.oid = _schema_created_by_read.oid
        _schema.puid = _schema_created_by_read.puid
        return

    _schema_created_by_read = AAZObjectType()

    created_by_read = _schema_created_by_read
    created_by_read.application_id = AAZStrType(
        serialized_name="applicationId",
        flags={"read_only": True},
    )
    created_by_read.oid = AAZStrType(
        flags={"read_only": True},
    )
    created_by_read.puid = AAZStrType(
        flags={"read_only": True},
    )

    _schema.application_id = _schema_created_by_read.application_id
    _schema.oid = _schema_created_by_read.oid
    _schema.puid = _schema_created_by_read.puid


_schema_managed_identity_configuration_read = None


def _build_schema_managed_identity_configuration_read(_schema):
    global _schema_managed_identity_configuration_read
    if _schema_managed_identity_configuration_read is not None:
        _schema.principal_id = _schema_managed_identity_configuration_read.principal_id
        _schema.tenant_id = _schema_managed_identity_configuration_read.tenant_id
        _schema.type = _schema_managed_identity_configuration_read.type
        return

    _schema_managed_identity_configuration_read = AAZObjectType()

    managed_identity_configuration_read = _schema_managed_identity_configuration_read
    managed_identity_configuration_read.principal_id = AAZStrType(
        serialized_name="principalId",
        flags={"read_only": True},
    )
    managed_identity_configuration_read.tenant_id = AAZStrType(
        serialized_name="tenantId",
        flags={"read_only": True},
    )
    managed_identity_configuration_read.type = AAZStrType(
        flags={"read_only": True},
    )

    _schema.principal_id = _schema_managed_identity_configuration_read.principal_id
    _schema.tenant_id = _schema_managed_identity_configuration_read.tenant_id
    _schema.type = _schema_managed_identity_configuration_read.type


_schema_workspace_custom_boolean_parameter_read = None


def _build_schema_workspace_custom_boolean_parameter_read(_schema):
    global _schema_workspace_custom_boolean_parameter_read
    if _schema_workspace_custom_boolean_parameter_read is not None:
        _schema.type = _schema_workspace_custom_boolean_parameter_read.type
        _schema.value = _schema_workspace_custom_boolean_parameter_read.value
        return

    _schema_workspace_custom_boolean_parameter_read = AAZObjectType()

    workspace_custom_boolean_parameter_read = _schema_workspace_custom_boolean_parameter_read
    workspace_custom_boolean_parameter_read.type = AAZStrType(
        flags={"read_only": True},
    )
    workspace_custom_boolean_parameter_read.value = AAZBoolType(
        flags={"required": True},
    )

    _schema.type = _schema_workspace_custom_boolean_parameter_read.type
    _schema.value = _schema_workspace_custom_boolean_parameter_read.value


_schema_workspace_custom_string_parameter_read = None


def _build_schema_workspace_custom_string_parameter_read(_schema):
    global _schema_workspace_custom_string_parameter_read
    if _schema_workspace_custom_string_parameter_read is not None:
        _schema.type = _schema_workspace_custom_string_parameter_read.type
        _schema.value = _schema_workspace_custom_string_parameter_read.value
        return

    _schema_workspace_custom_string_parameter_read = AAZObjectType()

    workspace_custom_string_parameter_read = _schema_workspace_custom_string_parameter_read
    workspace_custom_string_parameter_read.type = AAZStrType(
        flags={"read_only": True},
    )
    workspace_custom_string_parameter_read.value = AAZStrType(
        flags={"required": True},
    )

    _schema.type = _schema_workspace_custom_string_parameter_read.type
    _schema.value = _schema_workspace_custom_string_parameter_read.value


__all__ = ["Create"]
