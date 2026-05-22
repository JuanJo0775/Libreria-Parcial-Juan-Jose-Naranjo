
from behave import given, when, then
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from product import Product


@given('un producto llamado "{name}" con un precio base de {price:d}')
def step_given_producto(context, name, price):
    context.product = Product(name, price)
    context.error = None

@when('aplico un descuento del {discount:d} por ciento')
def step_when_aplico_descuento(context, discount):
    context.product.apply_discount(discount)

@when('intento aplicar un descuento del {discount:d} por ciento')
def step_when_intento_aplicar_descuento(context, discount):
    try:
        context.product.apply_discount(discount)
    except ValueError as e:
        context.error = e

@when('solicito el precio final')
def step_when_solicito_precio_final(context):
    pass

@then('el precio con descuento debe ser {expected_price:d}')
def step_then_precio_descuento(context, expected_price):
    assert context.product.discounted_price == expected_price, f"Esperado {expected_price}, pero fue {context.product.discounted_price}"

@then('el sistema debe rechazarlo con el mensaje "{expected_message}"')
def step_then_rechazo_mensaje(context, expected_message):
    assert context.error is not None, "Se esperaba un error"
    assert str(context.error) == expected_message, f"Esperado '{expected_message}', pero fue '{str(context.error)}'"

@then('el precio final debe ser aproximadamente {expected_price:d}')
def step_then_precio_final(context, expected_price):
    final_price = context.product.get_final_price()
    assert abs(final_price - expected_price) < 1, f"Esperado ~{expected_price}, pero fue {final_price}"