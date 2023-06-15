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
    "new-relic monitor show",
)
class Show(AAZCommand):
    """Get a NewRelicMonitorResource
    """

    _aaz_info = {
        "version": "2022-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/newrelic.observability/monitors/{}", "2022-07-01"],
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
            help="Name of the Monitors resource",
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
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/NewRelic.Observability/monitors/{monitorName}",
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
                    "api-version", "2022-07-01",
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
                flags={"required": True, "client_flatten": True},
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
            properties.account_creation_source = AAZStrType(
                serialized_name="accountCreationSource",
            )
            properties.liftr_resource_category = AAZStrType(
                serialized_name="liftrResourceCategory",
            )
            properties.liftr_resource_preference = AAZIntType(
                serialized_name="liftrResourcePreference",
                flags={"read_only": True},
            )
            properties.marketplace_subscription_id = AAZStrType(
                serialized_name="marketplaceSubscriptionId",
                flags={"read_only": True},
            )
            properties.marketplace_subscription_status = AAZStrType(
                serialized_name="marketplaceSubscriptionStatus",
            )
            properties.monitoring_status = AAZStrType(
                serialized_name="monitoringStatus",
            )
            properties.new_relic_account_properties = AAZObjectType(
                serialized_name="newRelicAccountProperties",
            )
            properties.org_creation_source = AAZStrType(
                serialized_name="orgCreationSource",
            )
            properties.plan_data = AAZObjectType(
                serialized_name="planData",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.user_info = AAZObjectType(
                serialized_name="userInfo",
            )

            new_relic_account_properties = cls._schema_on_200.properties.new_relic_account_properties
            new_relic_account_properties.account_info = AAZObjectType(
                serialized_name="accountInfo",
            )
            new_relic_account_properties.organization_info = AAZObjectType(
                serialized_name="organizationInfo",
            )
            new_relic_account_properties.single_sign_on_properties = AAZObjectType(
                serialized_name="singleSignOnProperties",
            )
            new_relic_account_properties.user_id = AAZStrType(
                serialized_name="userId",
            )

            account_info = cls._schema_on_200.properties.new_relic_account_properties.account_info
            account_info.account_id = AAZStrType(
                serialized_name="accountId",
            )
            account_info.ingestion_key = AAZStrType(
                serialized_name="ingestionKey",
                flags={"secret": True},
            )
            account_info.region = AAZStrType()

            organization_info = cls._schema_on_200.properties.new_relic_account_properties.organization_info
            organization_info.organization_id = AAZStrType(
                serialized_name="organizationId",
            )

            single_sign_on_properties = cls._schema_on_200.properties.new_relic_account_properties.single_sign_on_properties
            single_sign_on_properties.enterprise_app_id = AAZStrType(
                serialized_name="enterpriseAppId",
            )
            single_sign_on_properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            single_sign_on_properties.single_sign_on_state = AAZStrType(
                serialized_name="singleSignOnState",
            )
            single_sign_on_properties.single_sign_on_url = AAZStrType(
                serialized_name="singleSignOnUrl",
            )

            plan_data = cls._schema_on_200.properties.plan_data
            plan_data.billing_cycle = AAZStrType(
                serialized_name="billingCycle",
            )
            plan_data.effective_date = AAZStrType(
                serialized_name="effectiveDate",
            )
            plan_data.plan_details = AAZStrType(
                serialized_name="planDetails",
            )
            plan_data.usage_type = AAZStrType(
                serialized_name="usageType",
            )

            user_info = cls._schema_on_200.properties.user_info
            user_info.country = AAZStrType()
            user_info.email_address = AAZStrType(
                serialized_name="emailAddress",
            )
            user_info.first_name = AAZStrType(
                serialized_name="firstName",
            )
            user_info.last_name = AAZStrType(
                serialized_name="lastName",
            )
            user_info.phone_number = AAZStrType(
                serialized_name="phoneNumber",
            )

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


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
