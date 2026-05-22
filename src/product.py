class Product:
    def __init__(self, name, price):
        self._validate_price(price)
        self.name = name
        self.price = price

    def _validate_price(self, price):
        if price <= 0:
            raise ValueError("el precio debe ser mayor a cero")

    def apply_discount(self, discount):
        if discount < 0:
            raise ValueError("el descuento no puede ser negativo")
        if discount > 40:
            raise ValueError("el descuento no puede superar el 40 por ciento")
        self.discounted_price = self.price * (1 - discount / 100)
