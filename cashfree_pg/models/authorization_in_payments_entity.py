# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2022-09-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

class AuthorizationInPaymentsEntity(BaseModel):
    """
    If preauth enabled for account you will get this body
    """
    action: Optional[StrictStr] = Field(None, description="One of CAPTURE or VOID")
    status: Optional[StrictStr] = Field(None, description="One of SUCCESS or PENDING")
    captured_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The captured amount for this authorization request")
    start_time: Optional[StrictStr] = Field(None, description="Start time of this authorization hold (only for UPI)")
    end_time: Optional[StrictStr] = Field(None, description="End time of this authorization hold (only for UPI)")
    approve_by: Optional[StrictStr] = Field(None, description="Approve by time as passed in the authorization request (only for UPI)")
    action_reference: Optional[StrictStr] = Field(None, description="CAPTURE or VOID reference number based on action ")
    action_time: Optional[StrictStr] = Field(None, description="Time of action (CAPTURE or VOID)")
    __properties = ["action", "status", "captured_amount", "start_time", "end_time", "approve_by", "action_reference", "action_time"]

    @validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CAPTURE', 'VOID'):
            raise ValueError("must be one of enum values ('CAPTURE', 'VOID')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUCCESS', 'PENDING'):
            raise ValueError("must be one of enum values ('SUCCESS', 'PENDING')")
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
    def from_json(cls, json_str: str) -> AuthorizationInPaymentsEntity:
        """Create an instance of AuthorizationInPaymentsEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> AuthorizationInPaymentsEntity:
        """Create an instance of AuthorizationInPaymentsEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "action, status, captured_amount, start_time, end_time, approve_by, action_reference, action_time" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> AuthorizationInPaymentsEntity:
        """Create an instance of AuthorizationInPaymentsEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthorizationInPaymentsEntity.parse_obj(obj)

        _obj = AuthorizationInPaymentsEntity.parse_obj({
            "action": obj.get("action"),
            "status": obj.get("status"),
            "captured_amount": obj.get("captured_amount"),
            "start_time": obj.get("start_time"),
            "end_time": obj.get("end_time"),
            "approve_by": obj.get("approve_by"),
            "action_reference": obj.get("action_reference"),
            "action_time": obj.get("action_time")
        })
        return _obj


