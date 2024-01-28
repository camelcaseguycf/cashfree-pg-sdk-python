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


from typing import Dict, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, constr
from cashfree_pg.models.link_customer_details_entity import LinkCustomerDetailsEntity
from cashfree_pg.models.link_meta_entity import LinkMetaEntity
from cashfree_pg.models.link_notify_entity import LinkNotifyEntity

class CreateLinkRequest(BaseModel):
    """
    Request paramenters for link creation
    """
    link_id: constr(strict=True, max_length=50) = Field(..., description="Unique Identifier (provided by merchant) for the Link. Alphanumeric and only - and _ allowed (50 character limit). Use this for other link-related APIs.")
    link_amount: Union[StrictFloat, StrictInt] = Field(..., description="Amount to be collected using this link. Provide upto two decimals for paise.")
    link_currency: constr(strict=True) = Field(..., description="Currency for the payment link. Default is INR. Contact care@cashfree.com to enable new currencies.")
    link_purpose: constr(strict=True, max_length=500) = Field(..., description="A brief description for which payment must be collected. This is shown to the customer.")
    customer_details: LinkCustomerDetailsEntity = Field(...)
    link_partial_payments: Optional[StrictBool] = Field(None, description="If \"true\", customer can make partial payments for the link.")
    link_minimum_partial_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Minimum amount in first installment that needs to be paid by the customer if partial payments are enabled. This should be less than the link_amount.")
    link_expiry_time: Optional[StrictStr] = Field(None, description="Time after which the link expires. Customers will not be able to make the payment beyond the time specified here. You can provide them in a valid ISO 8601 time format. Default is 30 days.")
    link_notify: Optional[LinkNotifyEntity] = None
    link_auto_reminders: Optional[StrictBool] = Field(None, description="If \"true\", reminders will be sent to customers for collecting payments.")
    link_notes: Optional[Dict[str, StrictStr]] = Field(None, description="Key-value pair that can be used to store additional information about the entity. Maximum 5 key-value pairs")
    link_meta: Optional[LinkMetaEntity] = None
    __properties = ["link_id", "link_amount", "link_currency", "link_purpose", "customer_details", "link_partial_payments", "link_minimum_partial_amount", "link_expiry_time", "link_notify", "link_auto_reminders", "link_notes", "link_meta"]

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
    def from_json(cls, json_str: str) -> CreateLinkRequest:
        """Create an instance of CreateLinkRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CreateLinkRequest:
        """Create an instance of CreateLinkRequest from a JSON string"""
        if "link_id", "link_amount", "link_currency", "link_purpose", "customer_details", "link_partial_payments", "link_minimum_partial_amount", "link_expiry_time", "link_notify", "link_auto_reminders", "link_notes", "link_meta" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of customer_details
        if self.customer_details:
            _dict['customer_details'] = self.customer_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of link_notify
        if self.link_notify:
            _dict['link_notify'] = self.link_notify.to_dict()
        # override the default output from pydantic by calling `to_dict()` of link_meta
        if self.link_meta:
            _dict['link_meta'] = self.link_meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateLinkRequest:
        """Create an instance of CreateLinkRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateLinkRequest.parse_obj(obj)

        _obj = CreateLinkRequest.parse_obj({
            "link_id": obj.get("link_id"),
            "link_amount": obj.get("link_amount"),
            "link_currency": obj.get("link_currency"),
            "link_purpose": obj.get("link_purpose"),
            "customer_details": LinkCustomerDetailsEntity.from_dict(obj.get("customer_details")) if obj.get("customer_details") is not None else None,
            "link_partial_payments": obj.get("link_partial_payments"),
            "link_minimum_partial_amount": obj.get("link_minimum_partial_amount"),
            "link_expiry_time": obj.get("link_expiry_time"),
            "link_notify": LinkNotifyEntity.from_dict(obj.get("link_notify")) if obj.get("link_notify") is not None else None,
            "link_auto_reminders": obj.get("link_auto_reminders"),
            "link_notes": obj.get("link_notes"),
            "link_meta": LinkMetaEntity.from_dict(obj.get("link_meta")) if obj.get("link_meta") is not None else None
        })
        return _obj


