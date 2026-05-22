class Product:
    def __init__(self, name, price):
        self._validate_price(price)
        self.name = name
        
        self.price = price
        self.discounted_price = None

    def _validate_price(self, price):
        if price <= 0:
            raise ValueError("el precio debe ser mayor a cero")

    def _validate_discount(self, discount):
        if discount < 0:
            raise ValueError("el descuento no puede ser negativo")
        
        if discount > 40:
            raise ValueError("el descuento no puede superar el 40 por ciento")

    def apply_discount(self, discount):
        self._validate_discount(discount)
        self.discounted_price = self.price * (1 - discount / 100)

    def _get_base_for_calculation(self):
        return self.discounted_price if self.discounted_price is not None else self.price


    def get_final_price(self):
        IVA_RATE = 1.19
        final_price = self._get_base_for_calculation() * IVA_RATE
        return max(0, final_price)
