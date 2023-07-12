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
    "palo-alto cloudngfw local-rulestack local-rule list",
)
class List(AAZCommand):
    """List LocalRulesResource resources by LocalRulestacks
    """

    _aaz_info = {
        "version": "2022-08-29",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/paloaltonetworks.cloudngfw/localrulestacks/{}/localrules", "2022-08-29"],
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
        _args_schema.local_rulestack_name = AAZStrArg(
            options=["--local-rulestack-name"],
            help="LocalRulestack resource name",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.LocalRulesListByLocalRulestacks(ctx=self.ctx)()
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

    class LocalRulesListByLocalRulestacks(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PaloAltoNetworks.Cloudngfw/localRulestacks/{localRulestackName}/localRules",
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
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.action_type = AAZStrType(
                serialized_name="actionType",
            )
            properties.applications = AAZListType()
            properties.audit_comment = AAZStrType(
                serialized_name="auditComment",
            )
            properties.category = AAZObjectType()
            properties.decryption_rule_type = AAZStrType(
                serialized_name="decryptionRuleType",
            )
            properties.description = AAZStrType()
            properties.destination = AAZObjectType()
            properties.enable_logging = AAZStrType(
                serialized_name="enableLogging",
            )
            properties.etag = AAZStrType()
            properties.inbound_inspection_certificate = AAZStrType(
                serialized_name="inboundInspectionCertificate",
            )
            properties.negate_destination = AAZStrType(
                serialized_name="negateDestination",
            )
            properties.negate_source = AAZStrType(
                serialized_name="negateSource",
            )
            properties.priority = AAZIntType(
                flags={"read_only": True},
            )
            properties.protocol = AAZStrType()
            properties.protocol_port_list = AAZListType(
                serialized_name="protocolPortList",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.rule_name = AAZStrType(
                serialized_name="ruleName",
                flags={"required": True},
            )
            properties.rule_state = AAZStrType(
                serialized_name="ruleState",
            )
            properties.source = AAZObjectType()
            properties.tags = AAZListType()

            applications = cls._schema_on_200.value.Element.properties.applications
            applications.Element = AAZStrType()

            category = cls._schema_on_200.value.Element.properties.category
            category.feeds = AAZListType(
                flags={"required": True},
            )
            category.url_custom = AAZListType(
                serialized_name="urlCustom",
                flags={"required": True},
            )

            feeds = cls._schema_on_200.value.Element.properties.category.feeds
            feeds.Element = AAZStrType()

            url_custom = cls._schema_on_200.value.Element.properties.category.url_custom
            url_custom.Element = AAZStrType()

            destination = cls._schema_on_200.value.Element.properties.destination
            destination.cidrs = AAZListType()
            destination.countries = AAZListType()
            destination.feeds = AAZListType()
            destination.fqdn_lists = AAZListType(
                serialized_name="fqdnLists",
            )
            destination.prefix_lists = AAZListType(
                serialized_name="prefixLists",
            )

            cidrs = cls._schema_on_200.value.Element.properties.destination.cidrs
            cidrs.Element = AAZStrType()

            countries = cls._schema_on_200.value.Element.properties.destination.countries
            countries.Element = AAZStrType()

            feeds = cls._schema_on_200.value.Element.properties.destination.feeds
            feeds.Element = AAZStrType()

            fqdn_lists = cls._schema_on_200.value.Element.properties.destination.fqdn_lists
            fqdn_lists.Element = AAZStrType()

            prefix_lists = cls._schema_on_200.value.Element.properties.destination.prefix_lists
            prefix_lists.Element = AAZStrType()

            protocol_port_list = cls._schema_on_200.value.Element.properties.protocol_port_list
            protocol_port_list.Element = AAZStrType()

            source = cls._schema_on_200.value.Element.properties.source
            source.cidrs = AAZListType()
            source.countries = AAZListType()
            source.feeds = AAZListType()
            source.prefix_lists = AAZListType(
                serialized_name="prefixLists",
            )

            cidrs = cls._schema_on_200.value.Element.properties.source.cidrs
            cidrs.Element = AAZStrType()

            countries = cls._schema_on_200.value.Element.properties.source.countries
            countries.Element = AAZStrType()

            feeds = cls._schema_on_200.value.Element.properties.source.feeds
            feeds.Element = AAZStrType()

            prefix_lists = cls._schema_on_200.value.Element.properties.source.prefix_lists
            prefix_lists.Element = AAZStrType()

            tags = cls._schema_on_200.value.Element.properties.tags
            tags.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.tags.Element
            _element.key = AAZStrType(
                flags={"required": True},
            )
            _element.value = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200.value.Element.system_data
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

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
