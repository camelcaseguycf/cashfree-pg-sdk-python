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
from cashfree_pg.models.eligibility_payment_methods_entity import EligibilityPaymentMethodsEntity  # noqa: E501
from cashfree_pg.rest import ApiException

class TestEligibilityPaymentMethodsEntity(unittest.TestCase):
    """EligibilityPaymentMethodsEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EligibilityPaymentMethodsEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EligibilityPaymentMethodsEntity`
        """
        model = cashfree_pg.models.eligibility_payment_methods_entity.EligibilityPaymentMethodsEntity()  # noqa: E501
        if include_optional :
            return EligibilityPaymentMethodsEntity(
                eligibility = True, 
                entity_type = 'payment_methods', 
                entity_value = 'netbanking', 
                entity_details = {"payment_method_details":[{"nick":"motak_kahindra_bank","display":"Motak Kahindra Bank","eligibility":true,"code":3032},{"nick":"bank_of_india","display":"Bank Of India","eligibility":true,"code":3031}]}
            )
        else :
            return EligibilityPaymentMethodsEntity(
        )
        """

    def testEligibilityPaymentMethodsEntity(self):
        """Test EligibilityPaymentMethodsEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
