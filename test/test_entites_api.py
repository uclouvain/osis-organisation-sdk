"""
    Organisations Service

    A set of API endpoints that allow you to get information about organizations  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_organisation_sdk
from osis_organisation_sdk.api.entites_api import EntitesApi  # noqa: E501


class TestEntitesApi(unittest.TestCase):
    """EntitesApi unit test stubs"""

    def setUp(self):
        self.api = EntitesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_entities(self):
        """Test case for get_entities

        """
        pass

    def test_get_entity_addresses(self):
        """Test case for get_entity_addresses

        """
        pass


if __name__ == '__main__':
    unittest.main()
