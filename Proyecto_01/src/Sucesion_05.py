import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

"""
EJERCICIO 5

Verificar si la sucesión de Fibonacci, definida por
f_1 = 1
f_2 = 1
f_n = f_{n-1} + f_{n-2}, para n >= 3,
converge o diverge.

Los primeros términos de la sucesión son:
1, 1, 2, 3, 5, 8, 13, ...

Para analizar su comportamiento verificaremos dos propiedades.
Primero, comprobaremos que la sucesión es monótona no decreciente, verificando que así que la sucesión de Fibonacci diverge.
"""

# Generamos la sucesión de Fibonacci
def fibonacci(n):
    """
    Genera los primeros n términos de la sucesión de Fibonacci:
    f_1 = 1, f_2 = 1, f_n = f_{n-1} + f_{n-2}.
    """
    terminos = [1,1]
    
    for i in range(2, n):
        terminos.append(terminos[i-1] + terminos[i-2])
    
    return np.array(terminos[:n])

# Verificamos que sea monótona no decreciente
def es_monotona(terminos):
    """
    Verifica que f_{n+1} - f_n >= 0
    para todos los términos evaluados.
    """
    terminos = np.asarray(terminos)
    
    diferencias = np.diff(terminos)
    
    return np.all(diferencias >= 0)

# Verificamos una cota inferior que crezca sin un límite
def verificar_cota_inferior(terminos):
    """
    Verifica que
    f_n >= n - 1, para n >= 2.
    """
    terminos = np.asarray(terminos)
    
    n = np.arange(1, len(terminos) + 1)
    
    return np.all(terminos[1:] >= (n[1:] - 1))

RAIZ = Path(__file__).resolve().parent.parent
GRAFICAS = RAIZ / "graficas"


if __name__ == "__main__":
    N = 30
    n = np.arange(1, N + 1)

    f = fibonacci(N)

    print("Términos:", f[:8], "...", f[-1])

    # Monotonía
    monotona = es_monotona(f)

    print("\n--- Monotonía ---")
    print("¿La sucesión es monótona no decreciente?", monotona)

    # Cota inferior creciente
    cota = verificar_cota_inferior(f)

    print("\n--- Cota inferior ---")
    print("¿Se cumple f_n >= n - 1?", cota)
    print(f"Último f_n: {f[-1]}")
    print(f"Último n-1: {n[-1] - 1}")

    # Gráfica
    plt.plot(n, f, "o-", ms=4, label=r"$f_n$")
    plt.plot(n, n - 1, "--", label=r"$n-1$")

    plt.xlabel("n")
    plt.ylabel("valor")
    plt.title("Sucesión de Fibonacci")
    plt.legend()
    plt.grid(True)

    plt.savefig(GRAFICAS / "ej05.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("\nFigura guardada en graficas/ej05.png")