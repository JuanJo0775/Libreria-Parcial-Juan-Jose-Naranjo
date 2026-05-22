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

if __name__ == '__main__':
    unittest.main()
