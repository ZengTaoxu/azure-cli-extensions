# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals option_length_too_long

from azure.cli.core.commands import CliCommandType
from azext_network_manager._client_factory import (
    cf_networkmanager, cf_networkmanagercommit, cf_networkmanagerdeploymentstatus,
    cf_connectivityconfiguration, cf_networkgroup, cf_userrule,
    cf_userrulecollection, cf_adminrule, cf_adminrulecollection, cf_securityadminconfiguration,
    cf_securityuserconfiguration, cf_activesecurityuserrule,
    cf_scopeconnection, cf_staticmembers, cf_listeffectivevirtualnetwork,
    cf_subscriptionconnection, cf_managementgroupconnection, cf_effectivevirtualnetwork)


def load_command_table(self, _):
    network_networkmanager = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._network_managers_operations#NetworkManagersOperations.{}',
        client_factory=cf_networkmanager
    )

    network_connectivityconfiguration = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._connectivity_configurations_operations#ConnectivityConfigurationsOperations.{}',
        client_factory=cf_connectivityconfiguration
    )

    network_networkgroup = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._network_groups_operations#NetworkGroupsOperations.{}',
        client_factory=cf_networkgroup
    )

    network_securityuserconfiguration = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._security_user_configurations_operations#SecurityUserConfigurationsOperations.{}',
        client_factory=cf_securityuserconfiguration
    )

    network_securityadminconfiguration = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._security_admin_configurations_operations#SecurityAdminConfigurationsOperations.{}',
        client_factory=cf_securityadminconfiguration
    )

    network_adminrule = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._admin_rules_operations#AdminRulesOperations.{}',
        client_factory=cf_adminrule
    )

    network_adminrulecollection = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._admin_rule_collections_operations#AdminRuleCollectionsOperations.{}',
        client_factory=cf_adminrulecollection
    )

    # network_userrule = CliCommandType(
    #     operations_tmpl='azext_network_manager.vendored_sdks.operations._user_rules_operations#UserRulesOperations.{}',
    #     client_factory=cf_userrule
    # )

    # network_userrulecollection = CliCommandType(
    #     operations_tmpl='azext_network_manager.vendored_sdks.operations._user_rule_collections_operations#UserRuleCollectionsOperations.{}',
    #     client_factory=cf_userrulecollection
    # )

    network_scopeconnection = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._scope_connections_operations#ScopeConnectionsOperations.{}',
        client_factory=cf_scopeconnection
    )

    network_staticmembers = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._static_members_operations#StaticMembersOperations.{}',
        client_factory=cf_staticmembers
    )

    network_subscriptionconnection = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._subscription_network_manager_connections_operations#SubscriptionNetworkManagerConnectionsOperations.{}',
        client_factory=cf_subscriptionconnection
    )

