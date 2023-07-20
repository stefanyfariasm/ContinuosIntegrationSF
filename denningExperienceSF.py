class DiningExperienceManager:
    def __init__(self):
        self.menu = {
            "Chinese Food": 10,
            "Italian Food": 12,
            "Pastries": 5,
            "Chef's Specials": 15,
        }
        self.special_meal_category = "Chef's Specials"
        self.max_order_quantity = 100

    def display_menu(self):
        print("Menu:")
        for category, price in self.menu.items():
            print(f"{category}: ${price}")

    def take_order(self):
        order = {}
        for category in self.menu:
            quantity = self.get_valid_quantity(f"How many {category} would you like to order? ")
            order[category] = quantity
        return order

    def get_valid_quantity(self, prompt):
        while True:
            try:
                quantity = int(input(prompt))
                if quantity <= 0 or quantity > self.max_order_quantity:
                    raise ValueError
                return quantity
            except ValueError:
                print("Please enter a positive integer not exceeding 100.")

    def calculate_cost(self, order):
        total_cost = 0
        special_category_surcharge = 0

        for category, quantity in order.items():
            if category in self.menu:
                if category == self.special_meal_category:
                    special_category_surcharge += self.menu[category] * 0.05
                total_cost += self.menu[category] * quantity

        if total_cost > 50:
            total_cost -= 10
        if total_cost > 100:
            total_cost -= 25

        if len(order) > 5:
            total_cost *= 0.9
        if len(order) > 10:
            total_cost *= 0.8

        total_cost += special_category_surcharge

        return total_cost

    def confirm_order(self, order, total_cost):
        print("Order Summary:")
        for category, quantity in order.items():
            print(f"{quantity} x {category}")

        print(f"Total Cost: ${total_cost}")
        confirm = input("Confirm the order? (y/n): ").lower()
        return confirm == 'y'

    def manage_dining_experience(self):
        self.display_menu()
        order = self.take_order()
        total_cost = self.calculate_cost(order)

        if total_cost == 0:
            print("No meals selected. Order canceled.")
        else:
            if self.confirm_order(order, total_cost):
                print("Order confirmed. Total cost: $", total_cost)
            else:
                print("Order canceled.")

if __name__ == "__main__":
    manager = DiningExperienceManager()
    manager.manage_dining_experience()
