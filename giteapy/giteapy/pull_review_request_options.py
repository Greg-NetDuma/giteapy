# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.16.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class PullReviewRequestOptions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'reviewers': 'list[str]',
        'team_reviewers': 'list[str]'
    }

    attribute_map = {
        'reviewers': 'reviewers',
        'team_reviewers': 'team_reviewers'
    }

    def __init__(self, reviewers=None, team_reviewers=None, _configuration=None):  # noqa: E501
        """PullReviewRequestOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._reviewers = None
        self._team_reviewers = None
        self.discriminator = None

        if reviewers is not None:
            self.reviewers = reviewers
        if team_reviewers is not None:
            self.team_reviewers = team_reviewers

    @property
    def reviewers(self):
        """Gets the reviewers of this PullReviewRequestOptions.  # noqa: E501


        :return: The reviewers of this PullReviewRequestOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._reviewers

    @reviewers.setter
    def reviewers(self, reviewers):
        """Sets the reviewers of this PullReviewRequestOptions.


        :param reviewers: The reviewers of this PullReviewRequestOptions.  # noqa: E501
        :type: list[str]
        """

        self._reviewers = reviewers

    @property
    def team_reviewers(self):
        """Gets the team_reviewers of this PullReviewRequestOptions.  # noqa: E501


        :return: The team_reviewers of this PullReviewRequestOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._team_reviewers

    @team_reviewers.setter
    def team_reviewers(self, team_reviewers):
        """Sets the team_reviewers of this PullReviewRequestOptions.


        :param team_reviewers: The team_reviewers of this PullReviewRequestOptions.  # noqa: E501
        :type: list[str]
        """

        self._team_reviewers = team_reviewers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PullReviewRequestOptions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PullReviewRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PullReviewRequestOptions):
            return True

        return self.to_dict() != other.to_dict()