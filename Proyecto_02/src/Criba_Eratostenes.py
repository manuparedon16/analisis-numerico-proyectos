import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

"""
Para desarrollar la Criba de Eratóstenes, el profesor presenta un código en GNU Octave,
pero en este proyecto interpretaré la misma lógica utilizando Python.

Básicamente, la idea consiste en crear una lista con los números naturales desde 2 hasta n.
Después se toma el primer número disponible de la lista, se considera primo y se eliminan
todos sus múltiplos. El proceso se repite con el siguiente número que no haya sido eliminado.

Por ejemplo, primero se toma el 2 y se eliminan 4, 6, 8, 10, ...
Después se toma el 3 y se eliminan 6, 9, 12, 15, ...
Posteriormente se continúa con 5, 7, etc.

Los números que sobreviven al proceso de eliminación son precisamente los números primos.

La diferencia principal será de lenguaje: Octave trabaja con vectores
y concatenación, mientras que en Python usaremos listas y el operador módulo, pero la lógica de
reconstruir la lista en cada paso es la misma.

El objetivo será aplicar este procedimiento hasta n = 5000 y obtener la lista completa
de números primos menores o iguales a 5000.
"""

# Generamos la sucesion para crear la Criba de Eratostenes
def sucesion_eratostenes(n):
    """
    Genera los números naturales desde 2 hasta n
    que serán los candidatos iniciales de la criba.
    """
    terminos = []
    
    for i in range(2, n + 1):
        terminos.append(i)
    
    return np.array(terminos)

# Tomamos los candidatos y vamos eliminando sus multiplos
def eliminar_multiplos(terminos):
    """
    Aplica la lógica de la Criba de Eratóstenes.

    En cada paso toma el primer número disponible,
    lo guarda como primo y elimina sus múltiplos.
    """
    terminos = list(terminos)
    primos = []
    
    # Como no sabemos cuantas veces se repetira el proceso, en vez de usar un for, usamos un while
    while len(terminos) > 0:
        # 1. Tomar el primer numero de la lista "terminos"
        criba = terminos[0]
        # 2. Guardarlo en la lista "primos"
        primos.append(criba)
        
        nuevos_terminos = []
        
        for numero in terminos:
            # 3. Si numero NO es multiplo del primo actual, lo agregamos nuevamente a nuevos_terminos
            if numero % criba != 0:
                nuevos_terminos.append(numero)

        # 4. Actualizamos la lista con los numeros que sobrevivieron
        terminos = nuevos_terminos
        
    return np.array(primos)

# terminos = sucesion_eratostenes(5000)
# primos = eliminar_multiplos(terminos)

# print(primos)

# Hacemos una funcion para graficar la funcion pi que menciona el profe en el PDF
def graficar_pi(n, primos, ruta_salida):
    """
    Grafica la función pi(n) y la compara con n / ln(n).
    """

    x = np.arange(2, n + 1)

    es_primo = np.zeros(n + 1, dtype=int)

    for primo in primos:
        es_primo[primo] = 1

    pi_n = np.cumsum(es_primo)

    aproximacion = x / np.log(x)

    plt.figure(figsize=(10, 6))

    plt.plot(x, pi_n[2:], label=r"$\pi(n)$")
    plt.plot(x, aproximacion, "--", label=r"$n/\ln(n)$")

    plt.title("Función de conteo de números primos")
    plt.xlabel("n")
    plt.ylabel("Cantidad de números primos")
    plt.legend()
    plt.grid(alpha=0.3)

    plt.savefig(ruta_salida, dpi=300, bbox_inches="tight")
    plt.close()

# Hacemos una segunda grafica para graficar los huecos entre primos
def graficar_huecos(primos, ruta_salida):
    """
    Grafica la distancia entre números primos consecutivos.
    """

    huecos = np.diff(primos)

    plt.figure(figsize=(10, 6))

    plt.scatter(primos[:-1], huecos, s=15)

    plt.title("Huecos entre números primos consecutivos")
    plt.xlabel("Número primo")
    plt.ylabel("Distancia al siguiente primo")
    plt.grid(alpha=0.3)

    plt.savefig(ruta_salida, dpi=300, bbox_inches="tight")
    plt.close()
    
def main():

    # Valor solicitado en la tarea
    n = 5000

    # Generamos los candidatos iniciales
    terminos = sucesion_eratostenes(n)

    # Aplicamos la Criba de Eratóstenes
    primos = eliminar_multiplos(terminos)

    # Resultados principales
    print(f"Números primos menores o iguales a {n}:")
    print(primos)

    print()
    print(f"Cantidad de números primos: {len(primos)}")
    print(f"Aproximación n / ln(n): {n / np.log(n):.4f}")

    # Localizamos la carpeta principal del proyecto
    carpeta_proyecto = Path(__file__).resolve().parent.parent

    # Carpeta donde se guardarán las gráficas
    carpeta_graficas = carpeta_proyecto / "graficas"
    carpeta_graficas.mkdir(exist_ok=True)

    # Rutas de las gráficas
    ruta_pi = carpeta_graficas / "funcion_pi.png"
    ruta_huecos = carpeta_graficas / "huecos_primos.png"

    # Generamos las gráficas
    graficar_pi(n, primos, ruta_pi)
    graficar_huecos(primos, ruta_huecos)

    print()
    print("Gráficas guardadas correctamente en la carpeta 'graficas'.")


if __name__ == "__main__":
    main()