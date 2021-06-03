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


class AttachmentsCreate(object):
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
        'destination_name': 'str',
        'sources': 'list[AttachmentSourcesCreate]'
    }

    attribute_map = {
        'destination_name': 'destination_name',
        'sources': 'sources'
    }

    def __init__(self, destination_name=None, sources=None, local_vars_configuration=None):  # noqa: E501
        """AttachmentsCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._destination_name = None
        self._sources = None
        self.discriminator = None

        self.destination_name = destination_name
        self.sources = sources

    @property
    def destination_name(self):
        """Gets the destination_name of this AttachmentsCreate.  # noqa: E501


        :return: The destination_name of this AttachmentsCreate.  # noqa: E501
        :rtype: str
        """
        return self._destination_name

    @destination_name.setter
    def destination_name(self, destination_name):
        """Sets the destination_name of this AttachmentsCreate.


        :param destination_name: The destination_name of this AttachmentsCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and destination_name is None:  # noqa: E501
            raise ValueError("Invalid value for `destination_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                destination_name is not None and not isinstance(destination_name, str)):
            raise ValueError("Parameter `destination_name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                destination_name is not None and len(destination_name) < 1):
            raise ValueError("Invalid value for `destination_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._destination_name = destination_name

    @property
    def sources(self):
        """Gets the sources of this AttachmentsCreate.  # noqa: E501


        :return: The sources of this AttachmentsCreate.  # noqa: E501
        :rtype: list[AttachmentSourcesCreate]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this AttachmentsCreate.


        :param sources: The sources of this AttachmentsCreate.  # noqa: E501
        :type: list[AttachmentSourcesCreate]
        """
        if self.local_vars_configuration.client_side_validation and sources is None:  # noqa: E501
            raise ValueError("Invalid value for `sources`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sources is not None and not isinstance(sources, list)):
            raise ValueError("Parameter `sources` must be a list")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sources is not None:
            from ubiops.models.attachment_sources_create import AttachmentSourcesCreate

            sources = [
                AttachmentSourcesCreate(**item) if isinstance(item, dict) else item  # noqa: E501
                for item in sources
            ]

        self._sources = sources

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
        if not isinstance(other, AttachmentsCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentsCreate):
            return True

        return self.to_dict() != other.to_dict()
