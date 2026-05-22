Feature: Calculo de descuento y precio final para Libreria del Centro
  Como administrador de la tienda
  Quiero aplicar descuentos y calcular precios finales con IVA
  Para que los clientes vean los precios precisos en el checkout

  Background:
    Given un producto llamado "Libro de Algebra" con un precio base de 10000

  @descuento @valido
  Scenario: Aplicar un descuento valido
    When aplico un descuento del 20 por ciento
    Then el precio con descuento debe ser 8000

  @descuento @limite
  Scenario Outline: Aplicar descuento en valores limite
    When aplico un descuento del <descuento> por ciento
    Then el precio con descuento debe ser <precio_esperado>

    Examples:
      | descuento | precio_esperado |
      | 0         | 10000           |
      | 40        | 6000            |

  @descuento @error
  Scenario: Rechazar un descuento mayor al 40 por ciento
    When intento aplicar un descuento del 50 por ciento
    Then el sistema debe rechazarlo con el mensaje "el descuento no puede superar el 40 por ciento"

  @precio-final @valido
  Scenario: Calcular precio final con descuento e IVA
    When aplico un descuento del 20 por ciento
    And solicito el precio final
    Then el precio final debe ser aproximadamente 9520

  @precio-final @limite
  Scenario: Calcular precio final sin descuento e IVA
    When aplico un descuento del 0 por ciento
    And solicito el precio final
    Then el precio final debe ser aproximadamente 11900
