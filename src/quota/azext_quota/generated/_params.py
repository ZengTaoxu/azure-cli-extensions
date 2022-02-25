# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.validators import validate_file_or_dict
from azext_quota.action import AddLimitobject


def load_arguments(self, _):

    with self.argument_context('quota usage list') as c:
        c.argument('scope', type=str, help='The target Azure resource URI')

    with self.argument_context('quota usage show') as c:
        c.argument('resource_name', type=str, help='The resource name for a given resource provider')
        c.argument('scope', type=str, help='The target Azure resource URI')

    with self.argument_context('quota list') as c:
        c.argument('scope', type=str, help='The target Azure resource URI')

    with self.argument_context('quota show') as c:
        c.argument('resource_name', type=str, help='The resource name for a given resource provider.')
        c.argument('scope', type=str, help='The target Azure resource URI.')

    with self.argument_context('quota create') as c:
        c.argument('resource_name', type=str, help='The resource name for a given resource provider.')
        c.argument('scope', type=str, help='The target Azure resource URI.')
        c.argument('limit', action=AddLimitobject, nargs='+', help='The resource quota limit value.',
                   arg_group='Limit')
        c.argument('name', type=str, help='Resource type name.')
        c.argument('value', type=int, help='Resource type name.')
        c.argument('resource_type', type=str, help='Resource type name.')
        c.argument('properties', type=validate_file_or_dict, help='Additional properties for the specific resource '
                   'provider.')

    with self.argument_context('quota update') as c:
        c.argument('resource_name', type=str, help='The resource name for a given resource provider.')
        c.argument('scope', type=str, help='The target Azure resource URI.')
        c.argument('limit', action=AddLimitobject, nargs='+', help='The resource quota limit value.',
                   arg_group='Limit')
        c.argument('name', type=str, help='Resource type name.')
        c.argument('value', type=int, help='Resource type name.')
        c.argument('resource_type', type=str, help='Resource type name.')
        c.argument('properties', type=validate_file_or_dict, help='Additional properties for the specific resource '
                                                                  'provider.')
        c.ignore('create_quota_request')

    with self.argument_context('quota wait') as c:
        c.argument('resource_name', type=str, help='Resource name for a given resource provider.')
        c.argument('scope', type=str, help='The target Azure resource URI.')

    with self.argument_context('quota request status list') as c:
        c.argument('scope', type=str, help='The target Azure resource URI.')
        c.argument('filter_', options_list=['--filter'], type=str, help='')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('quota request status show') as c:
        c.argument('id', options_list=['--id'], type=str, help='Quota request ID.')
        c.argument('scope', type=str, help='The target Azure resource URI.')

    with self.argument_context('quota operation list') as c:
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')