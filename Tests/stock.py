import unittest
from app.Services.stock import StockServices
from . import BaseTestClass

class StockTestCase(BaseTestClass):

    service = StockServices()
    
    def test_update_stock(self):
        stock = self.service.update_stock(2, self.stock_4)
        for key in self.stock_4.keys():
            self.assertEqual(self.stock_4[key], getattr(stock, key))

    def test_get_by_id(self):
        stock = self.service.find_by_id(3)

        for key in self.stock_3.keys():
            self.assertEqual(self.stock_3[key], getattr(stock, key))

if __name__ == '__main__':
    unittest.main()
    