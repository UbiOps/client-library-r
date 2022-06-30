# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.  # noqa: E501

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ubiops.configuration import Configuration


class DeploymentVersionCreate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'version': 'str',
        'language': 'str',
        'memory_allocation': 'int',
        'instance_type': 'str',
        'maximum_instances': 'int',
        'minimum_instances': 'int',
        'maximum_idle_time': 'int',
        'description': 'str',
        'labels': 'dict(str, str)',
        'monitoring': 'str',
        'request_retention_time': 'int',
        'request_retention_mode': 'str',
        'default_notification_group': 'str',
        'maximum_queue_size_express': 'int',
        'maximum_queue_size_batch': 'int'
    }

    attribute_map = {
        'version': 'version',
        'language': 'language',
        'memory_allocation': 'memory_allocation',
        'instance_type': 'instance_type',
        'maximum_instances': 'maximum_instances',
        'minimum_instances': 'minimum_instances',
        'maximum_idle_time': 'maximum_idle_time',
        'description': 'description',
        'labels': 'labels',
        'monitoring': 'monitoring',
        'request_retention_time': 'request_retention_time',
        'request_retention_mode': 'request_retention_mode',
        'default_notification_group': 'default_notification_group',
        'maximum_queue_size_express': 'maximum_queue_size_express',
        'maximum_queue_size_batch': 'maximum_queue_size_batch'
    }

    def __init__(self, version=None, language='python3.7', memory_allocation=None, instance_type=None, maximum_instances=None, minimum_instances=None, maximum_idle_time=None, description=None, labels=None, monitoring=None, request_retention_time=None, request_retention_mode='full', default_notification_group=None, maximum_queue_size_express=None, maximum_queue_size_batch=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """DeploymentVersionCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._language = None
        self._memory_allocation = None
        self._instance_type = None
        self._maximum_instances = None
        self._minimum_instances = None
        self._maximum_idle_time = None
        self._description = None
        self._labels = None
        self._monitoring = None
        self._request_retention_time = None
        self._request_retention_mode = None
        self._default_notification_group = None
        self._maximum_queue_size_express = None
        self._maximum_queue_size_batch = None
        self.discriminator = None

        self.version = version
        if language is not None:
            self.language = language
        if memory_allocation is not None:
            self.memory_allocation = memory_allocation
        if instance_type is not None:
            self.instance_type = instance_type
        if maximum_instances is not None:
            self.maximum_instances = maximum_instances
        if minimum_instances is not None:
            self.minimum_instances = minimum_instances
        if maximum_idle_time is not None:
            self.maximum_idle_time = maximum_idle_time
        if description is not None:
            self.description = description
        self.labels = labels
        self.monitoring = monitoring
        if request_retention_time is not None:
            self.request_retention_time = request_retention_time
        if request_retention_mode is not None:
            self.request_retention_mode = request_retention_mode
        self.default_notification_group = default_notification_group
        if maximum_queue_size_express is not None:
            self.maximum_queue_size_express = maximum_queue_size_express
        if maximum_queue_size_batch is not None:
            self.maximum_queue_size_batch = maximum_queue_size_batch

    @property
    def version(self):
        """Gets the version of this DeploymentVersionCreate.  # noqa: E501


        :return: The version of this DeploymentVersionCreate.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeploymentVersionCreate.


        :param version: The version of this DeploymentVersionCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def language(self):
        """Gets the language of this DeploymentVersionCreate.  # noqa: E501


        :return: The language of this DeploymentVersionCreate.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DeploymentVersionCreate.


        :param language: The language of this DeploymentVersionCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                language is not None and not isinstance(language, str)):
            raise ValueError("Parameter `language` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                language is not None and len(language) < 1):
            raise ValueError("Invalid value for `language`, length must be greater than or equal to `1`")  # noqa: E501

        self._language = language

    @property
    def memory_allocation(self):
        """Gets the memory_allocation of this DeploymentVersionCreate.  # noqa: E501


        :return: The memory_allocation of this DeploymentVersionCreate.  # noqa: E501
        :rtype: int
        """
        return self._memory_allocation

    @memory_allocation.setter
    def memory_allocation(self, memory_allocation):
        """Sets the memory_allocation of this DeploymentVersionCreate.


        :param memory_allocation: The memory_allocation of this DeploymentVersionCreate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                memory_allocation is not None and not isinstance(memory_allocation, int)):
            raise ValueError("Parameter `memory_allocation` must be an integer")  # noqa: E501

        self._memory_allocation = memory_allocation

    @property
    def instance_type(self):
        """Gets the instance_type of this DeploymentVersionCreate.  # noqa: E501


        :return: The instance_type of this DeploymentVersionCreate.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this DeploymentVersionCreate.


        :param instance_type: The instance_type of this DeploymentVersionCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                instance_type is not None and not isinstance(instance_type, str)):
            raise ValueError("Parameter `instance_type` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                instance_type is not None and len(instance_type) < 1):
            raise ValueError("Invalid value for `instance_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._instance_type = instance_type

    @property
    def maximum_instances(self):
        """Gets the maximum_instances of this DeploymentVersionCreate.  # noqa: E501


        :return: The maximum_instances of this DeploymentVersionCreate.  # noqa: E501
        :rtype: int
        """
        return self._maximum_instances

    @maximum_instances.setter
    def maximum_instances(self, maximum_instances):
        """Sets the maximum_instances of this DeploymentVersionCreate.


        :param maximum_instances: The maximum_instances of this DeploymentVersionCreate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_instances is not None and not isinstance(maximum_instances, int)):
            raise ValueError("Parameter `maximum_instances` must be an integer")  # noqa: E501

        self._maximum_instances = maximum_instances

    @property
    def minimum_instances(self):
        """Gets the minimum_instances of this DeploymentVersionCreate.  # noqa: E501


        :return: The minimum_instances of this DeploymentVersionCreate.  # noqa: E501
        :rtype: int
        """
        return self._minimum_instances

    @minimum_instances.setter
    def minimum_instances(self, minimum_instances):
        """Sets the minimum_instances of this DeploymentVersionCreate.


        :param minimum_instances: The minimum_instances of this DeploymentVersionCreate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                minimum_instances is not None and not isinstance(minimum_instances, int)):
            raise ValueError("Parameter `minimum_instances` must be an integer")  # noqa: E501

        self._minimum_instances = minimum_instances

    @property
    def maximum_idle_time(self):
        """Gets the maximum_idle_time of this DeploymentVersionCreate.  # noqa: E501


        :return: The maximum_idle_time of this DeploymentVersionCreate.  # noqa: E501
        :rtype: int
        """
        return self._maximum_idle_time

    @maximum_idle_time.setter
    def maximum_idle_time(self, maximum_idle_time):
        """Sets the maximum_idle_time of this DeploymentVersionCreate.


        :param maximum_idle_time: The maximum_idle_time of this DeploymentVersionCreate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_idle_time is not None and not isinstance(maximum_idle_time, int)):
            raise ValueError("Parameter `maximum_idle_time` must be an integer")  # noqa: E501

        self._maximum_idle_time = maximum_idle_time

    @property
    def description(self):
        """Gets the description of this DeploymentVersionCreate.  # noqa: E501


        :return: The description of this DeploymentVersionCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeploymentVersionCreate.


        :param description: The description of this DeploymentVersionCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not isinstance(description, str)):
            raise ValueError("Parameter `description` must be a string")  # noqa: E501

        self._description = description

    @property
    def labels(self):
        """Gets the labels of this DeploymentVersionCreate.  # noqa: E501


        :return: The labels of this DeploymentVersionCreate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DeploymentVersionCreate.


        :param labels: The labels of this DeploymentVersionCreate.  # noqa: E501
        :type: dict(str, str)
        """
        if (self.local_vars_configuration.client_side_validation and
                labels is not None and not isinstance(labels, dict)):
            raise ValueError("Parameter `labels` must be a dictionary")  # noqa: E501

        self._labels = labels

    @property
    def monitoring(self):
        """Gets the monitoring of this DeploymentVersionCreate.  # noqa: E501


        :return: The monitoring of this DeploymentVersionCreate.  # noqa: E501
        :rtype: str
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """Sets the monitoring of this DeploymentVersionCreate.


        :param monitoring: The monitoring of this DeploymentVersionCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                monitoring is not None and not isinstance(monitoring, str)):
            raise ValueError("Parameter `monitoring` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                monitoring is not None and len(monitoring) < 1):
            raise ValueError("Invalid value for `monitoring`, length must be greater than or equal to `1`")  # noqa: E501

        self._monitoring = monitoring

    @property
    def request_retention_time(self):
        """Gets the request_retention_time of this DeploymentVersionCreate.  # noqa: E501


        :return: The request_retention_time of this DeploymentVersionCreate.  # noqa: E501
        :rtype: int
        """
        return self._request_retention_time

    @request_retention_time.setter
    def request_retention_time(self, request_retention_time):
        """Sets the request_retention_time of this DeploymentVersionCreate.


        :param request_retention_time: The request_retention_time of this DeploymentVersionCreate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                request_retention_time is not None and not isinstance(request_retention_time, int)):
            raise ValueError("Parameter `request_retention_time` must be an integer")  # noqa: E501

        self._request_retention_time = request_retention_time

    @property
    def request_retention_mode(self):
        """Gets the request_retention_mode of this DeploymentVersionCreate.  # noqa: E501


        :return: The request_retention_mode of this DeploymentVersionCreate.  # noqa: E501
        :rtype: str
        """
        return self._request_retention_mode

    @request_retention_mode.setter
    def request_retention_mode(self, request_retention_mode):
        """Sets the request_retention_mode of this DeploymentVersionCreate.


        :param request_retention_mode: The request_retention_mode of this DeploymentVersionCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                request_retention_mode is not None and not isinstance(request_retention_mode, str)):
            raise ValueError("Parameter `request_retention_mode` must be a string")  # noqa: E501
        allowed_values = ["none", "metadata", "full"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and request_retention_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `request_retention_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(request_retention_mode, allowed_values)
            )

        self._request_retention_mode = request_retention_mode

    @property
    def default_notification_group(self):
        """Gets the default_notification_group of this DeploymentVersionCreate.  # noqa: E501


        :return: The default_notification_group of this DeploymentVersionCreate.  # noqa: E501
        :rtype: str
        """
        return self._default_notification_group

    @default_notification_group.setter
    def default_notification_group(self, default_notification_group):
        """Sets the default_notification_group of this DeploymentVersionCreate.


        :param default_notification_group: The default_notification_group of this DeploymentVersionCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                default_notification_group is not None and not isinstance(default_notification_group, str)):
            raise ValueError("Parameter `default_notification_group` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                default_notification_group is not None and len(default_notification_group) < 1):
            raise ValueError("Invalid value for `default_notification_group`, length must be greater than or equal to `1`")  # noqa: E501

        self._default_notification_group = default_notification_group

    @property
    def maximum_queue_size_express(self):
        """Gets the maximum_queue_size_express of this DeploymentVersionCreate.  # noqa: E501


        :return: The maximum_queue_size_express of this DeploymentVersionCreate.  # noqa: E501
        :rtype: int
        """
        return self._maximum_queue_size_express

    @maximum_queue_size_express.setter
    def maximum_queue_size_express(self, maximum_queue_size_express):
        """Sets the maximum_queue_size_express of this DeploymentVersionCreate.


        :param maximum_queue_size_express: The maximum_queue_size_express of this DeploymentVersionCreate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_queue_size_express is not None and not isinstance(maximum_queue_size_express, int)):
            raise ValueError("Parameter `maximum_queue_size_express` must be an integer")  # noqa: E501

        self._maximum_queue_size_express = maximum_queue_size_express

    @property
    def maximum_queue_size_batch(self):
        """Gets the maximum_queue_size_batch of this DeploymentVersionCreate.  # noqa: E501


        :return: The maximum_queue_size_batch of this DeploymentVersionCreate.  # noqa: E501
        :rtype: int
        """
        return self._maximum_queue_size_batch

    @maximum_queue_size_batch.setter
    def maximum_queue_size_batch(self, maximum_queue_size_batch):
        """Sets the maximum_queue_size_batch of this DeploymentVersionCreate.


        :param maximum_queue_size_batch: The maximum_queue_size_batch of this DeploymentVersionCreate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_queue_size_batch is not None and not isinstance(maximum_queue_size_batch, int)):
            raise ValueError("Parameter `maximum_queue_size_batch` must be an integer")  # noqa: E501

        self._maximum_queue_size_batch = maximum_queue_size_batch

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeploymentVersionCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentVersionCreate):
            return True

        return self.to_dict() != other.to_dict()
