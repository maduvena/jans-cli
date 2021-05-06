# coding: utf-8

# flake8: noqa

"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    OpenAPI spec version: 5.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.default_api import DefaultApi
from swagger_client.api.discovery_api import DiscoveryApi
from swagger_client.api.fido2_devices_api import Fido2DevicesApi
from swagger_client.api.fido_devices_api import FidoDevicesApi
from swagger_client.api.group_api import GroupApi
from swagger_client.api.search_api import SearchApi
from swagger_client.api.user_api import UserApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.address import Address
from swagger_client.models.any_value import AnyValue
from swagger_client.models.base_resource import BaseResource
from swagger_client.models.basic_list_response import BasicListResponse
from swagger_client.models.bulk_data import BulkData
from swagger_client.models.bulk_operation import BulkOperation
from swagger_client.models.bulk_request import BulkRequest
from swagger_client.models.email import Email
from swagger_client.models.entitlement import Entitlement
from swagger_client.models.error_response import ErrorResponse
from swagger_client.models.fido2_device_resource import Fido2DeviceResource
from swagger_client.models.fido2_list_response import Fido2ListResponse
from swagger_client.models.fido_device_resource import FidoDeviceResource
from swagger_client.models.fido_list_response import FidoListResponse
from swagger_client.models.generic_list_response import GenericListResponse
from swagger_client.models.generic_resource import GenericResource
from swagger_client.models.group import Group
from swagger_client.models.group_list_response import GroupListResponse
from swagger_client.models.group_resource import GroupResource
from swagger_client.models.instant_messaging_address import InstantMessagingAddress
from swagger_client.models.member import Member
from swagger_client.models.meta import Meta
from swagger_client.models.name import Name
from swagger_client.models.one_of_generic_resource import OneOfGenericResource
from swagger_client.models.patch_operation import PatchOperation
from swagger_client.models.patch_request import PatchRequest
from swagger_client.models.phone_number import PhoneNumber
from swagger_client.models.photo import Photo
from swagger_client.models.resource_type import ResourceType
from swagger_client.models.resource_type_list_response import ResourceTypeListResponse
from swagger_client.models.resource_type_schema_extensions import ResourceTypeSchemaExtensions
from swagger_client.models.role import Role
from swagger_client.models.schema_attribute import SchemaAttribute
from swagger_client.models.schema_list_response import SchemaListResponse
from swagger_client.models.schema_resource import SchemaResource
from swagger_client.models.search_request import SearchRequest
from swagger_client.models.service_provider_config_response import ServiceProviderConfigResponse
from swagger_client.models.service_provider_config_response_authentication_schemes import ServiceProviderConfigResponseAuthenticationSchemes
from swagger_client.models.service_provider_config_response_bulk import ServiceProviderConfigResponseBulk
from swagger_client.models.service_provider_config_response_filter import ServiceProviderConfigResponseFilter
from swagger_client.models.service_provider_config_response_meta import ServiceProviderConfigResponseMeta
from swagger_client.models.service_provider_config_response_patch import ServiceProviderConfigResponsePatch
from swagger_client.models.user_list_response import UserListResponse
from swagger_client.models.user_resource import UserResource
from swagger_client.models.x509_certificate import X509Certificate