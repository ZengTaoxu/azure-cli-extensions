# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azext_observability._help import helps  # pylint: disable=unused-import


class ObservabilityCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_command_type = CliCommandType(
            operations_tmpl='azext_observability.custom#{}')
        super().__init__(cli_ctx=cli_ctx,
                         custom_command_type=custom_command_type)

    def load_command_table(self, args):
        from azext_observability.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_observability._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = ObservabilityCommandsLoader
