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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator
from cashfree_pg.models.authorization_in_payments_entity import AuthorizationInPaymentsEntity
from cashfree_pg.models.error_details_in_payments_entity import ErrorDetailsInPaymentsEntity
from cashfree_pg.models.payment_method_in_payments_entity import PaymentMethodInPaymentsEntity

class PaymentEntity(BaseModel):
    """
    payment entity full object
    """
    cf_payment_id: Optional[StrictInt] = None
    order_id: Optional[StrictStr] = None
    entity: Optional[StrictStr] = None
    error_details: Optional[ErrorDetailsInPaymentsEntity] = None
    is_captured: Optional[StrictBool] = None
    order_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Order amount can be different from payment amount if you collect service fee from the customer")
    payment_group: Optional[StrictStr] = Field(None, description="Type of payment group. One of ['prepaid_card', 'upi_ppi_offline', 'cash', 'upi_credit_card', 'paypal', 'net_banking', 'cardless_emi', 'credit_card', 'bank_transfer', 'pay_later', 'debit_card_emi', 'debit_card', 'wallet', 'upi_ppi', 'upi', 'credit_card_emi']")
    payment_currency: Optional[StrictStr] = None
    payment_amount: Optional[Union[StrictFloat, StrictInt]] = None
    payment_time: Optional[StrictStr] = Field(None, description="This is the time when the payment was initiated")
    payment_completion_time: Optional[StrictStr] = Field(None, description="This is the time when the payment reaches its terminal state")
    payment_status: Optional[StrictStr] = Field(None, description="The transaction status can be one of  [\"SUCCESS\", \"NOT_ATTEMPTED\", \"FAILED\", \"USER_DROPPED\", \"VOID\", \"CANCELLED\", \"PENDING\"]")
    payment_message: Optional[StrictStr] = None
    bank_reference: Optional[StrictStr] = None
    auth_id: Optional[StrictStr] = None
    authorization: Optional[AuthorizationInPaymentsEntity] = None
    payment_method: Optional[PaymentMethodInPaymentsEntity] = None
    __properties = ["cf_payment_id", "order_id", "entity", "error_details", "is_captured", "order_amount", "payment_group", "payment_currency", "payment_amount", "payment_time", "payment_completion_time", "payment_status", "payment_message", "bank_reference", "auth_id", "authorization", "payment_method"]

    @validator('payment_status')
    def payment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUCCESS', 'NOT_ATTEMPTED', 'FAILED', 'USER_DROPPED', 'VOID', 'CANCELLED', 'PENDING'):
            raise ValueError("must be one of enum values ('SUCCESS', 'NOT_ATTEMPTED', 'FAILED', 'USER_DROPPED', 'VOID', 'CANCELLED', 'PENDING')")
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
    def from_json(cls, json_str: str) -> PaymentEntity:
        """Create an instance of PaymentEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error_details
        if self.error_details:
            _dict['error_details'] = self.error_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of authorization
        if self.authorization:
            _dict['authorization'] = self.authorization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['payment_method'] = self.payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentEntity:
        """Create an instance of PaymentEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentEntity.parse_obj(obj)

        _obj = PaymentEntity.parse_obj({
            "cf_payment_id": obj.get("cf_payment_id"),
            "order_id": obj.get("order_id"),
            "entity": obj.get("entity"),
            "error_details": ErrorDetailsInPaymentsEntity.from_dict(obj.get("error_details")) if obj.get("error_details") is not None else None,
            "is_captured": obj.get("is_captured"),
            "order_amount": obj.get("order_amount"),
            "payment_group": obj.get("payment_group"),
            "payment_currency": obj.get("payment_currency"),
            "payment_amount": obj.get("payment_amount"),
            "payment_time": obj.get("payment_time"),
            "payment_completion_time": obj.get("payment_completion_time"),
            "payment_status": obj.get("payment_status"),
            "payment_message": obj.get("payment_message"),
            "bank_reference": obj.get("bank_reference"),
            "auth_id": obj.get("auth_id"),
            "authorization": AuthorizationInPaymentsEntity.from_dict(obj.get("authorization")) if obj.get("authorization") is not None else None,
            "payment_method": PaymentMethodInPaymentsEntity.from_dict(obj.get("payment_method")) if obj.get("payment_method") is not None else None
        })
        return _obj


