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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, constr, validator

class CashbackDetails(BaseModel):
    """
    Cashback detail boject
    """
    cashback_type: constr(strict=True, max_length=50, min_length=1) = Field(..., description="Type of discount")
    cashback_value: Union[StrictFloat, StrictInt] = Field(..., description="Value of Discount.")
    max_cashback_amount: Union[StrictFloat, StrictInt] = Field(..., description="Maximum Value of Cashback allowed.")
    __properties = ["cashback_type", "cashback_value", "max_cashback_amount"]

    @validator('cashback_type')
    def cashback_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('flat', 'percentage'):
            raise ValueError("must be one of enum values ('flat', 'percentage')")
        return value

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
    def from_json(cls, json_str: str) -> CashbackDetails:
        """Create an instance of CashbackDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CashbackDetails:
        """Create an instance of CashbackDetails from a JSON string"""
        temp_dict = json.loads(json_str)
        if "cashback_type, cashback_value, max_cashback_amount" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> CashbackDetails:
        """Create an instance of CashbackDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CashbackDetails.parse_obj(obj)

        _obj = CashbackDetails.parse_obj({
            "cashback_type": obj.get("cashback_type"),
            "cashback_value": obj.get("cashback_value"),
            "max_cashback_amount": obj.get("max_cashback_amount")
        })
        return _obj


