# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer
import time

class NetworkAnalyticsScenario(ScenarioTest):
    @ResourceGroupPreparer(parameter_name_for_location='location')
    def test_data_product_e2e(self, resource_group, location, user_id="test@microsoft.com"):
        self.kwargs.update({
          'name': self.create_random_name(prefix='cli', length=8),
          'group': resource_group,
          'loc': location,
          'id' : user_id,
        })

        #create DP
        self.cmd('az network-analytics data-product create --name {name} --resource-group {group} --location {loc} --publisher Microsoft --product MCC --major-version  1.0.0 --owners {id} --key-encryption-enable Enabled --encryption-key key-vault-uri=https://testkv.vault.azure.net key-name=testadx key-version=6adfebea181a443b90cc89362d5888b5 --networkacls virtual-network-rule[0].id=/subscriptions/susbcription/resourceGroups/resourceGroupName/providers/Microsoft.Network/virtualNetworks/checkVnet/subnets/default virtual-network-rule[0].action=Allow virtual-network-rule[0].state=Provisioning ip-rules[0].value=1.1.1.1 ip-rules[0].action=Allow allowed-query-ip-range-list=["1.1.1.1-2.2.2.2"] default-action=Allow --private-links-enabled Enabled --public-network-access Enabled --purview-account "/subscriptions/9a021c4c-ddcd-4e80-9155-a5b0e872f4c2/resourceGroups/aw8-compute-resgrp/providers/Microsoft.Purview/accounts/AOI-Test-Instance" --purview-collection cy5ne2 --redundancy Disabled --identity {{"type":"UserAssigned","userAssignedIdentities":{{"/subscriptions/9a021c4c-ddcd-4e80-9155-a5b0e872f4c2/resourceGroups/a40rg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/testiden":{{}}}}}} --tags envType=prod region=us', checks=[
            self.check('name', '{name}'),                                                                                                     
            self.check('provisioningState', 'Succeeded')
        ])

        #wait for 20 second
        time.sleep(20)

        #List All DP
        dplist = self.cmd('az network-analytics data-product list').get_output_in_json()
        self.assertTrue((len(dplist) > 0), msg="Data product list is empty")

        #List DP
        dplistinrg = self.cmd('az network-analytics data-product list --resource-group {group}').get_output_in_json()
        self.assertEquals(len(dplistinrg), 1, msg="Data product list should have exactly one element")

        #Get DP
        self.cmd('az network-analytics data-product show --name {name} --resource-group {group}', checks=[
            self.check('name', '{name}'),
            self.check('type', 'microsoft.networkanalytics/dataproducts')
        ])

        #Add User Role
        self.cmd('az network-analytics data-product add-user-role --data-product-name {name} --resource-group {group} --data-type-scope " " --principal-id {id} --principal-type user --role reader --role-id " " --user-name " "')

        #wait for 20 second
        time.sleep(20)

        #List User Role
        rolelist = self.cmd('az network-analytics data-product list-roles-assignment --data-product-name {name} --resource-group {group}').get_output_in_json()
        self.assertEquals(rolelist['count'], 1, msg="Expected role count is 1")
        self.assertEquals(rolelist['roleAssignmentResponse'][0]['principalId'], user_id, msg="Principal ID is not matching with the user ID")

        #Remove User Role
        self.cmd('az network-analytics data-product remove-user-role --data-product-name {name} --resource-group {group} --data-type-scope " " --principal-id {id} --principal-type user --role reader --role-id " " --user-name " " --role-assignment-id " "')

        #wait for 20 second
        time.sleep(20)

        #List User Role
        emptyrolelist = self.cmd('az network-analytics data-product list-roles-assignment --data-product-name {name} --resource-group {group}').get_output_in_json()
        self.assertEquals(emptyrolelist['count'], 0, msg="role list ia not empty after role is deleted")

        #Delete DP
        self.cmd('az network-analytics data-product delete --name {name} --resource-group {group} --yes')

        #wait for 20 second
        time.sleep(20)

        #List DP
        dplistinrg = self.cmd('az network-analytics data-product list --resource-group {group}').get_output_in_json()
        self.assertEquals(len(dplistinrg), 0, msg="Data product list is not empty after deletion")

    pass