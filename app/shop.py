import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def cost_of_products(self, product_cart: dict) -> float:
        cost = []
        for value, item in product_cart.items():
            cost.append(self.products[value] * item)
        return sum(cost)

    def print_receipt(self, name: str, products: dict) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {now}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")
        total = 0
        for value, item in products.items():
            cost = self.products[value] * item
            total += cost
            print(f"{item} {value}s for {cost: g} dollars".replace("  ", " "))
        print(f"Total cost is {total: g} dollars".replace("  ", " "))
        print("See you again!")
