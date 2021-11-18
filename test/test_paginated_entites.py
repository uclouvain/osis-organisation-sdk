"""
    Organisations Service

    A set of API endpoints that allow you to get information about organizations  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_organisation_sdk
from osis_organisation_sdk.model.entite import Entite
from osis_organisation_sdk.model.paginated_entites_all_of import PaginatedEntitesAllOf
from osis_organisation_sdk.model.paging import Paging
globals()['Entite'] = Entite
globals()['PaginatedEntitesAllOf'] = PaginatedEntitesAllOf
globals()['Paging'] = Paging
from osis_organisation_sdk.model.paginated_entites import PaginatedEntites


class TestPaginatedEntites(unittest.TestCase):
    """PaginatedEntites unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedEntites(self):
        """Test PaginatedEntites"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedEntites()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
