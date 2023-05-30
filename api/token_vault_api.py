# coding: utf-8

"""
    New Payment Gateway APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2022-01-01
    Contact: nextgenapi@cashfree.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cashfree_pg_sdk_python.api_client import ApiClient
from cashfree_pg_sdk_python.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TokenVaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_specific_saved_instrument(self, x_client_id, x_client_secret, customer_id, instrument_id, **kwargs):  # noqa: E501
        """Delete Saved Instrument  # noqa: E501

        To delete a saved instrument for a customer id and instrument id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_specific_saved_instrument(x_client_id, x_client_secret, customer_id, instrument_id, async_req=True)
        >>> result = thread.get()

        :param x_client_id: (required)
        :type x_client_id: str
        :param x_client_secret: (required)
        :type x_client_secret: str
        :param customer_id: (required)
        :type customer_id: str
        :param instrument_id: (required)
        :type instrument_id: str
        :param x_api_version:
        :type x_api_version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CFFetchAllSavedInstruments
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_specific_saved_instrument_with_http_info(x_client_id, x_client_secret, customer_id, instrument_id, **kwargs)  # noqa: E501

    def delete_specific_saved_instrument_with_http_info(self, x_client_id, x_client_secret, customer_id, instrument_id, **kwargs):  # noqa: E501
        """Delete Saved Instrument  # noqa: E501

        To delete a saved instrument for a customer id and instrument id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_specific_saved_instrument_with_http_info(x_client_id, x_client_secret, customer_id, instrument_id, async_req=True)
        >>> result = thread.get()

        :param x_client_id: (required)
        :type x_client_id: str
        :param x_client_secret: (required)
        :type x_client_secret: str
        :param customer_id: (required)
        :type customer_id: str
        :param instrument_id: (required)
        :type instrument_id: str
        :param x_api_version:
        :type x_api_version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CFFetchAllSavedInstruments, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'x_client_id',
            'x_client_secret',
            'customer_id',
            'instrument_id',
            'x_api_version'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_specific_saved_instrument" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_client_id' is set
        if self.api_client.client_side_validation and local_var_params.get('x_client_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_client_id` when calling `delete_specific_saved_instrument`")  # noqa: E501
        # verify the required parameter 'x_client_secret' is set
        if self.api_client.client_side_validation and local_var_params.get('x_client_secret') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_client_secret` when calling `delete_specific_saved_instrument`")  # noqa: E501
        # verify the required parameter 'customer_id' is set
        if self.api_client.client_side_validation and local_var_params.get('customer_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `customer_id` when calling `delete_specific_saved_instrument`")  # noqa: E501
        # verify the required parameter 'instrument_id' is set
        if self.api_client.client_side_validation and local_var_params.get('instrument_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrument_id` when calling `delete_specific_saved_instrument`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in local_var_params:
            path_params['customer_id'] = local_var_params['customer_id']  # noqa: E501
        if 'instrument_id' in local_var_params:
            path_params['instrument_id'] = local_var_params['instrument_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'x_client_id' in local_var_params:
            header_params['x-client-id'] = local_var_params['x_client_id']  # noqa: E501
        if 'x_client_secret' in local_var_params:
            header_params['x-client-secret'] = local_var_params['x_client_secret']  # noqa: E501
        if 'x_api_version' in local_var_params:
            header_params['x-api-version'] = local_var_params['x_api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "CFFetchAllSavedInstruments",
        }

        return self.api_client.call_api(
            '/customers/{customer_id}/instruments/{instrument_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def fetch_all_saved_instruments(self, x_client_id, x_client_secret, customer_id, instrument_type, **kwargs):  # noqa: E501
        """Fetch All Saved Instruments  # noqa: E501

        To get all saved instruments for a customer id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_all_saved_instruments(x_client_id, x_client_secret, customer_id, instrument_type, async_req=True)
        >>> result = thread.get()

        :param x_client_id: (required)
        :type x_client_id: str
        :param x_client_secret: (required)
        :type x_client_secret: str
        :param customer_id: (required)
        :type customer_id: str
        :param instrument_type: (required)
        :type instrument_type: str
        :param x_api_version:
        :type x_api_version: str
        :param x_idempotency_replayed:
        :type x_idempotency_replayed: bool
        :param x_idempotency_key:
        :type x_idempotency_key: str
        :param x_request_id:
        :type x_request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[CFFetchAllSavedInstruments]
        """
        kwargs['_return_http_data_only'] = True
        return self.fetch_all_saved_instruments_with_http_info(x_client_id, x_client_secret, customer_id, instrument_type, **kwargs)  # noqa: E501

    def fetch_all_saved_instruments_with_http_info(self, x_client_id, x_client_secret, customer_id, instrument_type, **kwargs):  # noqa: E501
        """Fetch All Saved Instruments  # noqa: E501

        To get all saved instruments for a customer id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_all_saved_instruments_with_http_info(x_client_id, x_client_secret, customer_id, instrument_type, async_req=True)
        >>> result = thread.get()

        :param x_client_id: (required)
        :type x_client_id: str
        :param x_client_secret: (required)
        :type x_client_secret: str
        :param customer_id: (required)
        :type customer_id: str
        :param instrument_type: (required)
        :type instrument_type: str
        :param x_api_version:
        :type x_api_version: str
        :param x_idempotency_replayed:
        :type x_idempotency_replayed: bool
        :param x_idempotency_key:
        :type x_idempotency_key: str
        :param x_request_id:
        :type x_request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[CFFetchAllSavedInstruments], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'x_client_id',
            'x_client_secret',
            'customer_id',
            'instrument_type',
            'x_api_version',
            'x_idempotency_replayed',
            'x_idempotency_key',
            'x_request_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_all_saved_instruments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_client_id' is set
        if self.api_client.client_side_validation and local_var_params.get('x_client_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_client_id` when calling `fetch_all_saved_instruments`")  # noqa: E501
        # verify the required parameter 'x_client_secret' is set
        if self.api_client.client_side_validation and local_var_params.get('x_client_secret') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_client_secret` when calling `fetch_all_saved_instruments`")  # noqa: E501
        # verify the required parameter 'customer_id' is set
        if self.api_client.client_side_validation and local_var_params.get('customer_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `customer_id` when calling `fetch_all_saved_instruments`")  # noqa: E501
        # verify the required parameter 'instrument_type' is set
        if self.api_client.client_side_validation and local_var_params.get('instrument_type') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrument_type` when calling `fetch_all_saved_instruments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in local_var_params:
            path_params['customer_id'] = local_var_params['customer_id']  # noqa: E501

        query_params = []
        if local_var_params.get('instrument_type') is not None:  # noqa: E501
            query_params.append(('instrument_type', local_var_params['instrument_type']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))
        if 'x_client_id' in local_var_params:
            header_params['x-client-id'] = local_var_params['x_client_id']  # noqa: E501
        if 'x_client_secret' in local_var_params:
            header_params['x-client-secret'] = local_var_params['x_client_secret']  # noqa: E501
        if 'x_api_version' in local_var_params:
            header_params['x-api-version'] = local_var_params['x_api_version']  # noqa: E501
        if 'x_idempotency_replayed' in local_var_params:
            header_params['x-idempotency-replayed'] = local_var_params['x_idempotency_replayed']  # noqa: E501
        if 'x_idempotency_key' in local_var_params:
            header_params['x-idempotency-key'] = local_var_params['x_idempotency_key']  # noqa: E501
        if 'x_request_id' in local_var_params:
            header_params['x-request-id'] = local_var_params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "list[CFFetchAllSavedInstruments]",
        }

        return self.api_client.call_api(
            '/customers/{customer_id}/instruments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def fetch_cryptogram(self, x_client_id, x_client_secret, customer_id, instrument_id, **kwargs):  # noqa: E501
        """Fetch cryptogram for saved instrument  # noqa: E501

        To get the card network token, token expiry and cryptogram for a saved instrument using instrument id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_cryptogram(x_client_id, x_client_secret, customer_id, instrument_id, async_req=True)
        >>> result = thread.get()

        :param x_client_id: (required)
        :type x_client_id: str
        :param x_client_secret: (required)
        :type x_client_secret: str
        :param customer_id: (required)
        :type customer_id: str
        :param instrument_id: (required)
        :type instrument_id: str
        :param x_api_version:
        :type x_api_version: str
        :param x_idempotency_replayed:
        :type x_idempotency_replayed: bool
        :param x_idempotency_key:
        :type x_idempotency_key: str
        :param x_request_id:
        :type x_request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CFCryptogram
        """
        kwargs['_return_http_data_only'] = True
        return self.fetch_cryptogram_with_http_info(x_client_id, x_client_secret, customer_id, instrument_id, **kwargs)  # noqa: E501

    def fetch_cryptogram_with_http_info(self, x_client_id, x_client_secret, customer_id, instrument_id, **kwargs):  # noqa: E501
        """Fetch cryptogram for saved instrument  # noqa: E501

        To get the card network token, token expiry and cryptogram for a saved instrument using instrument id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_cryptogram_with_http_info(x_client_id, x_client_secret, customer_id, instrument_id, async_req=True)
        >>> result = thread.get()

        :param x_client_id: (required)
        :type x_client_id: str
        :param x_client_secret: (required)
        :type x_client_secret: str
        :param customer_id: (required)
        :type customer_id: str
        :param instrument_id: (required)
        :type instrument_id: str
        :param x_api_version:
        :type x_api_version: str
        :param x_idempotency_replayed:
        :type x_idempotency_replayed: bool
        :param x_idempotency_key:
        :type x_idempotency_key: str
        :param x_request_id:
        :type x_request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CFCryptogram, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'x_client_id',
            'x_client_secret',
            'customer_id',
            'instrument_id',
            'x_api_version',
            'x_idempotency_replayed',
            'x_idempotency_key',
            'x_request_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_cryptogram" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_client_id' is set
        if self.api_client.client_side_validation and local_var_params.get('x_client_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_client_id` when calling `fetch_cryptogram`")  # noqa: E501
        # verify the required parameter 'x_client_secret' is set
        if self.api_client.client_side_validation and local_var_params.get('x_client_secret') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_client_secret` when calling `fetch_cryptogram`")  # noqa: E501
        # verify the required parameter 'customer_id' is set
        if self.api_client.client_side_validation and local_var_params.get('customer_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `customer_id` when calling `fetch_cryptogram`")  # noqa: E501
        # verify the required parameter 'instrument_id' is set
        if self.api_client.client_side_validation and local_var_params.get('instrument_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrument_id` when calling `fetch_cryptogram`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in local_var_params:
            path_params['customer_id'] = local_var_params['customer_id']  # noqa: E501
        if 'instrument_id' in local_var_params:
            path_params['instrument_id'] = local_var_params['instrument_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'x_client_id' in local_var_params:
            header_params['x-client-id'] = local_var_params['x_client_id']  # noqa: E501
        if 'x_client_secret' in local_var_params:
            header_params['x-client-secret'] = local_var_params['x_client_secret']  # noqa: E501
        if 'x_api_version' in local_var_params:
            header_params['x-api-version'] = local_var_params['x_api_version']  # noqa: E501
        if 'x_idempotency_replayed' in local_var_params:
            header_params['x-idempotency-replayed'] = local_var_params['x_idempotency_replayed']  # noqa: E501
        if 'x_idempotency_key' in local_var_params:
            header_params['x-idempotency-key'] = local_var_params['x_idempotency_key']  # noqa: E501
        if 'x_request_id' in local_var_params:
            header_params['x-request-id'] = local_var_params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "CFCryptogram",
        }

        return self.api_client.call_api(
            '/customers/{customer_id}/instruments/{instrument_id}/cryptogram', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def fetch_specific_saved_instrument(self, x_client_id, x_client_secret, customer_id, instrument_id, **kwargs):  # noqa: E501
        """Fetch Single Saved Instrument  # noqa: E501

        To get specific saved instrument for a customer id and instrument id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_specific_saved_instrument(x_client_id, x_client_secret, customer_id, instrument_id, async_req=True)
        >>> result = thread.get()

        :param x_client_id: (required)
        :type x_client_id: str
        :param x_client_secret: (required)
        :type x_client_secret: str
        :param customer_id: (required)
        :type customer_id: str
        :param instrument_id: (required)
        :type instrument_id: str
        :param x_api_version:
        :type x_api_version: str
        :param x_idempotency_replayed:
        :type x_idempotency_replayed: bool
        :param x_idempotency_key:
        :type x_idempotency_key: str
        :param x_request_id:
        :type x_request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CFFetchAllSavedInstruments
        """
        kwargs['_return_http_data_only'] = True
        return self.fetch_specific_saved_instrument_with_http_info(x_client_id, x_client_secret, customer_id, instrument_id, **kwargs)  # noqa: E501

    def fetch_specific_saved_instrument_with_http_info(self, x_client_id, x_client_secret, customer_id, instrument_id, **kwargs):  # noqa: E501
        """Fetch Single Saved Instrument  # noqa: E501

        To get specific saved instrument for a customer id and instrument id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_specific_saved_instrument_with_http_info(x_client_id, x_client_secret, customer_id, instrument_id, async_req=True)
        >>> result = thread.get()

        :param x_client_id: (required)
        :type x_client_id: str
        :param x_client_secret: (required)
        :type x_client_secret: str
        :param customer_id: (required)
        :type customer_id: str
        :param instrument_id: (required)
        :type instrument_id: str
        :param x_api_version:
        :type x_api_version: str
        :param x_idempotency_replayed:
        :type x_idempotency_replayed: bool
        :param x_idempotency_key:
        :type x_idempotency_key: str
        :param x_request_id:
        :type x_request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CFFetchAllSavedInstruments, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'x_client_id',
            'x_client_secret',
            'customer_id',
            'instrument_id',
            'x_api_version',
            'x_idempotency_replayed',
            'x_idempotency_key',
            'x_request_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_specific_saved_instrument" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_client_id' is set
        if self.api_client.client_side_validation and local_var_params.get('x_client_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_client_id` when calling `fetch_specific_saved_instrument`")  # noqa: E501
        # verify the required parameter 'x_client_secret' is set
        if self.api_client.client_side_validation and local_var_params.get('x_client_secret') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_client_secret` when calling `fetch_specific_saved_instrument`")  # noqa: E501
        # verify the required parameter 'customer_id' is set
        if self.api_client.client_side_validation and local_var_params.get('customer_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `customer_id` when calling `fetch_specific_saved_instrument`")  # noqa: E501
        # verify the required parameter 'instrument_id' is set
        if self.api_client.client_side_validation and local_var_params.get('instrument_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrument_id` when calling `fetch_specific_saved_instrument`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in local_var_params:
            path_params['customer_id'] = local_var_params['customer_id']  # noqa: E501
        if 'instrument_id' in local_var_params:
            path_params['instrument_id'] = local_var_params['instrument_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'x_client_id' in local_var_params:
            header_params['x-client-id'] = local_var_params['x_client_id']  # noqa: E501
        if 'x_client_secret' in local_var_params:
            header_params['x-client-secret'] = local_var_params['x_client_secret']  # noqa: E501
        if 'x_api_version' in local_var_params:
            header_params['x-api-version'] = local_var_params['x_api_version']  # noqa: E501
        if 'x_idempotency_replayed' in local_var_params:
            header_params['x-idempotency-replayed'] = local_var_params['x_idempotency_replayed']  # noqa: E501
        if 'x_idempotency_key' in local_var_params:
            header_params['x-idempotency-key'] = local_var_params['x_idempotency_key']  # noqa: E501
        if 'x_request_id' in local_var_params:
            header_params['x-request-id'] = local_var_params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "CFFetchAllSavedInstruments",
        }

        return self.api_client.call_api(
            '/customers/{customer_id}/instruments/{instrument_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
