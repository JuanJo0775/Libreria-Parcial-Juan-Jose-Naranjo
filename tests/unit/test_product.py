import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from product import Product

class TestProductRule1(unittest.TestCase):
    def test_crear_producto_precio_valido(self):
        product = Product("Libro", 50000)
        self.assertEqual(product.price, 50000)

    def test_crear_producto_precio_cero(self):
        with self.assertRaisesRegex(ValueError, "el precio debe ser mayor a cero"):
            Product("Libro", 0)

    def test_crear_producto_precio_negativo(self):
        with self.assertRaisesRegex(ValueError, "el precio debe ser mayor a cero"):
            Product("Libro", -100)


class TestProductRule2(unittest.TestCase):
    def setUp(self):
        self.product = Product("Libro", 10000)

    def test_aplicar_descuento_valido_20(self):
        self.product.apply_discount(20)
        self.assertEqual(self.product.discounted_price, 8000)

    def test_aplicar_descuento_0_sin_cambio(self):
        self.product.apply_discount(0)
        self.assertEqual(self.product.discounted_price, 10000)

    def test_aplicar_descuento_maximo_40(self):
        self.product.apply_discount(40)
        self.assertEqual(self.product.discounted_price, 6000)

    def test_descuento_mayor_a_40_error(self):
        with self.assertRaisesRegex(ValueError, "el descuento no puede superar el 40 por ciento"):
            self.product.apply_discount(50)

    def test_descuento_limite_41_error(self):
        with self.assertRaisesRegex(ValueError, "el descuento no puede superar el 40 por ciento"):
            self.product.apply_discount(41)

    def test_descuento_negativo_error(self):
        with self.assertRaisesRegex(ValueError, "el descuento no puede ser negativo"):
            self.product.apply_discount(-10)

class TestProductRule3(unittest.TestCase):
    def setUp(self):
        self.product = Product("Libro", 10000)

    def test_calcular_precio_final_con_descuento_e_iva(self):
        self.product.apply_discount(20)
        self.assertAlmostEqual(self.product.get_final_price(), 9520, places=2)

    def test_calcular_precio_final_sin_descuento_e_iva(self):
        self.product.apply_discount(0)
        self.assertAlmostEqual(self.product.get_final_price(), 11900, places=2)

    def test_calcular_precio_final_maximo_descuento_e_iva(self):
        self.product.apply_discount(40)
        self.assertAlmostEqual(self.product.get_final_price(), 7140, places=2)

    def test_precio_final_nunca_negativo(self):
        self.product.apply_discount(40)
        self.assertGreaterEqual(self.product.get_final_price(), 0)

if __name__ == '__main__':
    unittest.main()
