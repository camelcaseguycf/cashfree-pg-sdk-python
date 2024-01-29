# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2023-08-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class PaymentMethodsFilters(BaseModel):
    """
    Filter for Payment Methods
    """
    payment_methods: Optional[conlist(StrictStr)] = Field(None, description="Array of payment methods to be filtered. This is optional, by default all payment methods will be returned. Possible values in [ 'debit_card', 'credit_card', 'prepaid_card', 'corporate_credit_card', 'upi', 'wallet', 'netbanking', 'banktransfer', 'paylater', 'paypal', 'debit_card_emi', 'credit_card_emi', 'upi_credit_card', 'upi_ppi', 'cardless_emi', 'account_based_payment' ] ")
    __properties = ["payment_methods"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PaymentMethodsFilters:
        """Create an instance of PaymentMethodsFilters from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PaymentMethodsFilters:
        """Create an instance of PaymentMethodsFilters from a JSON string"""
        temp_dict = json.loads(json_str)
        if "payment_methods" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentMethodsFilters:
        """Create an instance of PaymentMethodsFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentMethodsFilters.parse_obj(obj)

        _obj = PaymentMethodsFilters.parse_obj({
            "payment_methods": obj.get("payment_methods")
        })
        return _obj


