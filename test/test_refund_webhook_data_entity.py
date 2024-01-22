# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2023-08-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import cashfree_pg
from cashfree_pg.models.refund_webhook_data_entity import RefundWebhookDataEntity  # noqa: E501
from cashfree_pg.rest import ApiException

class TestRefundWebhookDataEntity(unittest.TestCase):
    """RefundWebhookDataEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RefundWebhookDataEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RefundWebhookDataEntity`
        """
        model = cashfree_pg.models.refund_webhook_data_entity.RefundWebhookDataEntity()  # noqa: E501
        if include_optional :
            return RefundWebhookDataEntity(
                refund = {"cf_payment_id":"918812","cf_refund_id":"1553338","refund_id":"REF-123","order_id":"c6G-QMcbm1848","entity":"refund","refund_amount":100.81,"refund_currency":"INR","refund_note":"Refund for order #123","refund_status":"SUCCESS","refund_type":"MERCHANT_INITIATED","refund_splits":[],"status_description":"In Progress","refund_arn":"RF12312","metadata":{"option":"myotpion"},"created_at":"2021-07-25T08:57:52+05:30","processed_at":"2021-07-25T12:57:52+05:30","refund_charge":0,"refund_mode":"STANDARD"}
            )
        else :
            return RefundWebhookDataEntity(
        )
        """

    def testRefundWebhookDataEntity(self):
        """Test RefundWebhookDataEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
