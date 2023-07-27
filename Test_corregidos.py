import unittest 
from unittest import mock
from denningExperienceSF import DiningExperienceManager

class TestDiningExperienceManager(unittest.TestCase):

    def setUp(self):
        self.manager = DiningExperienceManager()


   
        
   
    def test_calculate_cost(self):
        # Test with no order
        order = {}
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 0)

        # Test with 1 meal and quantity of 1
        order = {"Italian food": 1}
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 12)

        # Test with multiple meals and quantities
        order = {
            "Chinese food": 2,
            "Italian food": 3,
            "Pastries": 2,
            "Mexican food": 4,
            "Vegetarian": 1,
            "Chef's Specials": 1,
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 86)

    
        order = {"Italian food": 1, "Pastries": 1}
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 17)

        order = {"Italian food": 1, "Pastries": 1, "Mexican food": 1}
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 28)


        order = {"Chef's Specials": 1}
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 15)


        order = {
            "Italian food": 2,
            "Chef's Specials": 3,
            "Vegetarian": 3,
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 75)
        
        
        order = {

            "Chef's Specials": 2
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 31)

        order = {
            "Mexican food": 5,
            "Vegetarian": 3
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 61)

        order = {
            "Italian food": 2,
            "Vegetarian": 5,
            "Chef's Specials": 10
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 124)
        
        order = {
            "Italian food": 2,
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 24)
        
        order = {
            "Vegetarian": 5,
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 40)
        
        
        order = {
            "Chinese food": 9,
            "Italian food": 3,
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 80)
        
        order = {
            "Pastries": 2,
            "Mexican food": 1,
            "Vegetarian": 1,
            "Chef's Specials": 1,
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 44)
        
        
        order = {
            "Chinese food": 6,
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 44)
        
        order = {
            "Chinese food": 9,
            
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 71)
        
        order = {
            "Chinese food": 2,
            "Italian food": 3,
            "Pastries": 2,
            "Mexican food": 4,
            "Vegetarian": 1,
            "Chef's Specials": 40,
        }
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 503)


    def test_confirm_order4(self):
        # ... (previously defined test cases)

        # Test order cancellation for each menu item individually
        menu_items = self.manager.menu.keys()
        for item in menu_items:
            order = {item: 1}
            total_cost = self.manager.menu[item]

            # Use mock.patch to capture the output and simulate user input ('n' for no)
            with mock.patch('builtins.input', side_effect=['n']):
                confirmed = self.manager.confirm_order(order, total_cost)
                self.assertFalse(confirmed)

    def test_get_valid_quantity(self):
        # ... (previously defined test cases)

        # Test invalid quantity input (negative number)
        with mock.patch('builtins.input', side_effect=['-5', '3']):
            quantity = self.manager.get_valid_quantity("Enter quantity: ")
            self.assertEqual(quantity, 3)


    def test_total_cost_discounts(self):
        # Test with more than 5 meals and > $50 (10% discount)
        order = {
            "Chinese food": 2,
            "Italian food": 1,
            "Pastries": 3,
            "Mexican food": 4,
        }
        # Total cost without discount = 20 + 12 + 15 + 44 = 91
        # Quantity discount (10% off): 91 * 0.9 = 81.9
        # Additional discount (>$50): 81.9 - 10 = 71.9
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 71)

        # Test with more than 10 meals (20% discount)
        order = {
            "Italian food": 3,
            "Pastries": 3,
            "Mexican food": 4,
            "Vegetarian": 3,
            "Chef's Specials": 3,
        }
        # Total cost without discount = 36 + 15 + 44 + 24 + 45 = 164
        # Quantity discount (20% off): 164 * 0.8 = 131.2
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 84)

    def test_total_cost_additional_discount(self):
        # Test with more than $100 (additional $25 discount)
        order = {
            "Italian food": 5,
            "Chef's Specials": 6,
        }
        # Total cost without discount = 60 + 90 = 150
        # Quantity discount (20% off): 150 * 0.8 = 120
        # Additional discount (>$100): 120 - 25 = 95
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 76)

        # Test with exactly $100 (no additional discount)
        order = {
            "Italian food": 5,
            "Chef's Specials": 5,
        }
        # Total cost without discount = 60 + 75 = 135
        # Quantity discount (20% off): 135 * 0.8 = 108
        total_cost = self.manager.calculate_cost(order)
        self.assertEqual(total_cost, 89)




       
if __name__ == '__main__':
    unittest.main()