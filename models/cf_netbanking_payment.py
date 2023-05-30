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


class CFNetbankingPayment(object):
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
        'netbanking': 'CFNetbanking'
    }

    attribute_map = {
        'netbanking': 'netbanking'
    }

    def __init__(self, netbanking=None, local_vars_configuration=None):  # noqa: E501
        """CFNetbankingPayment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._netbanking = None
        self.discriminator = None

        self.netbanking = netbanking

    @property
    def netbanking(self):
        """Gets the netbanking of this CFNetbankingPayment.  # noqa: E501


        :return: The netbanking of this CFNetbankingPayment.  # noqa: E501
        :rtype: CFNetbanking
        """
        return self._netbanking

    @netbanking.setter
    def netbanking(self, netbanking):
        """Sets the netbanking of this CFNetbankingPayment.


        :param netbanking: The netbanking of this CFNetbankingPayment.  # noqa: E501
        :type netbanking: CFNetbanking
        """
        if self.local_vars_configuration.client_side_validation and netbanking is None:  # noqa: E501
            raise ValueError("Invalid value for `netbanking`, must not be `None`")  # noqa: E501

        self._netbanking = netbanking

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
        if not isinstance(other, CFNetbankingPayment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CFNetbankingPayment):
            return True

        return self.to_dict() != other.to_dict()
