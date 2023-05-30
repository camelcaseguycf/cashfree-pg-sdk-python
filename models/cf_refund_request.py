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


class CFRefundRequest(object):
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
        'refund_amount': 'float',
        'refund_id': 'str',
        'refund_note': 'str',
        'refund_speed': 'str',
        'refund_splits': 'list[CFVendorSplit]'
    }

    attribute_map = {
        'refund_amount': 'refund_amount',
        'refund_id': 'refund_id',
        'refund_note': 'refund_note',
        'refund_speed': 'refund_speed',
        'refund_splits': 'refund_splits'
    }

    def __init__(self, refund_amount=None, refund_id=None, refund_note=None, refund_speed=None, refund_splits=None, local_vars_configuration=None):  # noqa: E501
        """CFRefundRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._refund_amount = None
        self._refund_id = None
        self._refund_note = None
        self._refund_speed = None
        self._refund_splits = None
        self.discriminator = None

        self.refund_amount = refund_amount
        self.refund_id = refund_id
        if refund_note is not None:
            self.refund_note = refund_note
        if refund_speed is not None:
            self.refund_speed = refund_speed
        if refund_splits is not None:
            self.refund_splits = refund_splits

    @property
    def refund_amount(self):
        """Gets the refund_amount of this CFRefundRequest.  # noqa: E501

        Amount to be refunded. Should be lesser than or equal to the transaction amount. (Decimals allowed)  # noqa: E501

        :return: The refund_amount of this CFRefundRequest.  # noqa: E501
        :rtype: float
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """Sets the refund_amount of this CFRefundRequest.

        Amount to be refunded. Should be lesser than or equal to the transaction amount. (Decimals allowed)  # noqa: E501

        :param refund_amount: The refund_amount of this CFRefundRequest.  # noqa: E501
        :type refund_amount: float
        """
        if self.local_vars_configuration.client_side_validation and refund_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `refund_amount`, must not be `None`")  # noqa: E501

        self._refund_amount = refund_amount

    @property
    def refund_id(self):
        """Gets the refund_id of this CFRefundRequest.  # noqa: E501

        An unique ID to associate the refund with. Provie alphanumeric values  # noqa: E501

        :return: The refund_id of this CFRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        """Sets the refund_id of this CFRefundRequest.

        An unique ID to associate the refund with. Provie alphanumeric values  # noqa: E501

        :param refund_id: The refund_id of this CFRefundRequest.  # noqa: E501
        :type refund_id: str
        """
        if self.local_vars_configuration.client_side_validation and refund_id is None:  # noqa: E501
            raise ValueError("Invalid value for `refund_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                refund_id is not None and len(refund_id) > 40):
            raise ValueError("Invalid value for `refund_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                refund_id is not None and len(refund_id) < 3):
            raise ValueError("Invalid value for `refund_id`, length must be greater than or equal to `3`")  # noqa: E501

        self._refund_id = refund_id

    @property
    def refund_note(self):
        """Gets the refund_note of this CFRefundRequest.  # noqa: E501

        A refund note for your reference.  # noqa: E501

        :return: The refund_note of this CFRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._refund_note

    @refund_note.setter
    def refund_note(self, refund_note):
        """Sets the refund_note of this CFRefundRequest.

        A refund note for your reference.  # noqa: E501

        :param refund_note: The refund_note of this CFRefundRequest.  # noqa: E501
        :type refund_note: str
        """
        if (self.local_vars_configuration.client_side_validation and
                refund_note is not None and len(refund_note) > 100):
            raise ValueError("Invalid value for `refund_note`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                refund_note is not None and len(refund_note) < 3):
            raise ValueError("Invalid value for `refund_note`, length must be greater than or equal to `3`")  # noqa: E501

        self._refund_note = refund_note

    @property
    def refund_speed(self):
        """Gets the refund_speed of this CFRefundRequest.  # noqa: E501

        Speed at which the refund is processed. It's an optional field with default being STANDARD  # noqa: E501

        :return: The refund_speed of this CFRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._refund_speed

    @refund_speed.setter
    def refund_speed(self, refund_speed):
        """Sets the refund_speed of this CFRefundRequest.

        Speed at which the refund is processed. It's an optional field with default being STANDARD  # noqa: E501

        :param refund_speed: The refund_speed of this CFRefundRequest.  # noqa: E501
        :type refund_speed: str
        """
        allowed_values = ["STANDARD", "INSTANT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and refund_speed not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `refund_speed` ({0}), must be one of {1}"  # noqa: E501
                .format(refund_speed, allowed_values)
            )

        self._refund_speed = refund_speed

    @property
    def refund_splits(self):
        """Gets the refund_splits of this CFRefundRequest.  # noqa: E501


        :return: The refund_splits of this CFRefundRequest.  # noqa: E501
        :rtype: list[CFVendorSplit]
        """
        return self._refund_splits

    @refund_splits.setter
    def refund_splits(self, refund_splits):
        """Sets the refund_splits of this CFRefundRequest.


        :param refund_splits: The refund_splits of this CFRefundRequest.  # noqa: E501
        :type refund_splits: list[CFVendorSplit]
        """

        self._refund_splits = refund_splits

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
        if not isinstance(other, CFRefundRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CFRefundRequest):
            return True

        return self.to_dict() != other.to_dict()
