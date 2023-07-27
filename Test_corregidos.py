import unittest
from denningExperienceSF import DiningExperienceManager

class TestDiningExperienceManager(unittest.TestCase):

    def setUp(self):
        self.manager = DiningExperienceManager()

    def test_calculate_cost_with_discounts(self):
        order = {
            "Chinese food": 5,
            "Italian food": 3,
            "Pastries": 2,
        }
        total_cost = self.manager.calculate_cost(order)
        expected_cost = 80  # (5 * 10 + 3 * 12 + 2 * 5) - 10 (total > 50 discount)
        self.assertEqual(total_cost, expected_cost)

    def test_calculate_cost_with_special_meal_surcharge(self):
        order = {
            "Chinese food": 5,
            "Italian food": 3,
            "Pastries": 2,
            "Chef's Specials": 1,
        }
        total_cost = self.manager.calculate_cost(order)
        expected_cost = 86  # (5 * 10 + 3 * 12 + 2 * 5 + 1 * 15) - 10 (total > 50 discount) + 1 * 15 * 0.05
        self.assertEqual(total_cost, expected_cost)

    def test_calculate_cost_with_multiple_discounts(self):
        order = {
            "Chinese food": 5,
            "Italian food": 3,
            "Pastries": 2,
            "Chef's Specials": 5,
        }
        total_cost = self.manager.calculate_cost(order)
        expected_cost = 171  # (5 * 10 + 3 * 12 + 2 * 5 + 5 * 15) - 25 (total > 100 discount) + 5 * 15 * 0.05
        self.assertEqual(total_cost, expected_cost)

    def test_calculate_cost_without_discounts(self):
        order = {
            "Chinese food": 2,
            "Italian food": 3,
        }
        total_cost = self.manager.calculate_cost(order)
        expected_cost = 64  # (2 * 10 + 3 * 12)
        self.assertEqual(total_cost, expected_cost)

    def test_calculate_cost_with_new_meals(self):
        order = {
            "Mexican food": 4,
            "Vegetarian Options": 2,
        }
        total_cost = self.manager.calculate_cost(order)
        expected_cost = 50  # (4 * 11 + 2 * 8)
        self.assertEqual(total_cost, expected_cost)

    def test_calculate_cost_with_new_and_existing_meals(self):
        order = {
            "Chinese food": 3,
            "Italian food": 2,
            "Mexican food": 4,
            "Vegetarian Options": 3,
        }
        total_cost = self.manager.calculate_cost(order)
        expected_cost = 93  # (3 * 10 + 2 * 12 + 4 * 11 + 3 * 8) - 10 (total > 50 discount) + 4 * 11 * 0.05
        self.assertEqual(total_cost, expected_cost)

    def test_confirm_order_confirmation(self):
        with unittest.mock.patch('builtins.input', return_value='y'):
            order = {
                "Chinese food": 5,
                "Italian food": 3,
            }
            total_cost = 65
            self.assertTrue(self.manager.confirm_order(order, total_cost))

    def test_confirm_order_cancellation(self):
        with unittest.mock.patch('builtins.input', return_value='n'):
            order = {
                "Chinese food": 5,
                "Italian food": 3,
            }
            total_cost = 65
            self.assertFalse(self.manager.confirm_order(order, total_cost))

    


if __name__ == '__main__':
      unittest.main()