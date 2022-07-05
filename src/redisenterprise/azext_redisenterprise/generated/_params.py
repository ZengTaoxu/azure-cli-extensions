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

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_redisenterprise.action import (
    AddPersistence,
    AddModules,
    AddLinkedDatabases
)


def load_arguments(self, _):

    with self.argument_context('redisenterprise operation-status show') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), id_part='name')
        c.argument('operation_id', type=str, help='The operation\'s unique identifier.', id_part='child_name_1')

    with self.argument_context('redisenterprise list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('redisenterprise show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')

    with self.argument_context('redisenterprise create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('sku', arg_type=get_enum_type(['Enterprise_E10', 'Enterprise_E20', 'Enterprise_E50',
                                                  'Enterprise_E100', 'EnterpriseFlash_F300', 'EnterpriseFlash_F700',
                                                  'EnterpriseFlash_F1500']), help='The type of RedisEnterprise cluster '
                   'to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)')
        c.argument('capacity', type=int, help='The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending '
                   'on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.')
        c.argument('zones', options_list=['--zones', '-z'], nargs='+', help='The Availability Zones where this cluster '
                   'will be deployed.')
        c.argument('minimum_tls_version', arg_type=get_enum_type(['1.0', '1.1', '1.2']), help='The minimum TLS version '
                   'for the cluster to support, e.g. \'1.2\'')

    with self.argument_context('redisenterprise update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('sku', arg_type=get_enum_type(['Enterprise_E10', 'Enterprise_E20', 'Enterprise_E50',
                                                  'Enterprise_E100', 'EnterpriseFlash_F300', 'EnterpriseFlash_F700',
                                                  'EnterpriseFlash_F1500']), help='The type of RedisEnterprise cluster '
                   'to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)')
        c.argument('capacity', type=int, help='The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending '
                   'on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.')
        c.argument('tags', tags_type)
        c.argument('minimum_tls_version', arg_type=get_enum_type(['1.0', '1.1', '1.2']), help='The minimum TLS version '
                   'for the cluster to support, e.g. \'1.2\'')

    with self.argument_context('redisenterprise delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')

    with self.argument_context('redisenterprise wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')

    with self.argument_context('redisenterprise database list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.')

    with self.argument_context('redisenterprise database show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')

    with self.argument_context('redisenterprise database create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.')
        c.argument('client_protocol', arg_type=get_enum_type(['Encrypted', 'Plaintext']), help='Specifies whether '
                   'redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is '
                   'TLS-encrypted.')
        c.argument('port', type=int, help='TCP port of the database endpoint. Specified at create time. Defaults to an '
                   'available port.')
        c.argument('clustering_policy', arg_type=get_enum_type(['EnterpriseCluster', 'OSSCluster']), help='Clustering '
                   'policy - default is OSSCluster. Specified at create time.')
        c.argument('eviction_policy', arg_type=get_enum_type(['AllKeysLFU', 'AllKeysLRU', 'AllKeysRandom',
                                                              'VolatileLRU', 'VolatileLFU', 'VolatileTTL',
                                                              'VolatileRandom', 'NoEviction']), help='Redis eviction '
                   'policy - default is VolatileLRU')
        c.argument('persistence', action=AddPersistence, nargs='+', help='Persistence settings', is_preview=True)
        c.argument('modules', action=AddModules, nargs='+', help='Optional set of redis modules to enable in this '
                   'database - modules can only be added at creation time.')
        c.argument('group_nickname', type=str, help='Name for the group of linked database resources', arg_group='Geo '
                   'Replication')
        c.argument('linked_databases', action=AddLinkedDatabases, nargs='+', help='List of database resources to link '
                   'with this database', arg_group='Geo Replication')

    with self.argument_context('redisenterprise database update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('client_protocol', arg_type=get_enum_type(['Encrypted', 'Plaintext']), help='Specifies whether '
                   'redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is '
                   'TLS-encrypted.')
        c.argument('eviction_policy', arg_type=get_enum_type(['AllKeysLFU', 'AllKeysLRU', 'AllKeysRandom',
                                                              'VolatileLRU', 'VolatileLFU', 'VolatileTTL',
                                                              'VolatileRandom', 'NoEviction']), help='Redis eviction '
                   'policy - default is VolatileLRU')
        c.argument('persistence', action=AddPersistence, nargs='+', help='Persistence settings', is_preview=True)
        c.argument('group_nickname', type=str, help='Name for the group of linked database resources', arg_group='Geo '
                   'Replication')
        c.argument('linked_databases', action=AddLinkedDatabases, nargs='+', help='List of database resources to link '
                   'with this database', arg_group='Geo Replication')

    with self.argument_context('redisenterprise database delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')

    with self.argument_context('redisenterprise database export') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('sas_uri', type=str, help='SAS URI for the target directory to export to')

    with self.argument_context('redisenterprise database force-unlink') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('unlink_ids', nargs='+', help='The resource IDs of the database resources to be unlinked.')

    with self.argument_context('redisenterprise database import') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('sas_uris', nargs='+', help='SAS URIs for the target blobs to import from')

    with self.argument_context('redisenterprise database list-keys') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.')

    with self.argument_context('redisenterprise database regenerate-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('key_type', arg_type=get_enum_type(['Primary', 'Secondary']),
                   help='Which access key to regenerate.')

    with self.argument_context('redisenterprise database wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
