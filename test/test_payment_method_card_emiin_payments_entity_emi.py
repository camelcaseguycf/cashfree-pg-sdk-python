# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2022-09-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import cashfree_pg
from cashfree_pg.models.payment_method_card_emiin_payments_entity_emi import PaymentMethodCardEMIInPaymentsEntityEmi  # noqa: E501
from cashfree_pg.rest import ApiException

class TestPaymentMethodCardEMIInPaymentsEntityEmi(unittest.TestCase):
    """PaymentMethodCardEMIInPaymentsEntityEmi unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentMethodCardEMIInPaymentsEntityEmi
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentMethodCardEMIInPaymentsEntityEmi`
        """
        model = cashfree_pg.models.payment_method_card_emiin_payments_entity_emi.PaymentMethodCardEMIInPaymentsEntityEmi()  # noqa: E501
        if include_optional :
            return PaymentMethodCardEMIInPaymentsEntityEmi(
                channel = '', 
                card_number = '', 
                card_network = '', 
                card_type = '', 
                card_country = '', 
                card_bank_name = '', 
                card_network_reference_id = '', 
                emi_tenure = 1.337, 
                emi_details = cashfree_pg.models.payment_method_card_emiin_payments_entity_emi_emi_details.PaymentMethodCardEMIInPaymentsEntity_emi_emi_details(
                    emi_amount = 1.337, 
                    emi_tenure = 1.337, 
                    emi_interest = 1.337, )
            )
        else :
            return PaymentMethodCardEMIInPaymentsEntityEmi(
        )
        """

    def testPaymentMethodCardEMIInPaymentsEntityEmi(self):
        """Test PaymentMethodCardEMIInPaymentsEntityEmi"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
