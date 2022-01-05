"""
    Organisations Service

    A set of API endpoints that allow you to get information about organizations  # noqa: E501

    The version of the OpenAPI document: 1.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_organisation_sdk
from osis_organisation_sdk.model.address import Address
from osis_organisation_sdk.model.paginated_addresses_all_of import PaginatedAddressesAllOf
from osis_organisation_sdk.model.paging import Paging
globals()['Address'] = Address
globals()['PaginatedAddressesAllOf'] = PaginatedAddressesAllOf
globals()['Paging'] = Paging
from osis_organisation_sdk.model.paginated_addresses import PaginatedAddresses


class TestPaginatedAddresses(unittest.TestCase):
    """PaginatedAddresses unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedAddresses(self):
        """Test PaginatedAddresses"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedAddresses()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
