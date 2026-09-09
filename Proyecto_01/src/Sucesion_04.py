import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

"""
EJERCICIO 4

Verificar si la sucesión n/(n+1), que va de n=1 hasta infinito, converge o diverge.
Los términos de la sucesión son:
    1/2, 2/3, 3/4, 4/5, ...
A medida que n aumenta, los términos crecen y se aproximan a 1.

Para probar la convergencia se utiliza el Teorema de Weierstrass:
TEOREMA DE WEIERSTRASS
Toda sucesión monótona y acotada es convergente.
"""

# Generemos la función 4
def sucesion_04(n):
    """
    Genera los primeros n términos de la sucesión
    a_n = n / (n + 1).
    """
    terminos = []

    for i in range(1, n + 1):
        terminos.append(i / (i + 1))

    return np.array(terminos)

# Comprobemos si la sucesion es creciente
def es_creciente(terminos):
    """
    Verifica computacionalmente que
    a_{n+1} - a_n > 0
    para todos los términos evaluados.
    """
    terminos = np.asarray(terminos)

    diferencias = np.diff(terminos)

    return np.all(diferencias > 0)

# Verificamos si la sucesión está acotada superiormente
def esta_acotada_superiormente(terminos, cota):
    """
    Verifica que todos los términos evaluados
    sean menores o iguales que una cota superior.
    """
    terminos = np.asarray(terminos)
    
    return np.all(terminos <= cota)

RAIZ = Path(__file__).resolve().parent.parent
GRAFICAS = RAIZ / "graficas"

# Medimos el error respecto al límite
def errores(terminos, limite):
    """Error absoluto |a_n - L| respecto al límite propuesto."""
    return np.abs(np.asarray(terminos) - limite)

if __name__ == "__main__":
    N = 30

    n = np.arange(1, N + 1)
    a = sucesion_04(N)

    print("Términos:", a[:4], "...", a[-1])

    # Teorema de Weierstrass
    creciente = es_creciente(a)
    acotada = esta_acotada_superiormente(a, 1)

    print("\n--- Teorema de Weierstrass ---")
    print("¿La sucesión es monótona creciente?", creciente)
    print("¿Está acotada superiormente por 1?", acotada)
    print("¿Cumple las hipótesis de Weierstrass?", creciente and acotada)

    # Error respecto al límite L = 1
    e = errores(a, 1)
    razon = e[1:] / e[:-1]

    print("\n--- Velocidad de convergencia ---")
    print(f"Error en n=1:   {e[0]:.3e}")
    print(f"Error en n={N}: {e[-1]:.3e}")
    print("Razón e_{n+1}/e_n:", razon[:5])

    # Gráfica
    plt.plot(n, a, "o-", ms=4, label=r"$a_n=n/(n+1)$")
    plt.axhline(1, linestyle="--", label="Cota y límite L = 1")

    plt.xlabel("n")
    plt.ylabel("valor")
    plt.title("Sucesión n/(n+1)")
    plt.legend()
    plt.grid(True)

    plt.savefig(GRAFICAS / "ej04.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("\nFigura guardada en graficas/ej04.png")