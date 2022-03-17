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


class ProjectCreate(object):
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
        'name': 'str',
        'organization_name': 'str',
        'advanced_permissions': 'bool',
        'credits': 'float'
    }

    attribute_map = {
        'name': 'name',
        'organization_name': 'organization_name',
        'advanced_permissions': 'advanced_permissions',
        'credits': 'credits'
    }

    def __init__(self, name=None, organization_name=None, advanced_permissions=False, credits=None, local_vars_configuration=None):  # noqa: E501
        """ProjectCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._organization_name = None
        self._advanced_permissions = None
        self._credits = None
        self.discriminator = None

        self.name = name
        self.organization_name = organization_name
        if advanced_permissions is not None:
            self.advanced_permissions = advanced_permissions
        self.credits = credits

    @property
    def name(self):
        """Gets the name of this ProjectCreate.  # noqa: E501


        :return: The name of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectCreate.


        :param name: The name of this ProjectCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def organization_name(self):
        """Gets the organization_name of this ProjectCreate.  # noqa: E501


        :return: The organization_name of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this ProjectCreate.


        :param organization_name: The organization_name of this ProjectCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organization_name is None:  # noqa: E501
            raise ValueError("Invalid value for `organization_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                organization_name is not None and not isinstance(organization_name, str)):
            raise ValueError("Parameter `organization_name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                organization_name is not None and len(organization_name) < 1):
            raise ValueError("Invalid value for `organization_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._organization_name = organization_name

    @property
    def advanced_permissions(self):
        """Gets the advanced_permissions of this ProjectCreate.  # noqa: E501


        :return: The advanced_permissions of this ProjectCreate.  # noqa: E501
        :rtype: bool
        """
        return self._advanced_permissions

    @advanced_permissions.setter
    def advanced_permissions(self, advanced_permissions):
        """Sets the advanced_permissions of this ProjectCreate.


        :param advanced_permissions: The advanced_permissions of this ProjectCreate.  # noqa: E501
        :type: bool
        """
        if (self.local_vars_configuration.client_side_validation and
                advanced_permissions is not None and not isinstance(advanced_permissions, bool)):
            raise ValueError("Parameter `advanced_permissions` must be a boolean")  # noqa: E501

        self._advanced_permissions = advanced_permissions

    @property
    def credits(self):
        """Gets the credits of this ProjectCreate.  # noqa: E501


        :return: The credits of this ProjectCreate.  # noqa: E501
        :rtype: float
        """
        return self._credits

    @credits.setter
    def credits(self, credits):
        """Sets the credits of this ProjectCreate.


        :param credits: The credits of this ProjectCreate.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                credits is not None and not isinstance(credits, float)):
            raise ValueError("Parameter `credits` must be a float")  # noqa: E501

        self._credits = credits

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
        if not isinstance(other, ProjectCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectCreate):
            return True

        return self.to_dict() != other.to_dict()
