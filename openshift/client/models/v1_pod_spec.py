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


class V1PodSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active_deadline_seconds=None, containers=None, dns_policy=None, host_ipc=None, host_network=None, host_pid=None, hostname=None, image_pull_secrets=None, node_name=None, node_selector=None, restart_policy=None, security_context=None, service_account=None, service_account_name=None, subdomain=None, termination_grace_period_seconds=None, volumes=None):
        """
        V1PodSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active_deadline_seconds': 'int',
            'containers': 'list[V1Container]',
            'dns_policy': 'str',
            'host_ipc': 'bool',
            'host_network': 'bool',
            'host_pid': 'bool',
            'hostname': 'str',
            'image_pull_secrets': 'list[V1LocalObjectReference]',
            'node_name': 'str',
            'node_selector': 'dict(str, str)',
            'restart_policy': 'str',
            'security_context': 'V1PodSecurityContext',
            'service_account': 'str',
            'service_account_name': 'str',
            'subdomain': 'str',
            'termination_grace_period_seconds': 'int',
            'volumes': 'list[V1Volume]'
        }

        self.attribute_map = {
            'active_deadline_seconds': 'activeDeadlineSeconds',
            'containers': 'containers',
            'dns_policy': 'dnsPolicy',
            'host_ipc': 'hostIPC',
            'host_network': 'hostNetwork',
            'host_pid': 'hostPID',
            'hostname': 'hostname',
            'image_pull_secrets': 'imagePullSecrets',
            'node_name': 'nodeName',
            'node_selector': 'nodeSelector',
            'restart_policy': 'restartPolicy',
            'security_context': 'securityContext',
            'service_account': 'serviceAccount',
            'service_account_name': 'serviceAccountName',
            'subdomain': 'subdomain',
            'termination_grace_period_seconds': 'terminationGracePeriodSeconds',
            'volumes': 'volumes'
        }

        self._active_deadline_seconds = active_deadline_seconds
        self._containers = containers
        self._dns_policy = dns_policy
        self._host_ipc = host_ipc
        self._host_network = host_network
        self._host_pid = host_pid
        self._hostname = hostname
        self._image_pull_secrets = image_pull_secrets
        self._node_name = node_name
        self._node_selector = node_selector
        self._restart_policy = restart_policy
        self._security_context = security_context
        self._service_account = service_account
        self._service_account_name = service_account_name
        self._subdomain = subdomain
        self._termination_grace_period_seconds = termination_grace_period_seconds
        self._volumes = volumes

    @property
    def active_deadline_seconds(self):
        """
        Gets the active_deadline_seconds of this V1PodSpec.
        Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

        :return: The active_deadline_seconds of this V1PodSpec.
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """
        Sets the active_deadline_seconds of this V1PodSpec.
        Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

        :param active_deadline_seconds: The active_deadline_seconds of this V1PodSpec.
        :type: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def containers(self):
        """
        Gets the containers of this V1PodSpec.
        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/containers

        :return: The containers of this V1PodSpec.
        :rtype: list[V1Container]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """
        Sets the containers of this V1PodSpec.
        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/containers

        :param containers: The containers of this V1PodSpec.
        :type: list[V1Container]
        """
        if containers is None:
            raise ValueError("Invalid value for `containers`, must not be `None`")

        self._containers = containers

    @property
    def dns_policy(self):
        """
        Gets the dns_policy of this V1PodSpec.
        Set DNS policy for containers within the pod. One of 'ClusterFirst' or 'Default'. Defaults to \"ClusterFirst\".

        :return: The dns_policy of this V1PodSpec.
        :rtype: str
        """
        return self._dns_policy

    @dns_policy.setter
    def dns_policy(self, dns_policy):
        """
        Sets the dns_policy of this V1PodSpec.
        Set DNS policy for containers within the pod. One of 'ClusterFirst' or 'Default'. Defaults to \"ClusterFirst\".

        :param dns_policy: The dns_policy of this V1PodSpec.
        :type: str
        """

        self._dns_policy = dns_policy

    @property
    def host_ipc(self):
        """
        Gets the host_ipc of this V1PodSpec.
        Use the host's ipc namespace. Optional: Default to false.

        :return: The host_ipc of this V1PodSpec.
        :rtype: bool
        """
        return self._host_ipc

    @host_ipc.setter
    def host_ipc(self, host_ipc):
        """
        Sets the host_ipc of this V1PodSpec.
        Use the host's ipc namespace. Optional: Default to false.

        :param host_ipc: The host_ipc of this V1PodSpec.
        :type: bool
        """

        self._host_ipc = host_ipc

    @property
    def host_network(self):
        """
        Gets the host_network of this V1PodSpec.
        Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

        :return: The host_network of this V1PodSpec.
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """
        Sets the host_network of this V1PodSpec.
        Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

        :param host_network: The host_network of this V1PodSpec.
        :type: bool
        """

        self._host_network = host_network

    @property
    def host_pid(self):
        """
        Gets the host_pid of this V1PodSpec.
        Use the host's pid namespace. Optional: Default to false.

        :return: The host_pid of this V1PodSpec.
        :rtype: bool
        """
        return self._host_pid

    @host_pid.setter
    def host_pid(self, host_pid):
        """
        Sets the host_pid of this V1PodSpec.
        Use the host's pid namespace. Optional: Default to false.

        :param host_pid: The host_pid of this V1PodSpec.
        :type: bool
        """

        self._host_pid = host_pid

    @property
    def hostname(self):
        """
        Gets the hostname of this V1PodSpec.
        Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

        :return: The hostname of this V1PodSpec.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this V1PodSpec.
        Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

        :param hostname: The hostname of this V1PodSpec.
        :type: str
        """

        self._hostname = hostname

    @property
    def image_pull_secrets(self):
        """
        Gets the image_pull_secrets of this V1PodSpec.
        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod

        :return: The image_pull_secrets of this V1PodSpec.
        :rtype: list[V1LocalObjectReference]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """
        Sets the image_pull_secrets of this V1PodSpec.
        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod

        :param image_pull_secrets: The image_pull_secrets of this V1PodSpec.
        :type: list[V1LocalObjectReference]
        """

        self._image_pull_secrets = image_pull_secrets

    @property
    def node_name(self):
        """
        Gets the node_name of this V1PodSpec.
        NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

        :return: The node_name of this V1PodSpec.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """
        Sets the node_name of this V1PodSpec.
        NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

        :param node_name: The node_name of this V1PodSpec.
        :type: str
        """

        self._node_name = node_name

    @property
    def node_selector(self):
        """
        Gets the node_selector of this V1PodSpec.
        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: http://kubernetes.io/docs/user-guide/node-selection/README

        :return: The node_selector of this V1PodSpec.
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """
        Sets the node_selector of this V1PodSpec.
        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: http://kubernetes.io/docs/user-guide/node-selection/README

        :param node_selector: The node_selector of this V1PodSpec.
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def restart_policy(self):
        """
        Gets the restart_policy of this V1PodSpec.
        Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: http://kubernetes.io/docs/user-guide/pod-states#restartpolicy

        :return: The restart_policy of this V1PodSpec.
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """
        Sets the restart_policy of this V1PodSpec.
        Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: http://kubernetes.io/docs/user-guide/pod-states#restartpolicy

        :param restart_policy: The restart_policy of this V1PodSpec.
        :type: str
        """

        self._restart_policy = restart_policy

    @property
    def security_context(self):
        """
        Gets the security_context of this V1PodSpec.
        SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

        :return: The security_context of this V1PodSpec.
        :rtype: V1PodSecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """
        Sets the security_context of this V1PodSpec.
        SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

        :param security_context: The security_context of this V1PodSpec.
        :type: V1PodSecurityContext
        """

        self._security_context = security_context

    @property
    def service_account(self):
        """
        Gets the service_account of this V1PodSpec.
        DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

        :return: The service_account of this V1PodSpec.
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """
        Sets the service_account of this V1PodSpec.
        DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

        :param service_account: The service_account of this V1PodSpec.
        :type: str
        """

        self._service_account = service_account

    @property
    def service_account_name(self):
        """
        Gets the service_account_name of this V1PodSpec.
        ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: http://releases.k8s.io/HEAD/docs/design/service_accounts.md

        :return: The service_account_name of this V1PodSpec.
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """
        Sets the service_account_name of this V1PodSpec.
        ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: http://releases.k8s.io/HEAD/docs/design/service_accounts.md

        :param service_account_name: The service_account_name of this V1PodSpec.
        :type: str
        """

        self._service_account_name = service_account_name

    @property
    def subdomain(self):
        """
        Gets the subdomain of this V1PodSpec.
        If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.

        :return: The subdomain of this V1PodSpec.
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """
        Sets the subdomain of this V1PodSpec.
        If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.

        :param subdomain: The subdomain of this V1PodSpec.
        :type: str
        """

        self._subdomain = subdomain

    @property
    def termination_grace_period_seconds(self):
        """
        Gets the termination_grace_period_seconds of this V1PodSpec.
        Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

        :return: The termination_grace_period_seconds of this V1PodSpec.
        :rtype: int
        """
        return self._termination_grace_period_seconds

    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, termination_grace_period_seconds):
        """
        Sets the termination_grace_period_seconds of this V1PodSpec.
        Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

        :param termination_grace_period_seconds: The termination_grace_period_seconds of this V1PodSpec.
        :type: int
        """

        self._termination_grace_period_seconds = termination_grace_period_seconds

    @property
    def volumes(self):
        """
        Gets the volumes of this V1PodSpec.
        List of volumes that can be mounted by containers belonging to the pod. More info: http://kubernetes.io/docs/user-guide/volumes

        :return: The volumes of this V1PodSpec.
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this V1PodSpec.
        List of volumes that can be mounted by containers belonging to the pod. More info: http://kubernetes.io/docs/user-guide/volumes

        :param volumes: The volumes of this V1PodSpec.
        :type: list[V1Volume]
        """

        self._volumes = volumes

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
        if not isinstance(other, V1PodSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other