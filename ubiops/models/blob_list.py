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


class BlobList(object):
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
        'id': 'str',
        'created_by': 'str',
        'creation_date': 'str',
        'last_updated': 'str',
        'filename': 'str',
        'size': 'int',
        'ttl': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'created_by',
        'creation_date': 'creation_date',
        'last_updated': 'last_updated',
        'filename': 'filename',
        'size': 'size',
        'ttl': 'ttl'
    }

    def __init__(self, id=None, created_by=None, creation_date=None, last_updated=None, filename=None, size=None, ttl=None, local_vars_configuration=None):  # noqa: E501
        """BlobList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_by = None
        self._creation_date = None
        self._last_updated = None
        self._filename = None
        self._size = None
        self._ttl = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_by is not None:
            self.created_by = created_by
        if creation_date is not None:
            self.creation_date = creation_date
        if last_updated is not None:
            self.last_updated = last_updated
        self.filename = filename
        self.size = size
        if ttl is not None:
            self.ttl = ttl

    @property
    def id(self):
        """Gets the id of this BlobList.  # noqa: E501


        :return: The id of this BlobList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BlobList.


        :param id: The id of this BlobList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this BlobList.  # noqa: E501


        :return: The created_by of this BlobList.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this BlobList.


        :param created_by: The created_by of this BlobList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                created_by is not None and not isinstance(created_by, str)):
            raise ValueError("Parameter `created_by` must be a string")  # noqa: E501

        self._created_by = created_by

    @property
    def creation_date(self):
        """Gets the creation_date of this BlobList.  # noqa: E501


        :return: The creation_date of this BlobList.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this BlobList.


        :param creation_date: The creation_date of this BlobList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                creation_date is not None and not isinstance(creation_date, str)):
            raise ValueError("Parameter `creation_date` must be a string")  # noqa: E501

        self._creation_date = creation_date

    @property
    def last_updated(self):
        """Gets the last_updated of this BlobList.  # noqa: E501


        :return: The last_updated of this BlobList.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this BlobList.


        :param last_updated: The last_updated of this BlobList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_updated is not None and not isinstance(last_updated, str)):
            raise ValueError("Parameter `last_updated` must be a string")  # noqa: E501

        self._last_updated = last_updated

    @property
    def filename(self):
        """Gets the filename of this BlobList.  # noqa: E501


        :return: The filename of this BlobList.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this BlobList.


        :param filename: The filename of this BlobList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and filename is None:  # noqa: E501
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filename is not None and not isinstance(filename, str)):
            raise ValueError("Parameter `filename` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                filename is not None and len(filename) > 512):
            raise ValueError("Invalid value for `filename`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filename is not None and len(filename) < 1):
            raise ValueError("Invalid value for `filename`, length must be greater than or equal to `1`")  # noqa: E501

        self._filename = filename

    @property
    def size(self):
        """Gets the size of this BlobList.  # noqa: E501


        :return: The size of this BlobList.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BlobList.


        :param size: The size of this BlobList.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size is not None and not isinstance(size, int)):
            raise ValueError("Parameter `size` must be an integer")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                size is not None and size < 0):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

    @property
    def ttl(self):
        """Gets the ttl of this BlobList.  # noqa: E501


        :return: The ttl of this BlobList.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this BlobList.


        :param ttl: The ttl of this BlobList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                ttl is not None and not isinstance(ttl, int)):
            raise ValueError("Parameter `ttl` must be an integer")  # noqa: E501

        self._ttl = ttl

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
        if not isinstance(other, BlobList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlobList):
            return True

        return self.to_dict() != other.to_dict()