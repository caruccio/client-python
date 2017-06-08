# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1GitBuildSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, http_proxy=None, https_proxy=None, no_proxy=None, ref=None, uri=None):
        """
        V1GitBuildSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'http_proxy': 'str',
            'https_proxy': 'str',
            'no_proxy': 'str',
            'ref': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'http_proxy': 'httpProxy',
            'https_proxy': 'httpsProxy',
            'no_proxy': 'noProxy',
            'ref': 'ref',
            'uri': 'uri'
        }

        self._http_proxy = http_proxy
        self._https_proxy = https_proxy
        self._no_proxy = no_proxy
        self._ref = ref
        self._uri = uri

    @property
    def http_proxy(self):
        """
        Gets the http_proxy of this V1GitBuildSource.
        httpProxy is a proxy used to reach the git repository over http

        :return: The http_proxy of this V1GitBuildSource.
        :rtype: str
        """
        return self._http_proxy

    @http_proxy.setter
    def http_proxy(self, http_proxy):
        """
        Sets the http_proxy of this V1GitBuildSource.
        httpProxy is a proxy used to reach the git repository over http

        :param http_proxy: The http_proxy of this V1GitBuildSource.
        :type: str
        """

        self._http_proxy = http_proxy

    @property
    def https_proxy(self):
        """
        Gets the https_proxy of this V1GitBuildSource.
        httpsProxy is a proxy used to reach the git repository over https

        :return: The https_proxy of this V1GitBuildSource.
        :rtype: str
        """
        return self._https_proxy

    @https_proxy.setter
    def https_proxy(self, https_proxy):
        """
        Sets the https_proxy of this V1GitBuildSource.
        httpsProxy is a proxy used to reach the git repository over https

        :param https_proxy: The https_proxy of this V1GitBuildSource.
        :type: str
        """

        self._https_proxy = https_proxy

    @property
    def no_proxy(self):
        """
        Gets the no_proxy of this V1GitBuildSource.
        noProxy is the list of domains for which the proxy should not be used

        :return: The no_proxy of this V1GitBuildSource.
        :rtype: str
        """
        return self._no_proxy

    @no_proxy.setter
    def no_proxy(self, no_proxy):
        """
        Sets the no_proxy of this V1GitBuildSource.
        noProxy is the list of domains for which the proxy should not be used

        :param no_proxy: The no_proxy of this V1GitBuildSource.
        :type: str
        """

        self._no_proxy = no_proxy

    @property
    def ref(self):
        """
        Gets the ref of this V1GitBuildSource.
        ref is the branch/tag/ref to build.

        :return: The ref of this V1GitBuildSource.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this V1GitBuildSource.
        ref is the branch/tag/ref to build.

        :param ref: The ref of this V1GitBuildSource.
        :type: str
        """

        self._ref = ref

    @property
    def uri(self):
        """
        Gets the uri of this V1GitBuildSource.
        uri points to the source that will be built. The structure of the source will depend on the type of build to run

        :return: The uri of this V1GitBuildSource.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this V1GitBuildSource.
        uri points to the source that will be built. The structure of the source will depend on the type of build to run

        :param uri: The uri of this V1GitBuildSource.
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")

        self._uri = uri

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1GitBuildSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
