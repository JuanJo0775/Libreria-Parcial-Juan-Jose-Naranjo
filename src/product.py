class Product:
    def __init__(self, name, price):
        self._validate_price(price)
        self.name = name
        self.price = price

    def _validate_price(self, price):
        if price <= 0:
            raise ValueError("el precio debe ser mayor a cero")
