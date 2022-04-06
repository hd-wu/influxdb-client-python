# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TemplateSummaryDiff(object):
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
        'buckets': 'list[TemplateSummaryDiffBuckets]',
        'checks': 'list[TemplateSummaryDiffChecks]',
        'dashboards': 'list[TemplateSummaryDiffDashboards]',
        'labels': 'list[TemplateSummaryDiffLabels]',
        'label_mappings': 'list[TemplateSummaryDiffLabelMappings]',
        'notification_endpoints': 'list[TemplateSummaryDiffNotificationEndpoints]',
        'notification_rules': 'list[TemplateSummaryDiffNotificationRules]',
        'tasks': 'list[TemplateSummaryDiffTasks]',
        'telegraf_configs': 'list[TemplateSummaryDiffTelegrafConfigs]',
        'variables': 'list[TemplateSummaryDiffVariables]'
    }

    attribute_map = {
        'buckets': 'buckets',
        'checks': 'checks',
        'dashboards': 'dashboards',
        'labels': 'labels',
        'label_mappings': 'labelMappings',
        'notification_endpoints': 'notificationEndpoints',
        'notification_rules': 'notificationRules',
        'tasks': 'tasks',
        'telegraf_configs': 'telegrafConfigs',
        'variables': 'variables'
    }

    def __init__(self, buckets=None, checks=None, dashboards=None, labels=None, label_mappings=None, notification_endpoints=None, notification_rules=None, tasks=None, telegraf_configs=None, variables=None):  # noqa: E501,D401,D403
        """TemplateSummaryDiff - a model defined in OpenAPI."""  # noqa: E501
        self._buckets = None
        self._checks = None
        self._dashboards = None
        self._labels = None
        self._label_mappings = None
        self._notification_endpoints = None
        self._notification_rules = None
        self._tasks = None
        self._telegraf_configs = None
        self._variables = None
        self.discriminator = None

        if buckets is not None:
            self.buckets = buckets
        if checks is not None:
            self.checks = checks
        if dashboards is not None:
            self.dashboards = dashboards
        if labels is not None:
            self.labels = labels
        if label_mappings is not None:
            self.label_mappings = label_mappings
        if notification_endpoints is not None:
            self.notification_endpoints = notification_endpoints
        if notification_rules is not None:
            self.notification_rules = notification_rules
        if tasks is not None:
            self.tasks = tasks
        if telegraf_configs is not None:
            self.telegraf_configs = telegraf_configs
        if variables is not None:
            self.variables = variables

    @property
    def buckets(self):
        """Get the buckets of this TemplateSummaryDiff.

        :return: The buckets of this TemplateSummaryDiff.
        :rtype: list[TemplateSummaryDiffBuckets]
        """  # noqa: E501
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Set the buckets of this TemplateSummaryDiff.

        :param buckets: The buckets of this TemplateSummaryDiff.
        :type: list[TemplateSummaryDiffBuckets]
        """  # noqa: E501
        self._buckets = buckets

    @property
    def checks(self):
        """Get the checks of this TemplateSummaryDiff.

        :return: The checks of this TemplateSummaryDiff.
        :rtype: list[TemplateSummaryDiffChecks]
        """  # noqa: E501
        return self._checks

    @checks.setter
    def checks(self, checks):
        """Set the checks of this TemplateSummaryDiff.

        :param checks: The checks of this TemplateSummaryDiff.
        :type: list[TemplateSummaryDiffChecks]
        """  # noqa: E501
        self._checks = checks

    @property
    def dashboards(self):
        """Get the dashboards of this TemplateSummaryDiff.

        :return: The dashboards of this TemplateSummaryDiff.
        :rtype: list[TemplateSummaryDiffDashboards]
        """  # noqa: E501
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """Set the dashboards of this TemplateSummaryDiff.

        :param dashboards: The dashboards of this TemplateSummaryDiff.
        :type: list[TemplateSummaryDiffDashboards]
        """  # noqa: E501
        self._dashboards = dashboards

    @property
    def labels(self):
        """Get the labels of this TemplateSummaryDiff.

        :return: The labels of this TemplateSummaryDiff.
        :rtype: list[TemplateSummaryDiffLabels]
        """  # noqa: E501
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Set the labels of this TemplateSummaryDiff.

        :param labels: The labels of this TemplateSummaryDiff.
        :type: list[TemplateSummaryDiffLabels]
        """  # noqa: E501
        self._labels = labels

    @property
    def label_mappings(self):
        """Get the label_mappings of this TemplateSummaryDiff.

        :return: The label_mappings of this TemplateSummaryDiff.
        :rtype: list[TemplateSummaryDiffLabelMappings]
        """  # noqa: E501
        return self._label_mappings

    @label_mappings.setter
    def label_mappings(self, label_mappings):
        """Set the label_mappings of this TemplateSummaryDiff.

        :param label_mappings: The label_mappings of this TemplateSummaryDiff.
        :type: list[TemplateSummaryDiffLabelMappings]
        """  # noqa: E501
        self._label_mappings = label_mappings

    @property
    def notification_endpoints(self):
        """Get the notification_endpoints of this TemplateSummaryDiff.

        :return: The notification_endpoints of this TemplateSummaryDiff.
        :rtype: list[TemplateSummaryDiffNotificationEndpoints]
        """  # noqa: E501
        return self._notification_endpoints

    @notification_endpoints.setter
    def notification_endpoints(self, notification_endpoints):
        """Set the notification_endpoints of this TemplateSummaryDiff.

        :param notification_endpoints: The notification_endpoints of this TemplateSummaryDiff.
        :type: list[TemplateSummaryDiffNotificationEndpoints]
        """  # noqa: E501
        self._notification_endpoints = notification_endpoints

    @property
    def notification_rules(self):
        """Get the notification_rules of this TemplateSummaryDiff.

        :return: The notification_rules of this TemplateSummaryDiff.
        :rtype: list[TemplateSummaryDiffNotificationRules]
        """  # noqa: E501
        return self._notification_rules

    @notification_rules.setter
    def notification_rules(self, notification_rules):
        """Set the notification_rules of this TemplateSummaryDiff.

        :param notification_rules: The notification_rules of this TemplateSummaryDiff.
        :type: list[TemplateSummaryDiffNotificationRules]
        """  # noqa: E501
        self._notification_rules = notification_rules

    @property
    def tasks(self):
        """Get the tasks of this TemplateSummaryDiff.

        :return: The tasks of this TemplateSummaryDiff.
        :rtype: list[TemplateSummaryDiffTasks]
        """  # noqa: E501
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Set the tasks of this TemplateSummaryDiff.

        :param tasks: The tasks of this TemplateSummaryDiff.
        :type: list[TemplateSummaryDiffTasks]
        """  # noqa: E501
        self._tasks = tasks

    @property
    def telegraf_configs(self):
        """Get the telegraf_configs of this TemplateSummaryDiff.

        :return: The telegraf_configs of this TemplateSummaryDiff.
        :rtype: list[TemplateSummaryDiffTelegrafConfigs]
        """  # noqa: E501
        return self._telegraf_configs

    @telegraf_configs.setter
    def telegraf_configs(self, telegraf_configs):
        """Set the telegraf_configs of this TemplateSummaryDiff.

        :param telegraf_configs: The telegraf_configs of this TemplateSummaryDiff.
        :type: list[TemplateSummaryDiffTelegrafConfigs]
        """  # noqa: E501
        self._telegraf_configs = telegraf_configs

    @property
    def variables(self):
        """Get the variables of this TemplateSummaryDiff.

        :return: The variables of this TemplateSummaryDiff.
        :rtype: list[TemplateSummaryDiffVariables]
        """  # noqa: E501
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Set the variables of this TemplateSummaryDiff.

        :param variables: The variables of this TemplateSummaryDiff.
        :type: list[TemplateSummaryDiffVariables]
        """  # noqa: E501
        self._variables = variables

    def to_dict(self):
        """Return the model properties as a dict."""
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, TemplateSummaryDiff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other