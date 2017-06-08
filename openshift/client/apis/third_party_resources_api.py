# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ThirdPartyResourcesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_third_party_resource(self, namespace, fqdn, resource, body, **kwargs):
        """
        Create a Resource
        Creates a third party resource of the type specified
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_third_party_resource(namespace, fqdn, resource, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param object body: The JSON schema of the Resource to create. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_third_party_resource_with_http_info(namespace, fqdn, resource, body, **kwargs)
        else:
            (data) = self.create_third_party_resource_with_http_info(namespace, fqdn, resource, body, **kwargs)
            return data

    def create_third_party_resource_with_http_info(self, namespace, fqdn, resource, body, **kwargs):
        """
        Create a Resource
        Creates a third party resource of the type specified
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_third_party_resource_with_http_info(namespace, fqdn, resource, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param object body: The JSON schema of the Resource to create. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'fqdn', 'resource', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_third_party_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params) or (params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `create_third_party_resource`")
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `create_third_party_resource`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `create_third_party_resource`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_third_party_resource`")


        collection_formats = {}

        resource_path = '/apis/{fqdn}/v1/namespaces/{namespace}/{resource}'.replace('{format}', 'json')
        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_third_party_resource(self, body, **kwargs):
        """
        Deletes a specific Resource
        Deletes the specified Resource in the specified namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_third_party_resource(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param V1DeleteOptions body: (required)
        :param int grace_period_seconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
        :param bool orphan_dependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both.
        :param str propagation_policy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_third_party_resource_with_http_info(body, **kwargs)
        else:
            (data) = self.delete_third_party_resource_with_http_info(body, **kwargs)
            return data

    def delete_third_party_resource_with_http_info(self, body, **kwargs):
        """
        Deletes a specific Resource
        Deletes the specified Resource in the specified namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_third_party_resource_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param V1DeleteOptions body: (required)
        :param int grace_period_seconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
        :param bool orphan_dependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both.
        :param str propagation_policy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'grace_period_seconds', 'orphan_dependents', 'propagation_policy']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_third_party_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_third_party_resource`")


        collection_formats = {}

        resource_path = '/apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name}'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'grace_period_seconds' in params:
            query_params['gracePeriodSeconds'] = params['grace_period_seconds']
        if 'orphan_dependents' in params:
            query_params['orphanDependents'] = params['orphan_dependents']
        if 'propagation_policy' in params:
            query_params['propagationPolicy'] = params['propagation_policy']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_third_party_resource(self, namespace, name, fqdn, resource, **kwargs):
        """
        Gets a specific Resource
        Returns a specific Resource in a namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_third_party_resource(namespace, name, fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str name: The Resource's name (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_third_party_resource_with_http_info(namespace, name, fqdn, resource, **kwargs)
        else:
            (data) = self.get_third_party_resource_with_http_info(namespace, name, fqdn, resource, **kwargs)
            return data

    def get_third_party_resource_with_http_info(self, namespace, name, fqdn, resource, **kwargs):
        """
        Gets a specific Resource
        Returns a specific Resource in a namespace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_third_party_resource_with_http_info(namespace, name, fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str name: The Resource's name (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'name', 'fqdn', 'resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_third_party_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params) or (params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `get_third_party_resource`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_third_party_resource`")
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `get_third_party_resource`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `get_third_party_resource`")


        collection_formats = {}

        resource_path = '/apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name}'.replace('{format}', 'json')
        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']
        if 'name' in params:
            path_params['name'] = params['name']
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_third_party_resource(self, fqdn, resource, **kwargs):
        """
        Gets Resources
        Returns a list of Resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_third_party_resource(fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_third_party_resource_with_http_info(fqdn, resource, **kwargs)
        else:
            (data) = self.list_third_party_resource_with_http_info(fqdn, resource, **kwargs)
            return data

    def list_third_party_resource_with_http_info(self, fqdn, resource, **kwargs):
        """
        Gets Resources
        Returns a list of Resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_third_party_resource_with_http_info(fqdn, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fqdn', 'resource', 'watch']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_third_party_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `list_third_party_resource`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `list_third_party_resource`")


        collection_formats = {}

        resource_path = '/apis/{fqdn}/v1/{resource}'.replace('{format}', 'json')
        path_params = {}
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}
        if 'watch' in params:
            query_params['watch'] = params['watch']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_third_party_resource(self, namespace, fqdn, resource, body, **kwargs):
        """
        Update a Resource
        Update the specified third party resource of the type specified
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_third_party_resource(namespace, fqdn, resource, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param object body: The JSON schema of the Resource to create. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_third_party_resource_with_http_info(namespace, fqdn, resource, body, **kwargs)
        else:
            (data) = self.update_third_party_resource_with_http_info(namespace, fqdn, resource, body, **kwargs)
            return data

    def update_third_party_resource_with_http_info(self, namespace, fqdn, resource, body, **kwargs):
        """
        Update a Resource
        Update the specified third party resource of the type specified
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_third_party_resource_with_http_info(namespace, fqdn, resource, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str namespace: The Resource's namespace (required)
        :param str fqdn: The Third party Resource fqdn (required)
        :param str resource: The Resource type (required)
        :param object body: The JSON schema of the Resource to create. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'fqdn', 'resource', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_third_party_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params) or (params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `update_third_party_resource`")
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params) or (params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `update_third_party_resource`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `update_third_party_resource`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_third_party_resource`")


        collection_formats = {}

        resource_path = '/apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name}'.replace('{format}', 'json')
        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)