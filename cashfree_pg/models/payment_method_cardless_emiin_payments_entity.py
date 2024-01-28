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


from typing import Optional
from pydantic import BaseModel
from cashfree_pg.models.payment_method_app_in_payments_entity_app import PaymentMethodAppInPaymentsEntityApp

class PaymentMethodCardlessEMIInPaymentsEntity(BaseModel):
    """
    payment method carless object in payment entity
    """
    cardless_emi: Optional[PaymentMethodAppInPaymentsEntityApp] = None
    __properties = ["cardless_emi"]

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
    def from_json(cls, json_str: str) -> PaymentMethodCardlessEMIInPaymentsEntity:
        """Create an instance of PaymentMethodCardlessEMIInPaymentsEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PaymentMethodCardlessEMIInPaymentsEntity:
        """Create an instance of PaymentMethodCardlessEMIInPaymentsEntity from a JSON string"""
        if "cardless_emi" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cardless_emi
        if self.cardless_emi:
            _dict['cardless_emi'] = self.cardless_emi.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentMethodCardlessEMIInPaymentsEntity:
        """Create an instance of PaymentMethodCardlessEMIInPaymentsEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentMethodCardlessEMIInPaymentsEntity.parse_obj(obj)

        _obj = PaymentMethodCardlessEMIInPaymentsEntity.parse_obj({
            "cardless_emi": PaymentMethodAppInPaymentsEntityApp.from_dict(obj.get("cardless_emi")) if obj.get("cardless_emi") is not None else None
        })
        return _obj


