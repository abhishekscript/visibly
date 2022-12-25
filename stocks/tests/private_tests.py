from django.test import TestCase

from account import factoryboy as account_factory
from stocks import private

class PrivateTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = account_factory.UserFactory()

    def test_search_stock_in_data_frame(self):
        
        with self.subTest('when security_code is passed'):
            stock = '500002'
            resp = private.search_stock_in_data_frame(stock)
            self.assertEqual(
                resp,
                {'score': 100, 'name': 'abb india limited', 'id': None}
            )

        with self.subTest('When security id is passed'):
            stock = 'hdfc'
            resp = private.search_stock_in_data_frame(stock)
            self.assertEqual(
                resp,
                {'score': 100, 'name': 'housing development finance corp.ltd.', 'id': None}
            )

        with self.subTest('When security name is passed'):
            stock = 'hdfc bank'
            resp = private.search_stock_in_data_frame(stock)
            self.assertEqual(
                resp[0]['name'],
                'hdfc bank ltd'
            )
