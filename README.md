# Librería — Parcial

Autor: Juan José Naranjo

Breve descripción
:
Este documento recoge las particiones de equivalencia y los casos límite que usé para diseñar las pruebas del parcial. Traté de dejar notas claras para quien revise los casos.

Sección 1 — Regla 1: Precio base

- Precio mayor a cero — Tipo: Válida. Valor representativo: 100. Resultado esperado: producto creado correctamente.
- Precio igual a cero — Tipo: Inválida. Valor: 0. Resultado esperado: error: el precio debe ser mayor que cero.
- Precio negativo — Tipo: Inválida. Valor: -50. Resultado esperado: error: el precio debe ser mayor que cero.

Notas: el precio base no admite valores iguales o menores a cero.

Sección 2 — Regla 2: Descuento porcentual

- Descuento entre 0% y 40% — Tipo: Válida. Valor representativo: 20. Resultado esperado: descuento aplicado correctamente.
- Descuento igual a 0% — Tipo: Válida. Valor: 0. Resultado esperado: sin descuento; precio base sin modificar.
- Descuento igual a 40% — Tipo: Válida. Valor: 40. Resultado esperado: descuento máximo permitido.
- Descuento mayor a 40% — Tipo: Inválida. Valor: 50. Resultado esperado: error: descuento no puede superar el 40%.
- Descuento negativo — Tipo: Inválida. Valor: -10. Resultado esperado: error: descuento no puede ser negativo.

Comentario: el rango válido para descuentos es 0%–40% inclusive.

Sección 3 — Análisis de valores límite (Regla 2)

- Valor -1 — Tipo: Inválido (fuera por abajo). Resultado esperado: rechazado.
- Valor 0 — Tipo: Válido (borde inferior). Resultado esperado: aceptado.
- Valor 1 — Tipo: Válido (dentro del rango). Resultado esperado: aceptado.
- Valor 39 — Tipo: Válido (dentro del rango). Resultado esperado: aceptado.
- Valor 40 — Tipo: Válido (borde superior). Resultado esperado: aceptado.
- Valor 41 — Tipo: Inválido (fuera por arriba). Resultado esperado: rechazado.

Sección 4 — Pregunta al administrador (Regla 3)

Pregunta
: Si el descuento deja el precio muy cercano a cero y, al aplicar el IVA del 19%, el precio final resulta en una cifra menor a un centavo, ¿cómo debemos manejarlo: redondear, truncar o rechazar la operación?

Justificación
: El enunciado aclara que el precio final no puede ser negativo, pero no detalla el comportamiento ante precios fraccionarios extremadamente bajos. Esto influye en cómo escribir casos de borde y en la implementación del cálculo (redondeo/truncamiento).

---

## Lista de Casos de Prueba

- **TC-01 (Regla 1 - Positivo):** Crear producto con precio válido. Precondición: Ninguna. Datos: nombre="Libro", precio=50000. Pasos: Instanciar Product. Resultado: Producto creado con precio 50000.
- **TC-02 (Regla 1 - Negativo):** Crear producto con precio cero. Precondición: Ninguna. Datos: nombre="Libro", precio=0. Pasos: Instanciar Product. Resultado: Error "el precio debe ser mayor a cero".
- **TC-03 (Regla 1 - Negativo):** Crear producto con precio negativo. Precondición: Ninguna. Datos: nombre="Libro", precio=-100. Pasos: Instanciar Product. Resultado: Error "el precio debe ser mayor a cero".
- **TC-04 (Regla 2 - Positivo):** Aplicar descuento válido del 20%. Precondición: Producto con precio 10000. Datos: descuento=20. Pasos: Llamar apply_discount(20). Resultado: Precio con descuento = 8000.
- **TC-05 (Regla 2 - Borde):** Aplicar descuento en límite inferior (0%). Precondición: Producto precio 10000. Datos: descuento=0. Pasos: Llamar apply_discount(0). Resultado: Precio con descuento = 10000.
- **TC-06 (Regla 2 - Borde):** Aplicar descuento en límite superior (40%). Precondición: Producto precio 10000. Datos: descuento=40. Pasos: Llamar apply_discount(40). Resultado: Precio con descuento = 6000.
- **TC-07 (Regla 2 - Negativo):** Aplicar descuento mayor al 40%. Precondición: Producto precio 10000. Datos: descuento=50. Pasos: Llamar apply_discount(50). Resultado: Error "el descuento no puede superar el 40%".
- **TC-08 (Regla 3 - Positivo):** Calcular precio final con descuento e IVA. Precondición: Producto precio 10000, descuento 20%. Pasos: Llamar get_final_price(). Resultado: 9520.
- **TC-09 (Regla 3 - Borde):** Calcular precio final sin descuento. Precondición: Producto precio 5000, descuento 0%. Pasos: Llamar get_final_price(). Resultado: 5950.
- **TC-10 (Regla 2 - Borde):** Aplicar descuento justo encima del límite (41%). Precondición: Producto precio 10000. Datos: descuento=41. Pasos: Llamar apply_discount(41). Resultado: Error "el descuento no puede superar el 40%".

## Reporte de Cobertura (Coverage Report)

ejecutar con
```text
coverage run -m unittest tests/unit/test_product.py; coverage report
```
```text
OK
Name                         Stmts   Miss  Cover
------------------------------------------------
src\product.py                  23      0   100%
tests\unit\test_product.py      59      1    98%
------------------------------------------------
TOTAL                           82      1    99%
```

— Juan José