#    network_managementgroupconnection = CliCommandType(
#        operations_tmpl='azext_network_manager.vendored_sdks.operations._management_group_network_manager_connections_operations#ManagementGroupNetworkManagerConnectionsOperations.{}',
#        client_factory=cf_managementgroupconnection
#    )

    with self.command_group('network manager', network_networkmanager, client_factory=cf_networkmanager) as g:
        g.custom_command('create', 'network_manager_create')
        g.custom_command('list', 'network_manager_list')
        g.custom_show_command('show', 'network_manager_show')
        g.generic_update_command('update', custom_func_name='network_manager_update')
        g.custom_command('delete', 'network_manager_delete', confirmation=True)
        g.custom_command('post-commit', 'network_manager_commit_post')
        g.custom_command('list-deploy-status', 'network_manager_deploy_status_list')
        # g.custom_command('list-effect-vnet', 'network_manager_effect_vnet_list_by_network_manager')
        g.custom_command('list-active-connectivity-config', 'network_manager_active_config_list')
        g.custom_command('list-effective-connectivity-config', 'network_manager_effective_config_list')
        g.custom_command('list-effective-security-admin-rule', 'network_manager_effective_security_admin_rule_list')
        g.custom_command('list-active-security-admin-rule', 'network_manager_active_security_admin_rule_list')
        # g.custom_command('list-active-security-user-rule', 'network_manager_active_security_user_rule_list')

    with self.command_group('network manager connect-config', network_connectivityconfiguration, client_factory=cf_connectivityconfiguration) as g:
        g.custom_command('list', 'network_manager_connect_config_list')
        g.custom_show_command('show', 'network_manager_connect_config_show')
        g.custom_command('create', 'network_manager_connect_config_create')
        g.generic_update_command('update', setter_arg_name='connectivity_configuration', custom_func_name='network_manager_connect_config_update')
        g.custom_command('delete', 'network_manager_connect_config_delete', confirmation=True)

    with self.command_group('network manager group', network_networkgroup, client_factory=cf_networkgroup) as g:
        g.custom_command('list', 'network_manager_group_list')
        g.custom_show_command('show', 'network_manager_group_show')
        g.custom_command('create', 'network_manager_group_create')
        g.generic_update_command('update', custom_func_name='network_manager_group_update')
        g.custom_command('delete', 'network_manager_group_delete', confirmation=True)
        g.custom_command('list-effect-vnet', 'network_manager_effect_vnet_list_by_network_group')

    with self.command_group('network manager security-user-config', network_securityuserconfiguration, client_factory=cf_securityuserconfiguration) as g:
        g.custom_command('list', 'network_manager_security_user_config_list')
        g.custom_show_command('show', 'network_manager_security_user_config_show')
        g.custom_command('create', 'network_manager_security_user_config_create')
        g.generic_update_command('update', setter_arg_name='security_user_configuration', custom_func_name='network_manager_security_user_config_update')
        g.custom_command('delete', 'network_manager_security_user_config_delete', confirmation=True)

    with self.command_group('network manager security-admin-config', network_securityadminconfiguration, client_factory=cf_securityadminconfiguration) as g:
        g.custom_command('list', 'network_manager_security_admin_config_list')
        g.custom_show_command('show', 'network_manager_security_admin_config_show')
        g.custom_command('create', 'network_manager_security_admin_config_create')
        g.generic_update_command('update', setter_arg_name='security_admin_configuration', custom_func_name='network_manager_security_admin_config_update')
        g.custom_command('delete', 'network_manager_security_admin_config_delete', confirmation=True)

    with self.command_group('network manager security-admin-config rule-collection rule', network_adminrule, client_factory=cf_adminrule) as g:
        g.custom_command('create', 'network_manager_admin_rule_create')
        g.generic_update_command('update', setter_arg_name='admin_rule', custom_func_name='network_manager_admin_rule_update')
        g.custom_command('list', 'network_manager_admin_rule_list')
        g.custom_show_command('show', 'network_manager_admin_rule_show')
        g.custom_command('delete', 'network_manager_admin_rule_delete', confirmation=True)

    with self.command_group('network manager security-admin-config rule-collection', network_adminrulecollection, client_factory=cf_adminrulecollection) as g:
        g.custom_command('create', 'network_manager_admin_rule_collection_create')
        g.generic_update_command('update', setter_arg_name='rule_collection', custom_func_name='network_manager_admin_rule_collection_update')
        g.custom_command('list', 'network_manager_admin_rule_collection_list')
        g.custom_show_command('show', 'network_manager_admin_rule_collection_show')
        g.custom_command('delete', 'network_manager_admin_rule_collection_delete', confirmation=True)

    # with self.command_group('network manager security-user-config rule-collection rule', network_userrule, client_factory=cf_userrule) as g:
    #     g.custom_command('list', 'network_manager_user_rule_list')
    #     g.custom_show_command('show', 'network_manager_user_rule_show')
    #     g.custom_command('create', 'network_manager_user_rule_create')
    #     g.generic_update_command('update', setter_arg_name='user_rule', custom_func_name='network_manager_user_rule_update')
    #     g.custom_command('delete', 'network_manager_user_rule_delete', confirmation=True)

    # with self.command_group('network manager security-user-config rule-collection', network_userrulecollection, client_factory=cf_userrulecollection) as g:
    #     g.custom_command('create', 'network_manager_user_rule_collection_create')
    #     g.generic_update_command('update', setter_arg_name='user_rule_collection', custom_func_name='network_manager_user_rule_collection_update')
    #     g.custom_command('list', 'network_manager_user_rule_collection_list')
    #     g.custom_show_command('show', 'network_manager_user_rule_collection_show')
    #     g.custom_command('delete', 'network_manager_user_rule_collection_delete', confirmation=True)

    with self.command_group('network manager connection subscription', network_subscriptionconnection, client_factory=cf_subscriptionconnection) as g:
        g.custom_command('create', 'network_manager_connection_subscription_create')
        g.generic_update_command('update', custom_func_name='network_manager_connection_subscription_update')
        g.custom_command('list', 'network_manager_connection_subscription_list')
        g.custom_show_command('show', 'network_manager_connection_subscription_show')
        g.custom_command('delete', 'network_manager_connection_subscription_delete', confirmation=True)

#    with self.command_group('network manager connection management-group', network_managementgroupconnection, client_factory=cf_managementgroupconnection) as g:
#        g.custom_command('create', 'network_manager_connection_management_group_create')
#        g.generic_update_command('update', setter_arg_name='connection_management_group', custom_func_name='network_manager_connection_management_group_update')
#        g.custom_command('list', 'network_manager_connection_management_group_list')
#        g.custom_show_command('show', 'network_manager_connection_management_group_show')
#        g.custom_command('delete', 'network_manager_connection_management_group_delete', confirmation=True)

    with self.command_group('network manager scope-connection', network_scopeconnection, client_factory=cf_scopeconnection) as g:
        g.custom_command('create', 'network_manager_scope_connection_create')
        g.generic_update_command('update', custom_func_name='network_manager_scope_connection_update')
        g.custom_command('list', 'network_manager_scope_connection_list')
        g.custom_show_command('show', 'network_manager_scope_connection_show')
        g.custom_command('delete', 'network_manager_scope_connection_delete', confirmation=True)

    with self.command_group('network manager group static-member', network_staticmembers, client_factory=cf_staticmembers) as g:
        g.custom_command('create', 'network_manager_group_static_member_create')
        # g.generic_update_command('update', custom_func_name='network_manager_group_static_member_update')
        g.custom_command('list', 'network_manager_group_static_member_list')
        g.custom_show_command('show', 'network_manager_group_static_member_show')
        # network_manager_group_static_member_show
        g.custom_command('delete', 'network_manager_group_static_member_delete', confirmation=True)
