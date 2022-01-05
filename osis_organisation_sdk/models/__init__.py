# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_organisation_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_organisation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_organisation_sdk.model.address import Address
from osis_organisation_sdk.model.entite import Entite
from osis_organisation_sdk.model.entite_type_enum import EntiteTypeEnum
from osis_organisation_sdk.model.error import Error
from osis_organisation_sdk.model.paginated_addresses import PaginatedAddresses
from osis_organisation_sdk.model.paginated_addresses_all_of import PaginatedAddressesAllOf
from osis_organisation_sdk.model.paginated_entites import PaginatedEntites
from osis_organisation_sdk.model.paginated_entites_all_of import PaginatedEntitesAllOf
from osis_organisation_sdk.model.paging import Paging
