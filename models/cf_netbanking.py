# coding: utf-8

"""
    New Payment Gateway APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2022-01-01
    Contact: nextgenapi@cashfree.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cashfree_pg_sdk_python.configuration import Configuration


class CFNetbanking(object):
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
        'channel': 'str',
        'netbanking_bank_code': 'int'
    }

    attribute_map = {
        'channel': 'channel',
        'netbanking_bank_code': 'netbanking_bank_code'
    }

    def __init__(self, channel=None, netbanking_bank_code=None, local_vars_configuration=None):  # noqa: E501
        """CFNetbanking - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._channel = None
        self._netbanking_bank_code = None
        self.discriminator = None

        self.channel = channel
        self.netbanking_bank_code = netbanking_bank_code

    @property
    def channel(self):
        """Gets the channel of this CFNetbanking.  # noqa: E501

        The channel for netbanking will always be `link`  # noqa: E501

        :return: The channel of this CFNetbanking.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this CFNetbanking.

        The channel for netbanking will always be `link`  # noqa: E501

        :param channel: The channel of this CFNetbanking.  # noqa: E501
        :type channel: str
        """
        if self.local_vars_configuration.client_side_validation and channel is None:  # noqa: E501
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def netbanking_bank_code(self):
        """Gets the netbanking_bank_code of this CFNetbanking.  # noqa: E501

        Bank code  # noqa: E501

        :return: The netbanking_bank_code of this CFNetbanking.  # noqa: E501
        :rtype: int
        """
        return self._netbanking_bank_code

    @netbanking_bank_code.setter
    def netbanking_bank_code(self, netbanking_bank_code):
        """Sets the netbanking_bank_code of this CFNetbanking.

        Bank code  # noqa: E501

        :param netbanking_bank_code: The netbanking_bank_code of this CFNetbanking.  # noqa: E501
        :type netbanking_bank_code: int
        """
        if self.local_vars_configuration.client_side_validation and netbanking_bank_code is None:  # noqa: E501
            raise ValueError("Invalid value for `netbanking_bank_code`, must not be `None`")  # noqa: E501

        self._netbanking_bank_code = netbanking_bank_code

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CFNetbanking):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CFNetbanking):
            return True

        return self.to_dict() != other.to_dict()
