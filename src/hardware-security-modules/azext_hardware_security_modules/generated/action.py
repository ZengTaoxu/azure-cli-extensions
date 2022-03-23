# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


# pylint: disable=protected-access

# pylint: disable=no-self-use


import argparse
from collections import defaultdict
from knack.util import CLIError


class AddSubnet(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.subnet = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'id':
                d['id'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter subnet. All possible keys are: id'.format(k)
                )

        return d


class AddNetworkInterfaces(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddNetworkInterfaces, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'private-ip-address':
                d['private_ip_address'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter network-interfaces. All possible keys are:'
                    ' private-ip-address'.format(k)
                )

        return d
