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



from pydantic import BaseModel, Field, constr, validator

class OfferTnc(BaseModel):
    """
    Offer terms and condition object
    """
    offer_tnc_type: constr(strict=True, max_length=50, min_length=3) = Field(..., description="TnC Type for the Offer. It can be either `text` or `link`")
    offer_tnc_value: constr(strict=True, max_length=100, min_length=3) = Field(..., description="TnC for the Offer.")
    __properties = ["offer_tnc_type", "offer_tnc_value"]

    @validator('offer_tnc_type')
    def offer_tnc_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('text', 'link'):
            raise ValueError("must be one of enum values ('text', 'link')")
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
    def from_json(cls, json_str: str) -> OfferTnc:
        """Create an instance of OfferTnc from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> OfferTnc:
        """Create an instance of OfferTnc from a JSON string"""
        temp_dict = json.loads(json_str)
        if "offer_tnc_type, offer_tnc_value" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> OfferTnc:
        """Create an instance of OfferTnc from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OfferTnc.parse_obj(obj)

        _obj = OfferTnc.parse_obj({
            "offer_tnc_type": obj.get("offer_tnc_type"),
            "offer_tnc_value": obj.get("offer_tnc_value")
        })
        return _obj


