from app.car import Car


class Customer:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.product_cart = config["product_cart"]
        self.location = config["location"]
        self.money = config["money"]
        self.car = Car(
            config.get("car").get("brand"),
            config.get("car").get("fuel_consumption")
        )

    def calculate_total_costs(self, shops: list, fuel_price: float) -> list:
        costs = []
        for shop in shops:
            fuel_cost = self.car.cost_fuel(
                self.location,
                shop.location,
                fuel_price
            )
            products_cost = shop.cost_of_products(self.product_cart)
            total = fuel_cost + products_cost
            costs.append((shop, round(total, 2)))
        return costs
