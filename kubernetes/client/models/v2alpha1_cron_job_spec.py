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


class V2alpha1CronJobSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, concurrency_policy=None, job_template=None, schedule=None, starting_deadline_seconds=None, suspend=None):
        """
        V2alpha1CronJobSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'concurrency_policy': 'str',
            'job_template': 'V2alpha1JobTemplateSpec',
            'schedule': 'str',
            'starting_deadline_seconds': 'int',
            'suspend': 'bool'
        }

        self.attribute_map = {
            'concurrency_policy': 'concurrencyPolicy',
            'job_template': 'jobTemplate',
            'schedule': 'schedule',
            'starting_deadline_seconds': 'startingDeadlineSeconds',
            'suspend': 'suspend'
        }

        self._concurrency_policy = concurrency_policy
        self._job_template = job_template
        self._schedule = schedule
        self._starting_deadline_seconds = starting_deadline_seconds
        self._suspend = suspend

    @property
    def concurrency_policy(self):
        """
        Gets the concurrency_policy of this V2alpha1CronJobSpec.
        ConcurrencyPolicy specifies how to treat concurrent executions of a Job.

        :return: The concurrency_policy of this V2alpha1CronJobSpec.
        :rtype: str
        """
        return self._concurrency_policy

    @concurrency_policy.setter
    def concurrency_policy(self, concurrency_policy):
        """
        Sets the concurrency_policy of this V2alpha1CronJobSpec.
        ConcurrencyPolicy specifies how to treat concurrent executions of a Job.

        :param concurrency_policy: The concurrency_policy of this V2alpha1CronJobSpec.
        :type: str
        """

        self._concurrency_policy = concurrency_policy

    @property
    def job_template(self):
        """
        Gets the job_template of this V2alpha1CronJobSpec.
        JobTemplate is the object that describes the job that will be created when executing a CronJob.

        :return: The job_template of this V2alpha1CronJobSpec.
        :rtype: V2alpha1JobTemplateSpec
        """
        return self._job_template

    @job_template.setter
    def job_template(self, job_template):
        """
        Sets the job_template of this V2alpha1CronJobSpec.
        JobTemplate is the object that describes the job that will be created when executing a CronJob.

        :param job_template: The job_template of this V2alpha1CronJobSpec.
        :type: V2alpha1JobTemplateSpec
        """
        if job_template is None:
            raise ValueError("Invalid value for `job_template`, must not be `None`")

        self._job_template = job_template

    @property
    def schedule(self):
        """
        Gets the schedule of this V2alpha1CronJobSpec.
        Schedule contains the schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.

        :return: The schedule of this V2alpha1CronJobSpec.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this V2alpha1CronJobSpec.
        Schedule contains the schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.

        :param schedule: The schedule of this V2alpha1CronJobSpec.
        :type: str
        """
        if schedule is None:
            raise ValueError("Invalid value for `schedule`, must not be `None`")

        self._schedule = schedule

    @property
    def starting_deadline_seconds(self):
        """
        Gets the starting_deadline_seconds of this V2alpha1CronJobSpec.
        Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.

        :return: The starting_deadline_seconds of this V2alpha1CronJobSpec.
        :rtype: int
        """
        return self._starting_deadline_seconds

    @starting_deadline_seconds.setter
    def starting_deadline_seconds(self, starting_deadline_seconds):
        """
        Sets the starting_deadline_seconds of this V2alpha1CronJobSpec.
        Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.

        :param starting_deadline_seconds: The starting_deadline_seconds of this V2alpha1CronJobSpec.
        :type: int
        """

        self._starting_deadline_seconds = starting_deadline_seconds

    @property
    def suspend(self):
        """
        Gets the suspend of this V2alpha1CronJobSpec.
        Suspend flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.

        :return: The suspend of this V2alpha1CronJobSpec.
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """
        Sets the suspend of this V2alpha1CronJobSpec.
        Suspend flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.

        :param suspend: The suspend of this V2alpha1CronJobSpec.
        :type: bool
        """

        self._suspend = suspend

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
        if not isinstance(other, V2alpha1CronJobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
