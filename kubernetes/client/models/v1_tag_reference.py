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


class V1TagReference(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, annotations=None, _from=None, generation=None, import_policy=None, name=None, reference=None, reference_policy=None):
        """
        V1TagReference - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'annotations': 'dict(str, str)',
            '_from': 'V1ObjectReference',
            'generation': 'int',
            'import_policy': 'V1TagImportPolicy',
            'name': 'str',
            'reference': 'bool',
            'reference_policy': 'V1TagReferencePolicy'
        }

        self.attribute_map = {
            'annotations': 'annotations',
            '_from': 'from',
            'generation': 'generation',
            'import_policy': 'importPolicy',
            'name': 'name',
            'reference': 'reference',
            'reference_policy': 'referencePolicy'
        }

        self._annotations = annotations
        self.__from = _from
        self._generation = generation
        self._import_policy = import_policy
        self._name = name
        self._reference = reference
        self._reference_policy = reference_policy

    @property
    def annotations(self):
        """
        Gets the annotations of this V1TagReference.
        Annotations associated with images using this tag

        :return: The annotations of this V1TagReference.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """
        Sets the annotations of this V1TagReference.
        Annotations associated with images using this tag

        :param annotations: The annotations of this V1TagReference.
        :type: dict(str, str)
        """
        if annotations is None:
            raise ValueError("Invalid value for `annotations`, must not be `None`")

        self._annotations = annotations

    @property
    def _from(self):
        """
        Gets the _from of this V1TagReference.
        From is a reference to an image stream tag or image stream this tag should track

        :return: The _from of this V1TagReference.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1TagReference.
        From is a reference to an image stream tag or image stream this tag should track

        :param _from: The _from of this V1TagReference.
        :type: V1ObjectReference
        """

        self.__from = _from

    @property
    def generation(self):
        """
        Gets the generation of this V1TagReference.
        Generation is the image stream generation that updated this tag - setting it to 0 is an indication that the generation must be updated. Legacy clients will send this as nil, which means the client doesn't know or care.

        :return: The generation of this V1TagReference.
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """
        Sets the generation of this V1TagReference.
        Generation is the image stream generation that updated this tag - setting it to 0 is an indication that the generation must be updated. Legacy clients will send this as nil, which means the client doesn't know or care.

        :param generation: The generation of this V1TagReference.
        :type: int
        """
        if generation is None:
            raise ValueError("Invalid value for `generation`, must not be `None`")

        self._generation = generation

    @property
    def import_policy(self):
        """
        Gets the import_policy of this V1TagReference.
        Import is information that controls how images may be imported by the server.

        :return: The import_policy of this V1TagReference.
        :rtype: V1TagImportPolicy
        """
        return self._import_policy

    @import_policy.setter
    def import_policy(self, import_policy):
        """
        Sets the import_policy of this V1TagReference.
        Import is information that controls how images may be imported by the server.

        :param import_policy: The import_policy of this V1TagReference.
        :type: V1TagImportPolicy
        """

        self._import_policy = import_policy

    @property
    def name(self):
        """
        Gets the name of this V1TagReference.
        Name of the tag

        :return: The name of this V1TagReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1TagReference.
        Name of the tag

        :param name: The name of this V1TagReference.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def reference(self):
        """
        Gets the reference of this V1TagReference.
        Reference states if the tag will be imported. Default value is false, which means the tag will be imported.

        :return: The reference of this V1TagReference.
        :rtype: bool
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this V1TagReference.
        Reference states if the tag will be imported. Default value is false, which means the tag will be imported.

        :param reference: The reference of this V1TagReference.
        :type: bool
        """

        self._reference = reference

    @property
    def reference_policy(self):
        """
        Gets the reference_policy of this V1TagReference.
        ReferencePolicy defines how other components should consume the image

        :return: The reference_policy of this V1TagReference.
        :rtype: V1TagReferencePolicy
        """
        return self._reference_policy

    @reference_policy.setter
    def reference_policy(self, reference_policy):
        """
        Sets the reference_policy of this V1TagReference.
        ReferencePolicy defines how other components should consume the image

        :param reference_policy: The reference_policy of this V1TagReference.
        :type: V1TagReferencePolicy
        """

        self._reference_policy = reference_policy

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
        if not isinstance(other, V1TagReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
