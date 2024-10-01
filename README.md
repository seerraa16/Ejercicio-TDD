# Ejercicio TDD
## Alejandro Serrano Catalina
Link al repositorio: https://github.com/seerraa16/Ejercicio-TDD.git

### Ejercicio;
Imagina que necesitamos implementar una función que calcule el factorial de un número. Si aplicamos la metodología de Desarrollo Basado en Pruebas (TDD), el primer paso es crear una función vacía, únicamente para poder llamarla. Luego, escribiremos una prueba que verifique su funcionamiento y la ejecutaremos para comprobar que efectivamente falla, como se espera.

Paso 1: Creación de Archivos y Estructura Inicial
Primero, vamos a crear un archivo llamado myfactorial.py, en el que definiremos la función factorial. Esta función inicialmente no hará nada, simplemente devolverá un valor predeterminado (como 0) para que podamos probarla. Luego, crearemos un archivo llamado test_.py, en el que escribiremos una prueba unitaria para verificar el cálculo del factorial.

Código en myfactorial.py:

´´´
def factorial(numero):
    return 0
´´´

Código en test_.py:

´´´
import pytest
import myfactorial

def test_myfactorial():
    assert myfactorial.factorial(3) == 6
´´´
Paso 2: Ejecutar la Prueba Inicial
Una vez que tengamos estos archivos, abrimos una terminal en el directorio donde están ubicados y ejecutamos el siguiente comando para correr las pruebas:


pytest test_.py
Este comando ejecutará la prueba y, dado que la función factorial aún no está correctamente implementada, la prueba fallará, lo cual es el comportamiento esperado en TDD.

Paso 3: Implementar la Función Factorial
Ahora, procedemos a implementar la lógica necesaria para calcular el factorial en la función factorial.

Código actualizado en myfactorial.py:

´´´

def factorial(numero):
    fact = 1
    for i in range(1, numero + 1):
        fact *= i
    return fact
´´´

Paso 4: Volver a Ejecutar las Pruebas
Después de haber implementado la función, volvemos a ejecutar el comando pytest test_.py. Si todo está correcto, la prueba debería pasar sin problemas, lo que indicará que nuestra función ahora calcula correctamente el factorial.

El resultado esperado en la terminal será algo similar a:


===================================== test session starts =====================================
platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/marcos/Desktop/Curso
collected 1 item

test_.py .                                                                              [100%]

====================================== 1 passed in 0.01s ======================================
Paso 5: Ampliar las Pruebas
Ahora es tu turno. Debes implementar pruebas adicionales que verifiquen el comportamiento de la función factorial en casos especiales. Por ejemplo, debes escribir pruebas que comprueben:

Qué sucede cuando intentas calcular el factorial de 0.
Qué sucede cuando intentas calcular el factorial de un número negativo.
Después de escribir estas pruebas, ejecútalas y observa los resultados. Si alguna prueba falla, refactoriza la función factorial hasta que pase todas las pruebas.

Criterios de Evaluación
Comprensión del Proceso TDD: El estudiante debe demostrar que entiende el ciclo "Rojo-Verde-Refactor" de TDD, mostrando la capacidad de escribir una prueba que inicialmente falla, implementar la funcionalidad necesaria para pasar la prueba, y refactorizar el código si es necesario.

Implementación Correcta del Código: El código debe estar correctamente estructurado, cumplir con los requisitos especificados (como calcular el factorial), y pasar todas las pruebas unitarias proporcionadas.

Manejo de Casos Especiales: El estudiante debe ser capaz de identificar y manejar correctamente casos especiales, como el cálculo del factorial de 0 o de un número negativo, a través de pruebas y modificaciones en el código.

Uso de Herramientas de Pruebas: El estudiante debe ser capaz de utilizar pytest u otra herramienta de pruebas de manera efectiva para ejecutar sus pruebas y analizar los resultados.

Refactorización del Código: El estudiante debe mostrar habilidad para refactorizar el código de manera que sea más eficiente, legible o mantenible, sin cambiar su funcionalidad.
