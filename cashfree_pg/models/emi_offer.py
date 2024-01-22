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


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist, constr

class EMIOffer(BaseModel):
    """
    EMIOffer
    """
    type: constr(strict=True, max_length=100, min_length=3) = Field(..., description="Type of emi offer. Possible values are `credit_card_emi`, `debit_card_emi`, `cardless_emi`")
    issuer: constr(strict=True, max_length=100, min_length=3) = Field(..., description="Bank Name")
    tenures: conlist(StrictInt) = Field(...)
    __properties = ["type", "issuer", "tenures"]

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
    def from_json(cls, json_str: str) -> EMIOffer:
        """Create an instance of EMIOffer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EMIOffer:
        """Create an instance of EMIOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EMIOffer.parse_obj(obj)

        _obj = EMIOffer.parse_obj({
            "type": obj.get("type"),
            "issuer": obj.get("issuer"),
            "tenures": obj.get("tenures")
        })
        return _obj


