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
    "palo-alto cloudngfw global-rulestack post-rule get-counter",
)
class GetCounter(AAZCommand):
    """Get counters
    """

    _aaz_info = {
        "version": "2022-08-29",
        "resources": [
            ["mgmt-plane", "/providers/paloaltonetworks.cloudngfw/globalrulestacks/{}/postrules/{}/getcounters", "2022-08-29"],
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
        _args_schema.global_rulestack_name = AAZStrArg(
            options=["--global-rulestack-name"],
            help="GlobalRulestack resource name",
            required=True,
        )
        _args_schema.priority = AAZStrArg(
            options=["--priority"],
            help="Post Rule priority",
            required=True,
        )
        _args_schema.firewall_name = AAZStrArg(
            options=["--firewall-name"],
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PostRulesGetCounters(ctx=self.ctx)()
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

    class PostRulesGetCounters(AAZHttpOperation):
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
                "/providers/PaloAltoNetworks.Cloudngfw/globalRulestacks/{globalRulestackName}/postRules/{priority}/getCounters",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "globalRulestackName", self.ctx.args.global_rulestack_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "priority", self.ctx.args.priority,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "firewallName", self.ctx.args.firewall_name,
                ),
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
            _schema_on_200.app_seen = AAZObjectType(
                serialized_name="appSeen",
            )
            _schema_on_200.firewall_name = AAZStrType(
                serialized_name="firewallName",
            )
            _schema_on_200.hit_count = AAZIntType(
                serialized_name="hitCount",
            )
            _schema_on_200.last_updated_timestamp = AAZStrType(
                serialized_name="lastUpdatedTimestamp",
            )
            _schema_on_200.priority = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.request_timestamp = AAZStrType(
                serialized_name="requestTimestamp",
            )
            _schema_on_200.rule_list_name = AAZStrType(
                serialized_name="ruleListName",
            )
            _schema_on_200.rule_name = AAZStrType(
                serialized_name="ruleName",
                flags={"required": True},
            )
            _schema_on_200.rule_stack_name = AAZStrType(
                serialized_name="ruleStackName",
            )
            _schema_on_200.timestamp = AAZStrType()

            app_seen = cls._schema_on_200.app_seen
            app_seen.app_seen_list = AAZListType(
                serialized_name="appSeenList",
                flags={"required": True},
            )
            app_seen.count = AAZIntType(
                flags={"required": True},
            )

            app_seen_list = cls._schema_on_200.app_seen.app_seen_list
            app_seen_list.Element = AAZObjectType()

            _element = cls._schema_on_200.app_seen.app_seen_list.Element
            _element.category = AAZStrType(
                flags={"required": True},
            )
            _element.risk = AAZStrType(
                flags={"required": True},
            )
            _element.standard_ports = AAZStrType(
                serialized_name="standardPorts",
                flags={"required": True},
            )
            _element.sub_category = AAZStrType(
                serialized_name="subCategory",
                flags={"required": True},
            )
            _element.tag = AAZStrType(
                flags={"required": True},
            )
            _element.technology = AAZStrType(
                flags={"required": True},
            )
            _element.title = AAZStrType(
                flags={"required": True},
            )

            return cls._schema_on_200


class _GetCounterHelper:
    """Helper class for GetCounter"""


__all__ = ["GetCounter"]
