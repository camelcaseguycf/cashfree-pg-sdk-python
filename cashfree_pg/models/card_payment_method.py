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



from pydantic import BaseModel, Field
from cashfree_pg.models.card import Card

class CardPaymentMethod(BaseModel):
    """
    The card payment object is used to make payment using either plain card number, saved card instrument id or using cryptogram 
    """
    card: Card = Field(...)
    __properties = ["card"]

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
    def from_json(cls, json_str: str) -> CardPaymentMethod:
        """Create an instance of CardPaymentMethod from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CardPaymentMethod:
        """Create an instance of CardPaymentMethod from a JSON string"""
        temp_dict = json.loads(json_str)
        if "card" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of card
        if self.card:
            _dict['card'] = self.card.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CardPaymentMethod:
        """Create an instance of CardPaymentMethod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CardPaymentMethod.parse_obj(obj)

        _obj = CardPaymentMethod.parse_obj({
            "card": Card.from_dict(obj.get("card")) if obj.get("card") is not None else None
        })
        return _obj


