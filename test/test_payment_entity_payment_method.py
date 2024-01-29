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
from cashfree_pg.models.payment_entity_payment_method import PaymentEntityPaymentMethod  # noqa: E501
from cashfree_pg.rest import ApiException

class TestPaymentEntityPaymentMethod(unittest.TestCase):
    """PaymentEntityPaymentMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentEntityPaymentMethod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentEntityPaymentMethod`
        """
        model = cashfree_pg.models.payment_entity_payment_method.PaymentEntityPaymentMethod()  # noqa: E501
        if include_optional :
            return PaymentEntityPaymentMethod(
                card = cashfree_pg.models.payment_method_card_in_payments_entity_card.PaymentMethodCardInPaymentsEntity_card(
                    channel = '', 
                    card_number = '', 
                    card_network = '', 
                    card_type = '', 
                    card_country = '', 
                    card_bank_name = '', 
                    card_network_reference_id = '', ), 
                netbanking = cashfree_pg.models.payment_method_net_banking_in_payments_entity_netbanking.PaymentMethodNetBankingInPaymentsEntity_netbanking(
                    channel = '', 
                    netbanking_bank_code = 56, 
                    netbanking_bank_name = '', ), 
                upi = cashfree_pg.models.payment_method_upiin_payments_entity_upi.PaymentMethodUPIInPaymentsEntity_upi(
                    channel = '', 
                    upi_id = '', ), 
                app = cashfree_pg.models.payment_method_app_in_payments_entity_app.PaymentMethodAppInPaymentsEntity_app(
                    channel = '', 
                    provider = '', 
                    phone = '', ), 
                cardless_emi = cashfree_pg.models.payment_method_app_in_payments_entity_app.PaymentMethodAppInPaymentsEntity_app(
                    channel = '', 
                    provider = '', 
                    phone = '', ), 
                paylater = cashfree_pg.models.payment_method_app_in_payments_entity_app.PaymentMethodAppInPaymentsEntity_app(
                    channel = '', 
                    provider = '', 
                    phone = '', ), 
                emi = cashfree_pg.models.payment_method_card_emiin_payments_entity_emi.PaymentMethodCardEMIInPaymentsEntity_emi(
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
                        emi_interest = 1.337, ), )
            )
        else :
            return PaymentEntityPaymentMethod(
        )
        """

    def testPaymentEntityPaymentMethod(self):
        """Test PaymentEntityPaymentMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
