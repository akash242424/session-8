import unittest
from discount import calculate_discount

class TestDiscount(unittest.TestCase):
    def test_negative_total_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_discount(-10)
            
    def test_exactly_fifty_gets_zero_discount(self):
        self.assertEqual(calculate_discount(50), 0.0)

    def test_seventy_gets_ten_percent(self):
        self.assertEqual(calculate_discount(70), 0.10)

    def test_one_twenty_gets_twenty_percent(self):
        self.assertEqual(calculate_discount(120), 0.20)

    def test_vip_gets_five_percent_bonus(self):
        self.assertEqual(calculate_discount(20, is_vip=True), 0.05)

    def test_discount_capped_at_twenty_five(self):
        self.assertEqual(calculate_discount(150, is_vip=True), 0.25)

if __name__ == '__main__':
    unittest.main()