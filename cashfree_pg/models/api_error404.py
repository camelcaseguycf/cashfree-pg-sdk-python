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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class ApiError404(BaseModel):
    """
    Error when resource requested is not found
    """
    message: Optional[StrictStr] = None
    code: Optional[StrictStr] = None
    type: Optional[StrictStr] = Field(None, description="invalid_request_error")
    __properties = ["message", "code", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('invalid_request_error'):
            raise ValueError("must be one of enum values ('invalid_request_error')")
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
    def from_json(cls, json_str: str) -> ApiError404:
        """Create an instance of ApiError404 from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> ApiError404:
        """Create an instance of ApiError404 from a JSON string"""
        temp_dict = json.loads(json_str)
        if "message, code, type" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> ApiError404:
        """Create an instance of ApiError404 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiError404.parse_obj(obj)

        _obj = ApiError404.parse_obj({
            "message": obj.get("message"),
            "code": obj.get("code"),
            "type": obj.get("type")
        })
        return _obj


