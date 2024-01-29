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
from cashfree_pg.models.payment_method_card_in_payments_entity_card import PaymentMethodCardInPaymentsEntityCard  # noqa: E501
from cashfree_pg.rest import ApiException

class TestPaymentMethodCardInPaymentsEntityCard(unittest.TestCase):
    """PaymentMethodCardInPaymentsEntityCard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentMethodCardInPaymentsEntityCard
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentMethodCardInPaymentsEntityCard`
        """
        model = cashfree_pg.models.payment_method_card_in_payments_entity_card.PaymentMethodCardInPaymentsEntityCard()  # noqa: E501
        if include_optional :
            return PaymentMethodCardInPaymentsEntityCard(
                channel = '', 
                card_number = '', 
                card_network = '', 
                card_type = '', 
                card_country = '', 
                card_bank_name = '', 
                card_network_reference_id = ''
            )
        else :
            return PaymentMethodCardInPaymentsEntityCard(
        )
        """

    def testPaymentMethodCardInPaymentsEntityCard(self):
        """Test PaymentMethodCardInPaymentsEntityCard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
