import unittest
from unittest.mock import patch
from denningExperienceSF import DiningExperienceManager

class TestDiningExperienceManager(unittest.TestCase):
    def setUp(self):
        self.manager = DiningExperienceManager()

    def test_calculate_cost_with_discounts(self):
        order = {
            "Chinese Food": 5,
            "Italian Food": 3,
            "Pastries": 2,
        }
        total_cost = self.manager.calculate_cost(order)
        expected_cost = 80  # (5 * 10 + 3 * 12 + 2 * 5) - 10 (total > 50 discount)
        self.assertEqual(total_cost, expected_cost)

    def test_calculate_cost_with_special_meal_surcharge(self):
        order = {
            "Chinese Food": 5,
            "Italian Food": 3,
            "Pastries": 2,
            "Chef's Specials": 1,
        }
        total_cost = self.manager.calculate_cost(order)
        expected_cost = 86  # (5 * 10 + 3 * 12 + 2 * 5 + 1 * 15) - 10 (total > 50 discount) + 1 * 15 * 0.05

    def test_calculate_cost_with_multiple_discounts(self):
        order = {
            "Chinese Food": 5,
            "Italian Food": 3,
            "Pastries": 2,
            "Chef's Specials": 5,
        }
        
        total_cost = self.manager.calculate_cost(order)
        print(total_cost)
        expected_cost = 171  # (5 * 10 + 3 * 12 + 2 * 5 + 5 * 15) - 25 (total > 100 discount) + 5 * 15 * 0.05

    def test_confirm_order_confirmation(self):
        with patch('builtins.input', return_value='y'):
            order = {
                "Chinese Food": 5,
                "Italian Food": 3,
            }
            total_cost = 65
            self.assertTrue(self.manager.confirm_order(order, total_cost))

    def test_confirm_order_cancellation(self):
        with patch('builtins.input', return_value='n'):
            order = {
                "Chinese Food": 5,
                "Italian Food": 3,
            }
            total_cost = 65
            self.assertFalse(self.manager.confirm_order(order, total_cost))

    def test_get_valid_quantity_valid_input(self):
        with patch('builtins.input', return_value='10'):
            quantity = self.manager.get_valid_quantity("Enter quantity: ")
            self.assertEqual(quantity, 10)

    def test_get_valid_quantity_invalid_input_then_valid_input(self):
        with patch('builtins.input', side_effect=['0', '-5', '15']):
            quantity = self.manager.get_valid_quantity("Enter quantity: ")
            self.assertEqual(quantity, 15)

    def test_get_valid_quantity_exceed_max_quantity_then_valid_input(self):
        with patch('builtins.input', side_effect=['105', '95']):
            quantity = self.manager.get_valid_quantity("Enter quantity: ")
            self.assertEqual(quantity, 95)

    def test_get_valid_quantity_maximum_quantity(self):
        with patch('builtins.input', return_value='100'):
            quantity = self.manager.get_valid_quantity("Enter quantity: ")
            self.assertEqual(quantity, 100)

if __name__ == "__main__":
    unittest.main()