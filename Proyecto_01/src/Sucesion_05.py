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

Primero verificamos que la sucesión es monótona no decreciente:

    f_{n+1} - f_n >= 0.

Después verificamos la cota inferior:

    f_n >= n - 1.

Como n - 1 -> +infinito, entonces f_n -> +infinito.

Por lo tanto, la sucesión diverge.
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
GRAFICAS.mkdir(parents=True, exist_ok=True)


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
    plt.semilogy(
        n,
        f,
        "o-",
        ms=4,
        label=r"$f_n$"
    )

    plt.semilogy(
        n[1:],
        n[1:] - 1,
        "--",
        label=r"$n-1$"
    )

    plt.xlabel("n")
    plt.ylabel("valor (escala log)")
    plt.title("Fibonacci y su cota inferior")
    plt.legend()
    plt.grid(True, which="both")

    plt.savefig(
        GRAFICAS / "sucesion05.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()