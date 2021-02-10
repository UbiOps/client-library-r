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


class UsagePerMonth(object):
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
        'object_type': 'str',
        'metric': 'str',
        'usage': 'list[UsagePerMonthMetric]'
    }

    attribute_map = {
        'object_type': 'object_type',
        'metric': 'metric',
        'usage': 'usage'
    }

    def __init__(self, object_type=None, metric=None, usage=None, local_vars_configuration=None):  # noqa: E501
        """UsagePerMonth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._object_type = None
        self._metric = None
        self._usage = None
        self.discriminator = None

        self.object_type = object_type
        self.metric = metric
        self.usage = usage

    @property
    def object_type(self):
        """Gets the object_type of this UsagePerMonth.  # noqa: E501


        :return: The object_type of this UsagePerMonth.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this UsagePerMonth.


        :param object_type: The object_type of this UsagePerMonth.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and object_type is None:  # noqa: E501
            raise ValueError("Invalid value for `object_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                object_type is not None and not isinstance(object_type, str)):
            raise ValueError("Parameter `object_type` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                object_type is not None and len(object_type) < 1):
            raise ValueError("Invalid value for `object_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._object_type = object_type

    @property
    def metric(self):
        """Gets the metric of this UsagePerMonth.  # noqa: E501


        :return: The metric of this UsagePerMonth.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this UsagePerMonth.


        :param metric: The metric of this UsagePerMonth.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and metric is None:  # noqa: E501
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                metric is not None and not isinstance(metric, str)):
            raise ValueError("Parameter `metric` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                metric is not None and len(metric) < 1):
            raise ValueError("Invalid value for `metric`, length must be greater than or equal to `1`")  # noqa: E501

        self._metric = metric

    @property
    def usage(self):
        """Gets the usage of this UsagePerMonth.  # noqa: E501


        :return: The usage of this UsagePerMonth.  # noqa: E501
        :rtype: list[UsagePerMonthMetric]
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this UsagePerMonth.


        :param usage: The usage of this UsagePerMonth.  # noqa: E501
        :type: list[UsagePerMonthMetric]
        """
        if self.local_vars_configuration.client_side_validation and usage is None:  # noqa: E501
            raise ValueError("Invalid value for `usage`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                usage is not None and not isinstance(usage, list)):
            raise ValueError("Parameter `usage` must be a list")  # noqa: E501

        self._usage = usage

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
        if not isinstance(other, UsagePerMonth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsagePerMonth):
            return True

        return self.to_dict() != other.to_dict()
