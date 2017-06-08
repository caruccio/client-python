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


class V1Parameter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, display_name=None, _from=None, generate=None, name=None, required=None, value=None):
        """
        V1Parameter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            '_from': 'str',
            'generate': 'str',
            'name': 'str',
            'required': 'bool',
            'value': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            '_from': 'from',
            'generate': 'generate',
            'name': 'name',
            'required': 'required',
            'value': 'value'
        }

        self._description = description
        self._display_name = display_name
        self.__from = _from
        self._generate = generate
        self._name = name
        self._required = required
        self._value = value

    @property
    def description(self):
        """
        Gets the description of this V1Parameter.
        Description of a parameter. Optional.

        :return: The description of this V1Parameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this V1Parameter.
        Description of a parameter. Optional.

        :param description: The description of this V1Parameter.
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this V1Parameter.
        Optional: The name that will show in UI instead of parameter 'Name'

        :return: The display_name of this V1Parameter.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this V1Parameter.
        Optional: The name that will show in UI instead of parameter 'Name'

        :param display_name: The display_name of this V1Parameter.
        :type: str
        """

        self._display_name = display_name

    @property
    def _from(self):
        """
        Gets the _from of this V1Parameter.
        From is an input value for the generator. Optional.

        :return: The _from of this V1Parameter.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1Parameter.
        From is an input value for the generator. Optional.

        :param _from: The _from of this V1Parameter.
        :type: str
        """

        self.__from = _from

    @property
    def generate(self):
        """
        Gets the generate of this V1Parameter.
        generate specifies the generator to be used to generate random string from an input value specified by From field. The result string is stored into Value field. If empty, no generator is being used, leaving the result Value untouched. Optional.  The only supported generator is \"expression\", which accepts a \"from\" value in the form of a simple regular expression containing the range expression \"[a-zA-Z0-9]\", and the length expression \"a{length}\".  Examples:  from             | value ----------------------------- \"test[0-9]{1}x\"  | \"test7x\" \"[0-1]{8}\"       | \"01001100\" \"0x[A-F0-9]{4}\"  | \"0xB3AF\" \"[a-zA-Z0-9]{8}\" | \"hW4yQU5i\"

        :return: The generate of this V1Parameter.
        :rtype: str
        """
        return self._generate

    @generate.setter
    def generate(self, generate):
        """
        Sets the generate of this V1Parameter.
        generate specifies the generator to be used to generate random string from an input value specified by From field. The result string is stored into Value field. If empty, no generator is being used, leaving the result Value untouched. Optional.  The only supported generator is \"expression\", which accepts a \"from\" value in the form of a simple regular expression containing the range expression \"[a-zA-Z0-9]\", and the length expression \"a{length}\".  Examples:  from             | value ----------------------------- \"test[0-9]{1}x\"  | \"test7x\" \"[0-1]{8}\"       | \"01001100\" \"0x[A-F0-9]{4}\"  | \"0xB3AF\" \"[a-zA-Z0-9]{8}\" | \"hW4yQU5i\"

        :param generate: The generate of this V1Parameter.
        :type: str
        """

        self._generate = generate

    @property
    def name(self):
        """
        Gets the name of this V1Parameter.
        Name must be set and it can be referenced in Template Items using ${PARAMETER_NAME}. Required.

        :return: The name of this V1Parameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Parameter.
        Name must be set and it can be referenced in Template Items using ${PARAMETER_NAME}. Required.

        :param name: The name of this V1Parameter.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def required(self):
        """
        Gets the required of this V1Parameter.
        Optional: Indicates the parameter must have a value.  Defaults to false.

        :return: The required of this V1Parameter.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this V1Parameter.
        Optional: Indicates the parameter must have a value.  Defaults to false.

        :param required: The required of this V1Parameter.
        :type: bool
        """

        self._required = required

    @property
    def value(self):
        """
        Gets the value of this V1Parameter.
        Value holds the Parameter data. If specified, the generator will be ignored. The value replaces all occurrences of the Parameter ${Name} expression during the Template to Config transformation. Optional.

        :return: The value of this V1Parameter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this V1Parameter.
        Value holds the Parameter data. If specified, the generator will be ignored. The value replaces all occurrences of the Parameter ${Name} expression during the Template to Config transformation. Optional.

        :param value: The value of this V1Parameter.
        :type: str
        """

        self._value = value

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
        if not isinstance(other, V1Parameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
