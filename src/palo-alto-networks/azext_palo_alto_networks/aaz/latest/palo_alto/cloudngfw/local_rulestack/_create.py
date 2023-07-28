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
    "palo-alto cloudngfw local-rulestack create",
)
class Create(AAZCommand):
    """Create a LocalRulestackResource

    :example: Create a LocalRulestackResource
        az palo-alto cloudngfw local-rulestack create -g MyResourceGroup -n MyLocalRulestacks --identity type=None --location eastus --default-mode IPS --description "local rulestacks" --min-app-id-version "8595-7473" --scope "LOCAL" --security-services vulnerability-profile=BestPractice anti-spyware-profile=BestPractice anti-virus-profile=BestPractice url-filtering-profile=BestPractice file-blocking-profile=BestPractice dns-subscription=BestPractice
    """

    _aaz_info = {
        "version": "2022-08-29",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/paloaltonetworks.cloudngfw/localrulestacks/{}", "2022-08-29"],
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
        _args_schema.local_rulestack_name = AAZStrArg(
            options=["-n", "--name", "--local-rulestack-name"],
            help="LocalRulestack resource name",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.associated_subscriptions = AAZListArg(
            options=["--associated-subs", "--associated-subscriptions"],
            arg_group="Properties",
            help="subscription scope of global rulestack",
        )
        _args_schema.default_mode = AAZStrArg(
            options=["--default-mode"],
            arg_group="Properties",
            help="Mode for default rules creation",
            enum={"FIREWALL": "FIREWALL", "IPS": "IPS", "NONE": "NONE"},
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="rulestack description",
        )
        _args_schema.min_app_id_version = AAZStrArg(
            options=["--min-app-id-version"],
            arg_group="Properties",
            help="minimum version",
        )
        _args_schema.pan_etag = AAZStrArg(
            options=["--pan-etag"],
            arg_group="Properties",
            help="PanEtag info",
        )
        _args_schema.pan_location = AAZStrArg(
            options=["--pan-location"],
            arg_group="Properties",
            help="Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks",
        )
        _args_schema.scope = AAZStrArg(
            options=["--scope"],
            arg_group="Properties",
            help="Rulestack Type",
            enum={"GLOBAL": "GLOBAL", "LOCAL": "LOCAL"},
        )
        _args_schema.security_services = AAZObjectArg(
            options=["--security-services"],
            arg_group="Properties",
            help="Security Profile",
        )

        associated_subscriptions = cls._args_schema.associated_subscriptions
        associated_subscriptions.Element = AAZStrArg()

        security_services = cls._args_schema.security_services
        security_services.anti_spyware_profile = AAZStrArg(
            options=["anti-spyware-profile"],
            help="Anti spyware Profile data",
        )
        security_services.anti_virus_profile = AAZStrArg(
            options=["anti-virus-profile"],
            help="anti virus profile data",
        )
        security_services.dns_subscription = AAZStrArg(
            options=["dns-subscription"],
            help="DNS Subscription profile data",
        )
        security_services.file_blocking_profile = AAZStrArg(
            options=["file-blocking-profile"],
            help="File blocking profile data",
        )
        security_services.outbound_trust_certificate = AAZStrArg(
            options=["outbound-trust-certificate"],
            help="Trusted Egress Decryption profile data",
        )
        security_services.outbound_un_trust_certificate = AAZStrArg(
            options=["outbound-un-trust-certificate"],
            help="Untrusted Egress Decryption profile data",
        )
        security_services.url_filtering_profile = AAZStrArg(
            options=["url-filtering-profile"],
            help="URL filtering profile data",
        )
        security_services.vulnerability_profile = AAZStrArg(
            options=["vulnerability-profile"],
            help="IPs Vulnerability Profile Data",
        )

        # define Arg Group "Resource"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Resource",
            help="The managed service identities assigned to this resource.",
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Resource",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Resource",
            help="Resource tags.",
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="The type of managed identity assigned to this resource.",
            required=True,
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned,UserAssigned": "SystemAssigned,UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The identities assigned to this resource by the user.",
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg()

        _element = cls._args_schema.identity.user_assigned_identities.Element
        _element.client_id = AAZStrArg(
            options=["client-id"],
            help="The active directory client identifier for this principal.",
        )
        _element.principal_id = AAZStrArg(
            options=["principal-id"],
            help="The active directory identifier for this principal.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.LocalRulestacksCreateOrUpdate(ctx=self.ctx)()
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

    class LocalRulestacksCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PaloAltoNetworks.Cloudngfw/localRulestacks/{localRulestackName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "localRulestackName", self.ctx.args.local_rulestack_name,
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
                    "api-version", "2022-08-29",
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
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".identity.userAssignedIdentities{}")
            if _elements is not None:
                _elements.set_prop("clientId", AAZStrType, ".client_id")
                _elements.set_prop("principalId", AAZStrType, ".principal_id")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("associatedSubscriptions", AAZListType, ".associated_subscriptions")
                properties.set_prop("defaultMode", AAZStrType, ".default_mode")
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("minAppIdVersion", AAZStrType, ".min_app_id_version")
                properties.set_prop("panEtag", AAZStrType, ".pan_etag")
                properties.set_prop("panLocation", AAZStrType, ".pan_location")
                properties.set_prop("scope", AAZStrType, ".scope")
                properties.set_prop("securityServices", AAZObjectType, ".security_services")

            associated_subscriptions = _builder.get(".properties.associatedSubscriptions")
            if associated_subscriptions is not None:
                associated_subscriptions.set_elements(AAZStrType, ".")

            security_services = _builder.get(".properties.securityServices")
            if security_services is not None:
                security_services.set_prop("antiSpywareProfile", AAZStrType, ".anti_spyware_profile")
                security_services.set_prop("antiVirusProfile", AAZStrType, ".anti_virus_profile")
                security_services.set_prop("dnsSubscription", AAZStrType, ".dns_subscription")
                security_services.set_prop("fileBlockingProfile", AAZStrType, ".file_blocking_profile")
                security_services.set_prop("outboundTrustCertificate", AAZStrType, ".outbound_trust_certificate")
                security_services.set_prop("outboundUnTrustCertificate", AAZStrType, ".outbound_un_trust_certificate")
                security_services.set_prop("urlFilteringProfile", AAZStrType, ".url_filtering_profile")
                security_services.set_prop("vulnerabilityProfile", AAZStrType, ".vulnerability_profile")

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
            _schema_on_200_201.identity = AAZObjectType()
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200_201.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200_201.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200_201.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
            )

            properties = cls._schema_on_200_201.properties
            properties.associated_subscriptions = AAZListType(
                serialized_name="associatedSubscriptions",
            )
            properties.default_mode = AAZStrType(
                serialized_name="defaultMode",
            )
            properties.description = AAZStrType()
            properties.min_app_id_version = AAZStrType(
                serialized_name="minAppIdVersion",
            )
            properties.pan_etag = AAZStrType(
                serialized_name="panEtag",
            )
            properties.pan_location = AAZStrType(
                serialized_name="panLocation",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.scope = AAZStrType()
            properties.security_services = AAZObjectType(
                serialized_name="securityServices",
            )

            associated_subscriptions = cls._schema_on_200_201.properties.associated_subscriptions
            associated_subscriptions.Element = AAZStrType()

            security_services = cls._schema_on_200_201.properties.security_services
            security_services.anti_spyware_profile = AAZStrType(
                serialized_name="antiSpywareProfile",
            )
            security_services.anti_virus_profile = AAZStrType(
                serialized_name="antiVirusProfile",
            )
            security_services.dns_subscription = AAZStrType(
                serialized_name="dnsSubscription",
            )
            security_services.file_blocking_profile = AAZStrType(
                serialized_name="fileBlockingProfile",
            )
            security_services.outbound_trust_certificate = AAZStrType(
                serialized_name="outboundTrustCertificate",
            )
            security_services.outbound_un_trust_certificate = AAZStrType(
                serialized_name="outboundUnTrustCertificate",
            )
            security_services.url_filtering_profile = AAZStrType(
                serialized_name="urlFilteringProfile",
            )
            security_services.vulnerability_profile = AAZStrType(
                serialized_name="vulnerabilityProfile",
            )

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


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
