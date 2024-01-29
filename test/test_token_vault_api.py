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

import cashfree_pg
from cashfree_pg.api.token_vault_api import TokenVaultApi  # noqa: E501
from cashfree_pg.rest import ApiException


class TestTokenVaultApi(unittest.TestCase):
    """TokenVaultApi unit test stubs"""

    def setUp(self):
        self.api = cashfree_pg.api.token_vault_api.TokenVaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_p_g_customer_delete_instrument(self):
        """Test case for p_g_customer_delete_instrument

        Delete Saved Card Instrument  # noqa: E501
        """
        pass

    def test_p_g_customer_fetch_instrument(self):
        """Test case for p_g_customer_fetch_instrument

        Fetch Specific Saved Card Instrument  # noqa: E501
        """
        pass

    def test_p_g_customer_fetch_instruments(self):
        """Test case for p_g_customer_fetch_instruments

        Fetch All Saved Card Instrument  # noqa: E501
        """
        pass

    def test_p_g_customer_instruments_fetch_cryptogram(self):
        """Test case for p_g_customer_instruments_fetch_cryptogram

        Fetch cryptogram for a saved card instrument  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
