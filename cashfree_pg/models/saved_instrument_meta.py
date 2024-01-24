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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class SavedInstrumentMeta(BaseModel):
    """
    Card instrument meta information
    """
    card_network: Optional[StrictStr] = Field(None, description="card scheme/network of the saved card. Example visa, mastercard")
    card_bank_name: Optional[StrictStr] = Field(None, description="Issuing bank name of saved card")
    card_country: Optional[StrictStr] = Field(None, description="Issuing country of saved card")
    card_type: Optional[StrictStr] = Field(None, description="Type of saved card")
    card_token_details: Optional[Dict[str, Any]] = None
    __properties = ["card_network", "card_bank_name", "card_country", "card_type", "card_token_details"]

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
    def from_json(cls, json_str: str) -> SavedInstrumentMeta:
        """Create an instance of SavedInstrumentMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SavedInstrumentMeta:
        """Create an instance of SavedInstrumentMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SavedInstrumentMeta.parse_obj(obj)

        _obj = SavedInstrumentMeta.parse_obj({
            "card_network": obj.get("card_network"),
            "card_bank_name": obj.get("card_bank_name"),
            "card_country": obj.get("card_country"),
            "card_type": obj.get("card_type"),
            "card_token_details": obj.get("card_token_details")
        })
        return _obj


