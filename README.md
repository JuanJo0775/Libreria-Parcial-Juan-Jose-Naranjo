# Librería Parcial - Juan José Naranjo

## Sección 1: Particiones de Equivalencia - Regla 1 (precio base)

| Partición | Tipo | Valor Representativo | Resultado Esperado |
|---|---|---|---|
| Precio mayor a cero | Válida | 100 | Producto creado correctamente |
| Precio igual a cero | Inválida | 0 | Error: precio debe ser mayor a cero |
| Precio negativo | Inválida | -50 | Error: precio debe ser mayor a cero |

## Sección 2: Particiones de Equivalencia - Regla 2 (descuento porcentual)

| Partición | Tipo | Valor Representativo | Resultado Esperado |
|---|---|---|---|
| Descuento entre 0% y 40% | Válida | 20 | Descuento aplicado correctamente |
| Descuento igual a 0% | Válida | 0 | Sin descuento, precio base sin modificar |
| Descuento igual a 40% | Válida | 40 | Descuento máximo aplicado |
| Descuento mayor a 40% | Inválida | 50 | Error: descuento no puede superar el 40% |
| Descuento negativo | Inválida | -10 | Error: descuento no puede ser negativo |

## Sección 3: Análisis de Valores Límite - Regla 2

| Valor | Tipo | Resultado Esperado |
|---|---|---|
| -1 | Inválido (borde inferior fuera) | Rechazado |
| 0 | Válido (borde inferior) | Aceptado |
| 1 | Válido (dentro del rango) | Aceptado |
| 39 | Válido (dentro del rango) | Aceptado |
| 40 | Válido (borde superior) | Aceptado |
| 41 | Inválido (borde superior fuera) | Rechazado |

## Sección 4: Pregunta al administrador - Regla 3

**Pregunta:** Si el descuento aplicado lleva el precio a un valor muy cercano a cero y el IVA del 19% sobre ese resultado da un precio final menor a un centavo, ¿el sistema debe redondearlo, truncarlo o rechazar la operación?

**Justificación:** El enunciado dice que el precio final nunca puede ser negativo, pero no especifica el comportamiento ante precios finales no enteros o de valor extremadamente bajo, lo cual afecta el diseño de los casos de prueba de borde.
