import unittest

import promotional_code_discount

class TestPromotionalCodeDiscount(unittest.TestCase):
    
    def test_that_promotional_code_discount_exists(self):
        promotional_code_discount.get_discounted_price("dog" , 200 , "")
