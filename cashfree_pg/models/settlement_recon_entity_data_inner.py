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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class SettlementReconEntityDataInner(BaseModel):
    """
    SettlementReconEntityDataInner
    """
    event_id: Optional[StrictStr] = Field(None, description="Unique ID associated with the event.")
    event_type: Optional[StrictStr] = Field(None, description="The event type can be PAYMENT, REFUND, REFUND_REVERSAL, DISPUTE, DISPUTE_REVERSAL, CHARGEBACK, CHARGEBACK_REVERSAL, OTHER_ADJUSTMENT.")
    event_settlement_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Amount that is part of the settlement corresponding to the event.")
    event_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Amount corresponding to the event. Example, refund amount, dispute amount, payment amount, etc.")
    sale_type: Optional[StrictStr] = Field(None, description="Indicates if it is CREDIT/DEBIT sale.")
    event_status: Optional[StrictStr] = Field(None, description="Status of the event. Example - SUCCESS, FAILED, PENDING, CANCELLED.")
    entity: Optional[StrictStr] = Field(None, description="Recon")
    event_time: Optional[StrictStr] = Field(None, description="Time associated with the event. Example, transaction time, dispute initiation time")
    event_currency: Optional[StrictStr] = Field(None, description="Curreny type - INR.")
    order_id: Optional[StrictStr] = Field(None, description="Unique order ID. Alphanumeric and only '-' and '_' allowed.")
    order_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The amount which was passed at the order creation time.")
    customer_phone: Optional[StrictStr] = Field(None, description="Customer phone number.")
    customer_email: Optional[StrictStr] = Field(None, description="Customer email.")
    customer_name: Optional[StrictStr] = Field(None, description="Customer name.")
    payment_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Payment amount captured.")
    payment_utr: Optional[StrictStr] = Field(None, description="Unique transaction reference number of the payment.")
    payment_time: Optional[StrictStr] = Field(None, description="Date and time when the payment was initiated.")
    payment_service_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Service charge applicable for the payment.")
    payment_service_tax: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Service tax applicable on the payment.")
    cf_payment_id: Optional[StrictInt] = Field(None, description="Cashfree Payments unique ID to identify a payment.")
    cf_settlement_id: Optional[StrictInt] = Field(None, description="Unique ID to identify the settlement.")
    settlement_date: Optional[StrictStr] = Field(None, description="Date and time when the settlement was processed.")
    settlement_utr: Optional[StrictStr] = Field(None, description="Unique transaction reference number of the settlement.")
    split_service_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Service charge that is applicable for splitting the payment.")
    split_service_tax: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Service tax applicable for splitting the amount to vendors.")
    vendor_commission: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Vendor commission applicable for this transaction.")
    closed_in_favor_of: Optional[StrictStr] = Field(None, description="Specifies whether the dispute was closed in favor of the merchant or customer. Possible values - Merchant, Customer.")
    dispute_resolved_on: Optional[StrictStr] = Field(None, description="Date and time when the dispute was resolved.")
    dispute_category: Optional[StrictStr] = Field(None, description="Category of the dispute - Dispute code and the reason for dispute is shown.")
    dispute_note: Optional[StrictStr] = Field(None, description="Note regarding the dispute.")
    refund_processed_at: Optional[StrictStr] = Field(None, description="Date and time when the refund was processed.")
    refund_arn: Optional[StrictStr] = Field(None, description="The bank reference number for refund.")
    refund_note: Optional[StrictStr] = Field(None, description="A refund note for your reference.")
    refund_id: Optional[StrictStr] = Field(None, description="An unique ID associated with the refund.")
    adjustment_remarks: Optional[StrictStr] = Field(None, description="Other adjustment remarks.")
    __properties = ["event_id", "event_type", "event_settlement_amount", "event_amount", "sale_type", "event_status", "entity", "event_time", "event_currency", "order_id", "order_amount", "customer_phone", "customer_email", "customer_name", "payment_amount", "payment_utr", "payment_time", "payment_service_charge", "payment_service_tax", "cf_payment_id", "cf_settlement_id", "settlement_date", "settlement_utr", "split_service_charge", "split_service_tax", "vendor_commission", "closed_in_favor_of", "dispute_resolved_on", "dispute_category", "dispute_note", "refund_processed_at", "refund_arn", "refund_note", "refund_id", "adjustment_remarks"]

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
    def from_json(cls, json_str: str) -> SettlementReconEntityDataInner:
        """Create an instance of SettlementReconEntityDataInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> SettlementReconEntityDataInner:
        """Create an instance of SettlementReconEntityDataInner from a JSON string"""
        if "event_id, event_type, event_settlement_amount, event_amount, sale_type, event_status, entity, event_time, event_currency, order_id, order_amount, customer_phone, customer_email, customer_name, payment_amount, payment_utr, payment_time, payment_service_charge, payment_service_tax, cf_payment_id, cf_settlement_id, settlement_date, settlement_utr, split_service_charge, split_service_tax, vendor_commission, closed_in_favor_of, dispute_resolved_on, dispute_category, dispute_note, refund_processed_at, refund_arn, refund_note, refund_id, adjustment_remarks" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SettlementReconEntityDataInner:
        """Create an instance of SettlementReconEntityDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SettlementReconEntityDataInner.parse_obj(obj)

        _obj = SettlementReconEntityDataInner.parse_obj({
            "event_id": obj.get("event_id"),
            "event_type": obj.get("event_type"),
            "event_settlement_amount": obj.get("event_settlement_amount"),
            "event_amount": obj.get("event_amount"),
            "sale_type": obj.get("sale_type"),
            "event_status": obj.get("event_status"),
            "entity": obj.get("entity"),
            "event_time": obj.get("event_time"),
            "event_currency": obj.get("event_currency"),
            "order_id": obj.get("order_id"),
            "order_amount": obj.get("order_amount"),
            "customer_phone": obj.get("customer_phone"),
            "customer_email": obj.get("customer_email"),
            "customer_name": obj.get("customer_name"),
            "payment_amount": obj.get("payment_amount"),
            "payment_utr": obj.get("payment_utr"),
            "payment_time": obj.get("payment_time"),
            "payment_service_charge": obj.get("payment_service_charge"),
            "payment_service_tax": obj.get("payment_service_tax"),
            "cf_payment_id": obj.get("cf_payment_id"),
            "cf_settlement_id": obj.get("cf_settlement_id"),
            "settlement_date": obj.get("settlement_date"),
            "settlement_utr": obj.get("settlement_utr"),
            "split_service_charge": obj.get("split_service_charge"),
            "split_service_tax": obj.get("split_service_tax"),
            "vendor_commission": obj.get("vendor_commission"),
            "closed_in_favor_of": obj.get("closed_in_favor_of"),
            "dispute_resolved_on": obj.get("dispute_resolved_on"),
            "dispute_category": obj.get("dispute_category"),
            "dispute_note": obj.get("dispute_note"),
            "refund_processed_at": obj.get("refund_processed_at"),
            "refund_arn": obj.get("refund_arn"),
            "refund_note": obj.get("refund_note"),
            "refund_id": obj.get("refund_id"),
            "adjustment_remarks": obj.get("adjustment_remarks")
        })
        return _obj


