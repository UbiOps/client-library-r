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


class ProjectResourceUsage(object):
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
        'deployments': 'int',
        'deployment_versions': 'str',
        'pipelines': 'int',
        'pipeline_versions': 'str',
        'versions': 'int'
    }

    attribute_map = {
        'deployments': 'deployments',
        'deployment_versions': 'deployment_versions',
        'pipelines': 'pipelines',
        'pipeline_versions': 'pipeline_versions',
        'versions': 'versions'
    }

    def __init__(self, deployments=None, deployment_versions=None, pipelines=None, pipeline_versions=None, versions=None, local_vars_configuration=None):  # noqa: E501
        """ProjectResourceUsage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deployments = None
        self._deployment_versions = None
        self._pipelines = None
        self._pipeline_versions = None
        self._versions = None
        self.discriminator = None

        if deployments is not None:
            self.deployments = deployments
        if deployment_versions is not None:
            self.deployment_versions = deployment_versions
        if pipelines is not None:
            self.pipelines = pipelines
        if pipeline_versions is not None:
            self.pipeline_versions = pipeline_versions
        if versions is not None:
            self.versions = versions

    @property
    def deployments(self):
        """Gets the deployments of this ProjectResourceUsage.  # noqa: E501


        :return: The deployments of this ProjectResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this ProjectResourceUsage.


        :param deployments: The deployments of this ProjectResourceUsage.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                deployments is not None and not isinstance(deployments, int)):
            raise ValueError("Parameter `deployments` must be an integer")  # noqa: E501

        self._deployments = deployments

    @property
    def deployment_versions(self):
        """Gets the deployment_versions of this ProjectResourceUsage.  # noqa: E501


        :return: The deployment_versions of this ProjectResourceUsage.  # noqa: E501
        :rtype: str
        """
        return self._deployment_versions

    @deployment_versions.setter
    def deployment_versions(self, deployment_versions):
        """Sets the deployment_versions of this ProjectResourceUsage.


        :param deployment_versions: The deployment_versions of this ProjectResourceUsage.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                deployment_versions is not None and not isinstance(deployment_versions, str)):
            raise ValueError("Parameter `deployment_versions` must be a string")  # noqa: E501

        self._deployment_versions = deployment_versions

    @property
    def pipelines(self):
        """Gets the pipelines of this ProjectResourceUsage.  # noqa: E501


        :return: The pipelines of this ProjectResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._pipelines

    @pipelines.setter
    def pipelines(self, pipelines):
        """Sets the pipelines of this ProjectResourceUsage.


        :param pipelines: The pipelines of this ProjectResourceUsage.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                pipelines is not None and not isinstance(pipelines, int)):
            raise ValueError("Parameter `pipelines` must be an integer")  # noqa: E501

        self._pipelines = pipelines

    @property
    def pipeline_versions(self):
        """Gets the pipeline_versions of this ProjectResourceUsage.  # noqa: E501


        :return: The pipeline_versions of this ProjectResourceUsage.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_versions

    @pipeline_versions.setter
    def pipeline_versions(self, pipeline_versions):
        """Sets the pipeline_versions of this ProjectResourceUsage.


        :param pipeline_versions: The pipeline_versions of this ProjectResourceUsage.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pipeline_versions is not None and not isinstance(pipeline_versions, str)):
            raise ValueError("Parameter `pipeline_versions` must be a string")  # noqa: E501

        self._pipeline_versions = pipeline_versions

    @property
    def versions(self):
        """Gets the versions of this ProjectResourceUsage.  # noqa: E501


        :return: The versions of this ProjectResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this ProjectResourceUsage.


        :param versions: The versions of this ProjectResourceUsage.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                versions is not None and not isinstance(versions, int)):
            raise ValueError("Parameter `versions` must be an integer")  # noqa: E501

        self._versions = versions

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
        if not isinstance(other, ProjectResourceUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectResourceUsage):
            return True

        return self.to_dict() != other.to_dict()
