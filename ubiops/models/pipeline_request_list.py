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


class PipelineRequestList(object):
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
        'pipeline': 'str',
        'version': 'str',
        'status': 'str',
        'success': 'bool',
        'time_created': 'datetime',
        'time_started': 'datetime',
        'time_completed': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'pipeline': 'pipeline',
        'version': 'version',
        'status': 'status',
        'success': 'success',
        'time_created': 'time_created',
        'time_started': 'time_started',
        'time_completed': 'time_completed'
    }

    def __init__(self, id=None, pipeline=None, version=None, status=None, success=None, time_created=None, time_started=None, time_completed=None, local_vars_configuration=None):  # noqa: E501
        """PipelineRequestList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._pipeline = None
        self._version = None
        self._status = None
        self._success = None
        self._time_created = None
        self._time_started = None
        self._time_completed = None
        self.discriminator = None

        self.id = id
        self.pipeline = pipeline
        self.version = version
        self.status = status
        self.success = success
        self.time_created = time_created
        self.time_started = time_started
        self.time_completed = time_completed

    @property
    def id(self):
        """Gets the id of this PipelineRequestList.  # noqa: E501


        :return: The id of this PipelineRequestList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineRequestList.


        :param id: The id of this PipelineRequestList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def pipeline(self):
        """Gets the pipeline of this PipelineRequestList.  # noqa: E501


        :return: The pipeline of this PipelineRequestList.  # noqa: E501
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this PipelineRequestList.


        :param pipeline: The pipeline of this PipelineRequestList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pipeline is not None and not isinstance(pipeline, str)):
            raise ValueError("Parameter `pipeline` must be a string")  # noqa: E501

        self._pipeline = pipeline

    @property
    def version(self):
        """Gets the version of this PipelineRequestList.  # noqa: E501


        :return: The version of this PipelineRequestList.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PipelineRequestList.


        :param version: The version of this PipelineRequestList.  # noqa: E501
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
    def status(self):
        """Gets the status of this PipelineRequestList.  # noqa: E501


        :return: The status of this PipelineRequestList.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PipelineRequestList.


        :param status: The status of this PipelineRequestList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")  # noqa: E501
        allowed_values = ["pending", "processing", "completed", "failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def success(self):
        """Gets the success of this PipelineRequestList.  # noqa: E501


        :return: The success of this PipelineRequestList.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PipelineRequestList.


        :param success: The success of this PipelineRequestList.  # noqa: E501
        :type: bool
        """
        if (self.local_vars_configuration.client_side_validation and
                success is not None and not isinstance(success, bool)):
            raise ValueError("Parameter `success` must be a boolean")  # noqa: E501

        self._success = success

    @property
    def time_created(self):
        """Gets the time_created of this PipelineRequestList.  # noqa: E501


        :return: The time_created of this PipelineRequestList.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this PipelineRequestList.


        :param time_created: The time_created of this PipelineRequestList.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and time_created is None:  # noqa: E501
            raise ValueError("Invalid value for `time_created`, must not be `None`")  # noqa: E501

        self._time_created = time_created

    @property
    def time_started(self):
        """Gets the time_started of this PipelineRequestList.  # noqa: E501


        :return: The time_started of this PipelineRequestList.  # noqa: E501
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """Sets the time_started of this PipelineRequestList.


        :param time_started: The time_started of this PipelineRequestList.  # noqa: E501
        :type: datetime
        """

        self._time_started = time_started

    @property
    def time_completed(self):
        """Gets the time_completed of this PipelineRequestList.  # noqa: E501


        :return: The time_completed of this PipelineRequestList.  # noqa: E501
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """Sets the time_completed of this PipelineRequestList.


        :param time_completed: The time_completed of this PipelineRequestList.  # noqa: E501
        :type: datetime
        """

        self._time_completed = time_completed

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
        if not isinstance(other, PipelineRequestList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineRequestList):
            return True

        return self.to_dict() != other.to_dict()
