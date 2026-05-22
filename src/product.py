class Product:
    def __init__(self, name, price):
        if price <= 0:
            raise ValueError("el precio debe ser mayor a cero")
        self.name = name
        self.price = price
