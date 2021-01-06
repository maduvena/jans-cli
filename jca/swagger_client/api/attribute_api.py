# coding: utf-8

"""
    jans-config-api

    jans-config-api - Authorization services  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: xxx@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AttributeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_attributes_by_inum(self, inum, **kwargs):  # noqa: E501
        """Deletes an attribute based on inum.  # noqa: E501

        Deletes an attribute based on inum.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_attributes_by_inum(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: Attribute ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_attributes_by_inum_with_http_info(inum, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_attributes_by_inum_with_http_info(inum, **kwargs)  # noqa: E501
            return data

    def delete_attributes_by_inum_with_http_info(self, inum, **kwargs):  # noqa: E501
        """Deletes an attribute based on inum.  # noqa: E501

        Deletes an attribute based on inum.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_attributes_by_inum_with_http_info(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: Attribute ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_attributes_by_inum" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inum' is set
        if ('inum' not in params or
                params['inum'] is None):
            raise ValueError("Missing the required parameter `inum` when calling `delete_attributes_by_inum`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inum' in params:
            path_params['inum'] = params['inum']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/attributes/{inum}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_attributes(self, **kwargs):  # noqa: E501
        """Gets a list of Gluu attributes.  # noqa: E501

        Gets all attributes. Optionally max-size of the result, attribute status and pattern can be provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attributes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Search size - max size of the results to return.
        :param str pattern: Search pattern.
        :param str status: Status of the attribute
        :return: list[GluuAttribute]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_attributes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_attributes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_attributes_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of Gluu attributes.  # noqa: E501

        Gets all attributes. Optionally max-size of the result, attribute status and pattern can be provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attributes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Search size - max size of the results to return.
        :param str pattern: Search pattern.
        :param str status: Status of the attribute
        :return: list[GluuAttribute]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'pattern', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_attributes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'pattern' in params:
            query_params.append(('pattern', params['pattern']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/attributes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GluuAttribute]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_attributes_by_inum(self, inum, **kwargs):  # noqa: E501
        """Gets an attribute based on inum.  # noqa: E501

        Gets an attribute based on inum.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attributes_by_inum(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: Attribute ID. (required)
        :return: GluuAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_attributes_by_inum_with_http_info(inum, **kwargs)  # noqa: E501
        else:
            (data) = self.get_attributes_by_inum_with_http_info(inum, **kwargs)  # noqa: E501
            return data

    def get_attributes_by_inum_with_http_info(self, inum, **kwargs):  # noqa: E501
        """Gets an attribute based on inum.  # noqa: E501

        Gets an attribute based on inum.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attributes_by_inum_with_http_info(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: Attribute ID. (required)
        :return: GluuAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_attributes_by_inum" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inum' is set
        if ('inum' not in params or
                params['inum'] is None):
            raise ValueError("Missing the required parameter `inum` when calling `get_attributes_by_inum`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inum' in params:
            path_params['inum'] = params['inum']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/attributes/{inum}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GluuAttribute',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_attributes_by_inum(self, inum, **kwargs):  # noqa: E501
        """Partially modify a GluuAttribute.  # noqa: E501

        Partially modify a GluuAttribute.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_attributes_by_inum(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: Attribute ID. (required)
        :param list[PatchRequest] body:
        :return: GluuAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_attributes_by_inum_with_http_info(inum, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_attributes_by_inum_with_http_info(inum, **kwargs)  # noqa: E501
            return data

    def patch_attributes_by_inum_with_http_info(self, inum, **kwargs):  # noqa: E501
        """Partially modify a GluuAttribute.  # noqa: E501

        Partially modify a GluuAttribute.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_attributes_by_inum_with_http_info(inum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inum: Attribute ID. (required)
        :param list[PatchRequest] body:
        :return: GluuAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inum', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_attributes_by_inum" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inum' is set
        if ('inum' not in params or
                params['inum'] is None):
            raise ValueError("Missing the required parameter `inum` when calling `patch_attributes_by_inum`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inum' in params:
            path_params['inum'] = params['inum']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/attributes/{inum}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GluuAttribute',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_attributes(self, body, **kwargs):  # noqa: E501
        """Adds a new attribute.  # noqa: E501

        Adds a new attribute.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_attributes(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GluuAttribute body: (required)
        :return: GluuAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_attributes_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_attributes_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_attributes_with_http_info(self, body, **kwargs):  # noqa: E501
        """Adds a new attribute.  # noqa: E501

        Adds a new attribute.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_attributes_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GluuAttribute body: (required)
        :return: GluuAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_attributes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_attributes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/attributes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GluuAttribute',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_attributes(self, body, **kwargs):  # noqa: E501
        """Updates an existing attribute.  # noqa: E501

        Updates an existing attribute.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_attributes(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GluuAttribute body: (required)
        :return: GluuAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_attributes_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_attributes_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def put_attributes_with_http_info(self, body, **kwargs):  # noqa: E501
        """Updates an existing attribute.  # noqa: E501

        Updates an existing attribute.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_attributes_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GluuAttribute body: (required)
        :return: GluuAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_attributes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_attributes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jans-auth']  # noqa: E501

        return self.api_client.call_api(
            '/jans-config-api/api/v1/attributes', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GluuAttribute',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)