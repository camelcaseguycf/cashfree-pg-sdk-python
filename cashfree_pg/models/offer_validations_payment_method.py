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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from cashfree_pg.models.offer_all import OfferAll
from cashfree_pg.models.offer_card import OfferCard
from cashfree_pg.models.offer_emi import OfferEMI
from cashfree_pg.models.offer_nb import OfferNB
from cashfree_pg.models.offer_paylater import OfferPaylater
from cashfree_pg.models.offer_upi import OfferUPI
from cashfree_pg.models.offer_wallet import OfferWallet
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

OFFERVALIDATIONSPAYMENTMETHOD_ONE_OF_SCHEMAS = ["OfferAll", "OfferCard", "OfferEMI", "OfferNB", "OfferPaylater", "OfferUPI", "OfferWallet"]

class OfferValidationsPaymentMethod(BaseModel):
    """
    OfferValidationsPaymentMethod
    """
    # data type: OfferAll
    oneof_schema_1_validator: Optional[OfferAll] = None
    # data type: OfferCard
    oneof_schema_2_validator: Optional[OfferCard] = None
    # data type: OfferNB
    oneof_schema_3_validator: Optional[OfferNB] = None
    # data type: OfferWallet
    oneof_schema_4_validator: Optional[OfferWallet] = None
    # data type: OfferUPI
    oneof_schema_5_validator: Optional[OfferUPI] = None
    # data type: OfferPaylater
    oneof_schema_6_validator: Optional[OfferPaylater] = None
    # data type: OfferEMI
    oneof_schema_7_validator: Optional[OfferEMI] = None
    if TYPE_CHECKING:
        actual_instance: Union[OfferAll, OfferCard, OfferEMI, OfferNB, OfferPaylater, OfferUPI, OfferWallet]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(OFFERVALIDATIONSPAYMENTMETHOD_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = OfferValidationsPaymentMethod.construct()
        error_messages = []
        match = 0
        # validate data type: OfferAll
        if not isinstance(v, OfferAll):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OfferAll`")
        else:
            match += 1
        # validate data type: OfferCard
        if not isinstance(v, OfferCard):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OfferCard`")
        else:
            match += 1
        # validate data type: OfferNB
        if not isinstance(v, OfferNB):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OfferNB`")
        else:
            match += 1
        # validate data type: OfferWallet
        if not isinstance(v, OfferWallet):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OfferWallet`")
        else:
            match += 1
        # validate data type: OfferUPI
        if not isinstance(v, OfferUPI):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OfferUPI`")
        else:
            match += 1
        # validate data type: OfferPaylater
        if not isinstance(v, OfferPaylater):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OfferPaylater`")
        else:
            match += 1
        # validate data type: OfferEMI
        if not isinstance(v, OfferEMI):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OfferEMI`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in OfferValidationsPaymentMethod with oneOf schemas: OfferAll, OfferCard, OfferEMI, OfferNB, OfferPaylater, OfferUPI, OfferWallet. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in OfferValidationsPaymentMethod with oneOf schemas: OfferAll, OfferCard, OfferEMI, OfferNB, OfferPaylater, OfferUPI, OfferWallet. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> OfferValidationsPaymentMethod:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> OfferValidationsPaymentMethod:
        """Returns the object represented by the json string"""
        instance = OfferValidationsPaymentMethod.construct()
        error_messages = []
        match = 0

        # deserialize data into OfferAll
        try:
            instance.actual_instance = OfferAll.from_json(json_str)
            match += 1
            if (instance.actual_instance == None):
                # do nothing
            else:
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OfferCard
        try:
            instance.actual_instance = OfferCard.from_json(json_str)
            match += 1
            if (instance.actual_instance == None):
                # do nothing
            else:
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OfferNB
        try:
            instance.actual_instance = OfferNB.from_json(json_str)
            match += 1
            if (instance.actual_instance == None):
                # do nothing
            else:
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OfferWallet
        try:
            instance.actual_instance = OfferWallet.from_json(json_str)
            match += 1
            if (instance.actual_instance == None):
                # do nothing
            else:
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OfferUPI
        try:
            instance.actual_instance = OfferUPI.from_json(json_str)
            match += 1
            if (instance.actual_instance == None):
                # do nothing
            else:
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OfferPaylater
        try:
            instance.actual_instance = OfferPaylater.from_json(json_str)
            match += 1
            if (instance.actual_instance == None):
                # do nothing
            else:
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OfferEMI
        try:
            instance.actual_instance = OfferEMI.from_json(json_str)
            match += 1
            if (instance.actual_instance == None):
                # do nothing
            else:
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into OfferValidationsPaymentMethod with oneOf schemas: OfferAll, OfferCard, OfferEMI, OfferNB, OfferPaylater, OfferUPI, OfferWallet. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into OfferValidationsPaymentMethod with oneOf schemas: OfferAll, OfferCard, OfferEMI, OfferNB, OfferPaylater, OfferUPI, OfferWallet. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


