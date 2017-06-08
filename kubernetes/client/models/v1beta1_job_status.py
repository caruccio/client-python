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


class V1beta1JobStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active=None, completion_time=None, conditions=None, failed=None, start_time=None, succeeded=None):
        """
        V1beta1JobStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active': 'int',
            'completion_time': 'datetime',
            'conditions': 'list[V1beta1JobCondition]',
            'failed': 'int',
            'start_time': 'datetime',
            'succeeded': 'int'
        }

        self.attribute_map = {
            'active': 'active',
            'completion_time': 'completionTime',
            'conditions': 'conditions',
            'failed': 'failed',
            'start_time': 'startTime',
            'succeeded': 'succeeded'
        }

        self._active = active
        self._completion_time = completion_time
        self._conditions = conditions
        self._failed = failed
        self._start_time = start_time
        self._succeeded = succeeded

    @property
    def active(self):
        """
        Gets the active of this V1beta1JobStatus.
        Active is the number of actively running pods.

        :return: The active of this V1beta1JobStatus.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this V1beta1JobStatus.
        Active is the number of actively running pods.

        :param active: The active of this V1beta1JobStatus.
        :type: int
        """

        self._active = active

    @property
    def completion_time(self):
        """
        Gets the completion_time of this V1beta1JobStatus.
        CompletionTime represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.

        :return: The completion_time of this V1beta1JobStatus.
        :rtype: datetime
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """
        Sets the completion_time of this V1beta1JobStatus.
        CompletionTime represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.

        :param completion_time: The completion_time of this V1beta1JobStatus.
        :type: datetime
        """

        self._completion_time = completion_time

    @property
    def conditions(self):
        """
        Gets the conditions of this V1beta1JobStatus.
        Conditions represent the latest available observations of an object's current state. More info: http://kubernetes.io/docs/user-guide/jobs

        :return: The conditions of this V1beta1JobStatus.
        :rtype: list[V1beta1JobCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1beta1JobStatus.
        Conditions represent the latest available observations of an object's current state. More info: http://kubernetes.io/docs/user-guide/jobs

        :param conditions: The conditions of this V1beta1JobStatus.
        :type: list[V1beta1JobCondition]
        """

        self._conditions = conditions

    @property
    def failed(self):
        """
        Gets the failed of this V1beta1JobStatus.
        Failed is the number of pods which reached Phase Failed.

        :return: The failed of this V1beta1JobStatus.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """
        Sets the failed of this V1beta1JobStatus.
        Failed is the number of pods which reached Phase Failed.

        :param failed: The failed of this V1beta1JobStatus.
        :type: int
        """

        self._failed = failed

    @property
    def start_time(self):
        """
        Gets the start_time of this V1beta1JobStatus.
        StartTime represents time when the job was acknowledged by the Job Manager. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.

        :return: The start_time of this V1beta1JobStatus.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this V1beta1JobStatus.
        StartTime represents time when the job was acknowledged by the Job Manager. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.

        :param start_time: The start_time of this V1beta1JobStatus.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def succeeded(self):
        """
        Gets the succeeded of this V1beta1JobStatus.
        Succeeded is the number of pods which reached Phase Succeeded.

        :return: The succeeded of this V1beta1JobStatus.
        :rtype: int
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """
        Sets the succeeded of this V1beta1JobStatus.
        Succeeded is the number of pods which reached Phase Succeeded.

        :param succeeded: The succeeded of this V1beta1JobStatus.
        :type: int
        """

        self._succeeded = succeeded

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
        if not isinstance(other, V1beta1JobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
