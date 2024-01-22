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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from cashfree_pg.models.recon_entity_data_inner import ReconEntityDataInner

class ReconEntity(BaseModel):
    """
    Settlement detailed recon response
    """
    cursor: Optional[StrictStr] = Field(None, description="Specifies from where the next set of settlement details should be fetched.")
    limit: Optional[StrictInt] = Field(None, description="Number of settlements you want to fetch in the next iteration.")
    data: Optional[conlist(ReconEntityDataInner)] = None
    __properties = ["cursor", "limit", "data"]

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
    def from_json(cls, json_str: str) -> ReconEntity:
        """Create an instance of ReconEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReconEntity:
        """Create an instance of ReconEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReconEntity.parse_obj(obj)

        _obj = ReconEntity.parse_obj({
            "cursor": obj.get("cursor"),
            "limit": obj.get("limit"),
            "data": [ReconEntityDataInner.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None
        })
        return _obj


