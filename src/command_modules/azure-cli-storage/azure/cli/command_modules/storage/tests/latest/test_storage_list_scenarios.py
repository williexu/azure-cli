# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, StorageAccountPreparer,
                               JMESPathCheck, NoneCheck, StringCheck, StringContainCheck)
from ..storage_test_util import StorageScenarioMixin


class StorageListingScenarios(StorageScenarioMixin, ScenarioTest):
    @ResourceGroupPreparer()
    @StorageAccountPreparer()
    def test_storage_file_list_scenario(self, resource_group, storage_account):
        account_info = self.get_account_info(resource_group, storage_account)
        s1 = self.create_share(account_info)
        s2 = self.create_share(account_info)

        # verify listing shares
        a = self.storage_cmd('storage share list', account_info)
        print(a.__dict__)
        raise Exception

        dir1, dir2 = 'dir1', 'dir2'
        file1, file2, = 'file1.txt', 'file2.txt'

        self.storage_cmd('storage directory create --share-name {} -n {}', account_info, s1, d1)
        self.storage_cmd('storage directory create --share-name {} -n {}', account_info, s2, d2)

        local_file = self.create_temp_file(512, full_random=False)

        self.storage_cmd('storage file upload -p {} --share-name {} --source "{}"',
                         account_info, file1, s1, local_file)
        self.storage_cmd('storage file upload -p {} --share-name {} --source "{}"',
                         account_info, file2, s1, local_file)



    @ResourceGroupPreparer()
    @StorageAccountPreparer()
    def test_storage_blob_list_scenario(self, resource_group, storage_account):
        account_info = self.get_account_info(resource_group, storage_account)
        c1 = self.create_container(account_info)
        c2 = self.create_container(account_info)
        blob1, blob2 = 'blob1', 'blob2'

        local_file = self.create_temp_file(512, full_random=False)

        self.storage_cmd('storage blob upload -c {} -f "{}" -n {}', account_info,
                         container, local_file, blob1)
        self.storage_cmd('storage blob upload -c {} -f "{}" -n {}', account_info,
                         container, local_file, blob2)

        self.storage_cmd('storage blob list -c {} -otable --num-results 1', account_info, container)
