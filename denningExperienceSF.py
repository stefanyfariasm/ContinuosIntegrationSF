class DiningExperienceManager:
    def __init__(self):
        self.menu = {
            "Chinese food": 10,
            "Italian food": 12,
            "Pastries": 5,
            "Mexican food": 11,
            "Vegetarian": 8,
            "Chef's Specials": 15,

        }

    def calculate_cost(self, order):
        base_cost = 0
        special_meal_surcharge = 0
        total_quantity = sum(order.values())

        for meal, quantity in order.items():
            if meal in self.menu:
                base_cost += self.menu[meal] * quantity
                if meal == "Chef's Specials":
                    special_meal_surcharge += self.menu[meal] * 0.05 * quantity

        total_cost = base_cost + special_meal_surcharge

        if total_quantity > 5:
            total_cost *= 0.9  # 10% discount for more than 5 meals
        if total_quantity > 10:
            total_cost *= 0.8  # Additional 20% discount for more than 10 meals

        if total_cost > 50:
            total_cost -= 10  # $10 discount if total cost is more than $50
        if total_cost > 100:
            total_cost -= 25  # $25 discount if total cost is more than $100

        return int(total_cost)

    def confirm_order(self, order, total_cost):
        print("Selected Meals:")
        for meal, quantity in order.items():
            print(f"{meal}: {quantity}")
        print(f"Total Cost: ${total_cost}")

        while True:
            user_input = input("Confirma la orden(s/n): ").strip().lower()
            if user_input == 's':
                return True
            elif user_input == 'n':
                return False
            else:
                print("Ingresa 's' para confirmar o 'n' para cancelar la orden.")

    def get_valid_quantity(self, prompt):
        while True:
            try:
                quantity = int(input(prompt))
                if 1 <= quantity <= 100:
                    return quantity
                else:
                    print("Invalido. Ingresa un número entre 1 y 100.")
            except ValueError:
                print("Ingresa un número.")


if __name__ == "__main__":
    manager = DiningExperienceManager()

    print("Menu:")
    for meal in manager.menu:
        print(f"{meal}: ${manager.menu[meal]}")

    order = {}
    while True:
        meal_choice = input("Ingresa el nombre de la comida que deseas (o 'x' to para finalizar): ").strip()
        if meal_choice.lower() == 'x':
            break

        if meal_choice in manager.menu:
            quantity = manager.get_valid_quantity(f"Cantidad {meal_choice}: ")
            order[meal_choice] = quantity
        else:
            print("Ingresa una comida que esté en el menú.")

    total_cost = manager.calculate_cost(order)
    print(f"Costo Total: ${total_cost}")

    if manager.confirm_order(order, total_cost):
        print("¡Orden confirmada!")
    else:
        print("Orden cancelada.")
