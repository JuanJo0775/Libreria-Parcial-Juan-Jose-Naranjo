## SECCIÓN TEÓRICA — 2.0 puntos
### Archivo: `TEORIA.md` en el repositorio

---

**PREGUNTAS DE SELECCIÓN MÚLTIPLE**
*Escribe el ID de la respuesta correcta y explica en una línea por qué las otras son incorrectas.*

**SM-1 (0.3 puntos)**

Un equipo de desarrollo termina de escribir toda la funcionalidad de un módulo y luego le pide al QA que diseñe las pruebas. Según lo visto en clase, ¿cómo se llama este enfoque y cuál es su principal problema?

A. Shift-left testing. El problema es que las pruebas se vuelven demasiado técnicas para que el cliente las entienda.

B. Shift-right testing. El problema es que las pruebas solo se pueden ejecutar en producción.

C. Desarrollo tradicional con pruebas al final. El problema es que los defectos se detectan tarde, cuando corregirlos cuesta hasta 100 veces más que si se hubieran encontrado en etapas tempranas. (correcta)

D. Integración continua. El problema es que requiere un pipeline de CI/CD que el equipo no tiene configurado.

---

**SM-2 (0.3 puntos)**

Un desarrollador escribe el siguiente ciclo: primero implementa la función `calcular_descuento()` completa con todos los casos que se le ocurren, luego escribe los tests para verificar que funciona. ¿Qué regla de TDD está violando?

A. La regla del refactor, porque debería mejorar el código antes de escribir tests.

B. La primera regla de Uncle Bob: no escribir código de producción sin que exista primero un test que falle. El código fue escrito antes de que ningún test lo requiriera. (correcta)

C. La regla del Green, porque el código debería ser mínimo y no cubrir todos los casos desde el inicio.

D. No está violando ninguna regla. TDD permite escribir el código primero siempre que los tests se escriban inmediatamente después.

---

**PREGUNTAS ABIERTAS**
*Responde con tus propias palabras. La extensión ideal es entre 5 y 8 líneas por pregunta. No se piden definiciones de diccionario: se pide que demuestres que entendiste el concepto.*

**PA-1 (0.3 puntos)**

Durante la semana 4 implementamos el carrito de compras con TDD y en el primer ciclo, el paso GREEN consistió en escribir el código más simple posible aunque fuera "feo". Explica por qué TDD obliga a hacer esto en el GREEN y qué pasaría con el proceso si el desarrollador aprovecha ese paso para escribir código "limpio y completo" desde el inicio.

PA-1 respuesta:

En TDD el paso GREEN obliga a escribir el código más simple posible porque el objetivo de ese momento no es diseñar la solución perfecta, sino únicamente hacer que el test pase. Esto mantiene ciclos pequeños, rápidos y fáciles de entender. 
---

**PA-2 (0.3 puntos)**

Explica con tus propias palabras la diferencia entre TDD y BDD. No es suficiente decir que uno usa código y el otro usa Gherkin. Explica qué problema resuelve cada uno, a quién está dirigido y por qué se complementan en lugar de reemplazarse.

PA-2 respuesta:

TDD y BDD buscan mejorar la calidad del software, pero resuelven problemas distintos el TDD esta orientado principalmente a los desarrolladores y se enfoca en construir código correcto desde el inicio mediante tests automatizados escritos antes del código Ayuda al diseño técnico, reduce bugs y facilita refactorizar. BDD busca mejorar la comunicación entre negocio usando escenarios entendibles para todos se buaca asegurar que el sistema haga realmente lo que el cliente espera por eso se complementan: TDD garantiza calidad técnica interna y BDD valida el comportamiento esperado del negocio
---

**PA-3 (0.3 puntos)**

Un compañero te muestra su suite de pruebas y dice: "Tengo 95% de cobertura de código, así que mi sistema no tiene bugs." Explica por qué esa afirmación es incorrecta. Usa un ejemplo concreto que demuestre que cobertura alta no garantiza ausencia de defectos.

PA-3 respuesta:

La cobertura de código solo indica qué porcentaje del código fue ejecutado por los tests, pero no garantiza que los tests sean buenos ni que validen correctamente los resultados, un sistema puede tener 95% de cobertura y aun así contener errores graves

---

**PA-4 (0.2 puntos)**

En el contexto de la Regla 2 del examen (descuento entre 0% y 40%), un compañero dice que basta con probar el descuento del 20% porque "si funciona con ese valor, funciona con todos". Explica por qué esa lógica es incorrecta y qué valores concretos deberías probar tú y por qué.

PA-4 respuesta:

Esa lógica es incorrecta porque probar un solo valor no garantiza que los límites funcionen bien. Los errores normalmente aparecen en los casos borde y no en los valores normale si la regla permite descuentos entre 0% y 40%, yo probaría valores como 0%, 1%, 20%, 39%, 40% y tambien valores inválidos como -1% y 41%. los límites son importantes porque muchas veces los desarrolladores se equivocan 
---

**PA-5 (0.3 puntos)**

Mirando el planeador de la asignatura, las semanas 3 y 4 cubren pruebas ágiles, TDD y BDD. Explica cómo estas prácticas se conectan con el concepto de CI/CD que veremos en la semana 6. ¿Qué pasaría con un pipeline de CI/CD si el equipo no tiene una suite de tests automatizados sólida?

PA-5 respuesta:

CI/CD depende completamente de una suite de pruebas automatizadas sólida en integración continua, cada cambio que un desarrollador sube al repositorio ejecuta automáticamente pruebas para detectar errores rápidamente. TDD y BDD ayudan a construir esa base de pruebas desde etapas tempranas y de manera constante
si el equipo no tiene buenos tests automatizados, el pipeline pierde confiabilidad porque no puede validar si el sistema sigue funcionando después de cada cambio esso provocaría despliegues inseguros, bugs y necesidad de hacer muchas verificaciones manuales
---