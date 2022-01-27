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


class Logs(object):
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
        'log': 'str',
        'date': 'str',
        'deployment_name': 'str',
        'deployment_version': 'str',
        'pipeline_name': 'str',
        'pipeline_version': 'str',
        'pipeline_object_name': 'str',
        'deployment_request_id': 'str',
        'pipeline_request_id': 'str',
        'build_id': 'str',
        'system': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'log': 'log',
        'date': 'date',
        'deployment_name': 'deployment_name',
        'deployment_version': 'deployment_version',
        'pipeline_name': 'pipeline_name',
        'pipeline_version': 'pipeline_version',
        'pipeline_object_name': 'pipeline_object_name',
        'deployment_request_id': 'deployment_request_id',
        'pipeline_request_id': 'pipeline_request_id',
        'build_id': 'build_id',
        'system': 'system'
    }

    def __init__(self, id=None, log=None, date=None, deployment_name=None, deployment_version=None, pipeline_name=None, pipeline_version=None, pipeline_object_name=None, deployment_request_id=None, pipeline_request_id=None, build_id=None, system=None, local_vars_configuration=None):  # noqa: E501
        """Logs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._log = None
        self._date = None
        self._deployment_name = None
        self._deployment_version = None
        self._pipeline_name = None
        self._pipeline_version = None
        self._pipeline_object_name = None
        self._deployment_request_id = None
        self._pipeline_request_id = None
        self._build_id = None
        self._system = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if log is not None:
            self.log = log
        if date is not None:
            self.date = date
        if deployment_name is not None:
            self.deployment_name = deployment_name
        if deployment_version is not None:
            self.deployment_version = deployment_version
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if pipeline_version is not None:
            self.pipeline_version = pipeline_version
        if pipeline_object_name is not None:
            self.pipeline_object_name = pipeline_object_name
        if deployment_request_id is not None:
            self.deployment_request_id = deployment_request_id
        if pipeline_request_id is not None:
            self.pipeline_request_id = pipeline_request_id
        if build_id is not None:
            self.build_id = build_id
        if system is not None:
            self.system = system

    @property
    def id(self):
        """Gets the id of this Logs.  # noqa: E501


        :return: The id of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Logs.


        :param id: The id of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def log(self):
        """Gets the log of this Logs.  # noqa: E501


        :return: The log of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this Logs.


        :param log: The log of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                log is not None and not isinstance(log, str)):
            raise ValueError("Parameter `log` must be a string")  # noqa: E501

        self._log = log

    @property
    def date(self):
        """Gets the date of this Logs.  # noqa: E501


        :return: The date of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Logs.


        :param date: The date of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                date is not None and not isinstance(date, str)):
            raise ValueError("Parameter `date` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                date is not None and len(date) < 1):
            raise ValueError("Invalid value for `date`, length must be greater than or equal to `1`")  # noqa: E501

        self._date = date

    @property
    def deployment_name(self):
        """Gets the deployment_name of this Logs.  # noqa: E501


        :return: The deployment_name of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        """Sets the deployment_name of this Logs.


        :param deployment_name: The deployment_name of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                deployment_name is not None and not isinstance(deployment_name, str)):
            raise ValueError("Parameter `deployment_name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                deployment_name is not None and len(deployment_name) < 1):
            raise ValueError("Invalid value for `deployment_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._deployment_name = deployment_name

    @property
    def deployment_version(self):
        """Gets the deployment_version of this Logs.  # noqa: E501


        :return: The deployment_version of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._deployment_version

    @deployment_version.setter
    def deployment_version(self, deployment_version):
        """Sets the deployment_version of this Logs.


        :param deployment_version: The deployment_version of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                deployment_version is not None and not isinstance(deployment_version, str)):
            raise ValueError("Parameter `deployment_version` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                deployment_version is not None and len(deployment_version) < 1):
            raise ValueError("Invalid value for `deployment_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._deployment_version = deployment_version

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this Logs.  # noqa: E501


        :return: The pipeline_name of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this Logs.


        :param pipeline_name: The pipeline_name of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pipeline_name is not None and not isinstance(pipeline_name, str)):
            raise ValueError("Parameter `pipeline_name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                pipeline_name is not None and len(pipeline_name) < 1):
            raise ValueError("Invalid value for `pipeline_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._pipeline_name = pipeline_name

    @property
    def pipeline_version(self):
        """Gets the pipeline_version of this Logs.  # noqa: E501


        :return: The pipeline_version of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_version

    @pipeline_version.setter
    def pipeline_version(self, pipeline_version):
        """Sets the pipeline_version of this Logs.


        :param pipeline_version: The pipeline_version of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pipeline_version is not None and not isinstance(pipeline_version, str)):
            raise ValueError("Parameter `pipeline_version` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                pipeline_version is not None and len(pipeline_version) < 1):
            raise ValueError("Invalid value for `pipeline_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._pipeline_version = pipeline_version

    @property
    def pipeline_object_name(self):
        """Gets the pipeline_object_name of this Logs.  # noqa: E501


        :return: The pipeline_object_name of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_object_name

    @pipeline_object_name.setter
    def pipeline_object_name(self, pipeline_object_name):
        """Sets the pipeline_object_name of this Logs.


        :param pipeline_object_name: The pipeline_object_name of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pipeline_object_name is not None and not isinstance(pipeline_object_name, str)):
            raise ValueError("Parameter `pipeline_object_name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                pipeline_object_name is not None and len(pipeline_object_name) < 1):
            raise ValueError("Invalid value for `pipeline_object_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._pipeline_object_name = pipeline_object_name

    @property
    def deployment_request_id(self):
        """Gets the deployment_request_id of this Logs.  # noqa: E501


        :return: The deployment_request_id of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._deployment_request_id

    @deployment_request_id.setter
    def deployment_request_id(self, deployment_request_id):
        """Sets the deployment_request_id of this Logs.


        :param deployment_request_id: The deployment_request_id of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                deployment_request_id is not None and not isinstance(deployment_request_id, str)):
            raise ValueError("Parameter `deployment_request_id` must be a string")  # noqa: E501

        self._deployment_request_id = deployment_request_id

    @property
    def pipeline_request_id(self):
        """Gets the pipeline_request_id of this Logs.  # noqa: E501


        :return: The pipeline_request_id of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_request_id

    @pipeline_request_id.setter
    def pipeline_request_id(self, pipeline_request_id):
        """Sets the pipeline_request_id of this Logs.


        :param pipeline_request_id: The pipeline_request_id of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pipeline_request_id is not None and not isinstance(pipeline_request_id, str)):
            raise ValueError("Parameter `pipeline_request_id` must be a string")  # noqa: E501

        self._pipeline_request_id = pipeline_request_id

    @property
    def build_id(self):
        """Gets the build_id of this Logs.  # noqa: E501


        :return: The build_id of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this Logs.


        :param build_id: The build_id of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                build_id is not None and not isinstance(build_id, str)):
            raise ValueError("Parameter `build_id` must be a string")  # noqa: E501

        self._build_id = build_id

    @property
    def system(self):
        """Gets the system of this Logs.  # noqa: E501


        :return: The system of this Logs.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this Logs.


        :param system: The system of this Logs.  # noqa: E501
        :type: bool
        """
        if (self.local_vars_configuration.client_side_validation and
                system is not None and not isinstance(system, bool)):
            raise ValueError("Parameter `system` must be a boolean")  # noqa: E501

        self._system = system

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
        if not isinstance(other, Logs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Logs):
            return True

        return self.to_dict() != other.to_dict()