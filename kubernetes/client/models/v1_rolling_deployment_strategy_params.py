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


class V1RollingDeploymentStrategyParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, interval_seconds=None, max_surge=None, max_unavailable=None, post=None, pre=None, timeout_seconds=None, update_period_seconds=None):
        """
        V1RollingDeploymentStrategyParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interval_seconds': 'int',
            'max_surge': 'str',
            'max_unavailable': 'str',
            'post': 'V1LifecycleHook',
            'pre': 'V1LifecycleHook',
            'timeout_seconds': 'int',
            'update_period_seconds': 'int'
        }

        self.attribute_map = {
            'interval_seconds': 'intervalSeconds',
            'max_surge': 'maxSurge',
            'max_unavailable': 'maxUnavailable',
            'post': 'post',
            'pre': 'pre',
            'timeout_seconds': 'timeoutSeconds',
            'update_period_seconds': 'updatePeriodSeconds'
        }

        self._interval_seconds = interval_seconds
        self._max_surge = max_surge
        self._max_unavailable = max_unavailable
        self._post = post
        self._pre = pre
        self._timeout_seconds = timeout_seconds
        self._update_period_seconds = update_period_seconds

    @property
    def interval_seconds(self):
        """
        Gets the interval_seconds of this V1RollingDeploymentStrategyParams.
        IntervalSeconds is the time to wait between polling deployment status after update. If the value is nil, a default will be used.

        :return: The interval_seconds of this V1RollingDeploymentStrategyParams.
        :rtype: int
        """
        return self._interval_seconds

    @interval_seconds.setter
    def interval_seconds(self, interval_seconds):
        """
        Sets the interval_seconds of this V1RollingDeploymentStrategyParams.
        IntervalSeconds is the time to wait between polling deployment status after update. If the value is nil, a default will be used.

        :param interval_seconds: The interval_seconds of this V1RollingDeploymentStrategyParams.
        :type: int
        """

        self._interval_seconds = interval_seconds

    @property
    def max_surge(self):
        """
        Gets the max_surge of this V1RollingDeploymentStrategyParams.
        MaxSurge is the maximum number of pods that can be scheduled above the original number of pods. Value can be an absolute number (ex: 5) or a percentage of total pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up.  This cannot be 0 if MaxUnavailable is 0. By default, 25% is used.  Example: when this is set to 30%, the new RC can be scaled up by 30% immediately when the rolling update starts. Once old pods have been killed, new RC can be scaled up further, ensuring that total number of pods running at any time during the update is atmost 130% of original pods.

        :return: The max_surge of this V1RollingDeploymentStrategyParams.
        :rtype: str
        """
        return self._max_surge

    @max_surge.setter
    def max_surge(self, max_surge):
        """
        Sets the max_surge of this V1RollingDeploymentStrategyParams.
        MaxSurge is the maximum number of pods that can be scheduled above the original number of pods. Value can be an absolute number (ex: 5) or a percentage of total pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up.  This cannot be 0 if MaxUnavailable is 0. By default, 25% is used.  Example: when this is set to 30%, the new RC can be scaled up by 30% immediately when the rolling update starts. Once old pods have been killed, new RC can be scaled up further, ensuring that total number of pods running at any time during the update is atmost 130% of original pods.

        :param max_surge: The max_surge of this V1RollingDeploymentStrategyParams.
        :type: str
        """

        self._max_surge = max_surge

    @property
    def max_unavailable(self):
        """
        Gets the max_unavailable of this V1RollingDeploymentStrategyParams.
        MaxUnavailable is the maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total pods at the start of update (ex: 10%). Absolute number is calculated from percentage by rounding down.  This cannot be 0 if MaxSurge is 0. By default, 25% is used.  Example: when this is set to 30%, the old RC can be scaled down by 30% immediately when the rolling update starts. Once new pods are ready, old RC can be scaled down further, followed by scaling up the new RC, ensuring that at least 70% of original number of pods are available at all times during the update.

        :return: The max_unavailable of this V1RollingDeploymentStrategyParams.
        :rtype: str
        """
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, max_unavailable):
        """
        Sets the max_unavailable of this V1RollingDeploymentStrategyParams.
        MaxUnavailable is the maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total pods at the start of update (ex: 10%). Absolute number is calculated from percentage by rounding down.  This cannot be 0 if MaxSurge is 0. By default, 25% is used.  Example: when this is set to 30%, the old RC can be scaled down by 30% immediately when the rolling update starts. Once new pods are ready, old RC can be scaled down further, followed by scaling up the new RC, ensuring that at least 70% of original number of pods are available at all times during the update.

        :param max_unavailable: The max_unavailable of this V1RollingDeploymentStrategyParams.
        :type: str
        """

        self._max_unavailable = max_unavailable

    @property
    def post(self):
        """
        Gets the post of this V1RollingDeploymentStrategyParams.
        Post is a lifecycle hook which is executed after the strategy has finished all deployment logic. All LifecycleHookFailurePolicy values are supported.

        :return: The post of this V1RollingDeploymentStrategyParams.
        :rtype: V1LifecycleHook
        """
        return self._post

    @post.setter
    def post(self, post):
        """
        Sets the post of this V1RollingDeploymentStrategyParams.
        Post is a lifecycle hook which is executed after the strategy has finished all deployment logic. All LifecycleHookFailurePolicy values are supported.

        :param post: The post of this V1RollingDeploymentStrategyParams.
        :type: V1LifecycleHook
        """

        self._post = post

    @property
    def pre(self):
        """
        Gets the pre of this V1RollingDeploymentStrategyParams.
        Pre is a lifecycle hook which is executed before the deployment process begins. All LifecycleHookFailurePolicy values are supported.

        :return: The pre of this V1RollingDeploymentStrategyParams.
        :rtype: V1LifecycleHook
        """
        return self._pre

    @pre.setter
    def pre(self, pre):
        """
        Sets the pre of this V1RollingDeploymentStrategyParams.
        Pre is a lifecycle hook which is executed before the deployment process begins. All LifecycleHookFailurePolicy values are supported.

        :param pre: The pre of this V1RollingDeploymentStrategyParams.
        :type: V1LifecycleHook
        """

        self._pre = pre

    @property
    def timeout_seconds(self):
        """
        Gets the timeout_seconds of this V1RollingDeploymentStrategyParams.
        TimeoutSeconds is the time to wait for updates before giving up. If the value is nil, a default will be used.

        :return: The timeout_seconds of this V1RollingDeploymentStrategyParams.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """
        Sets the timeout_seconds of this V1RollingDeploymentStrategyParams.
        TimeoutSeconds is the time to wait for updates before giving up. If the value is nil, a default will be used.

        :param timeout_seconds: The timeout_seconds of this V1RollingDeploymentStrategyParams.
        :type: int
        """

        self._timeout_seconds = timeout_seconds

    @property
    def update_period_seconds(self):
        """
        Gets the update_period_seconds of this V1RollingDeploymentStrategyParams.
        UpdatePeriodSeconds is the time to wait between individual pod updates. If the value is nil, a default will be used.

        :return: The update_period_seconds of this V1RollingDeploymentStrategyParams.
        :rtype: int
        """
        return self._update_period_seconds

    @update_period_seconds.setter
    def update_period_seconds(self, update_period_seconds):
        """
        Sets the update_period_seconds of this V1RollingDeploymentStrategyParams.
        UpdatePeriodSeconds is the time to wait between individual pod updates. If the value is nil, a default will be used.

        :param update_period_seconds: The update_period_seconds of this V1RollingDeploymentStrategyParams.
        :type: int
        """

        self._update_period_seconds = update_period_seconds

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
        if not isinstance(other, V1RollingDeploymentStrategyParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other