import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


"""
SERIE 2

Verificar si la serie

    1 + 1/2 + 1/4 + 1/8 + ...

converge o diverge.

Es una serie geométrica con razón r = 1/2.

Sus sumas parciales son:

    S_N = 2(1 - 1/2^N)

Como 1/2^N -> 0,

    S_N -> 2.

Por lo tanto, la serie converge a 2.
"""


# Generamos los términos de la serie
def serie_geometrica(n):
    """
    Genera los primeros n términos de la serie:
    a_n = (1/2)^(n-1).
    """
    indices = np.arange(n)

    return (1 / 2) ** indices


# Calculamos las sumas parciales
def sumas_parciales(terminos):
    """
    Calcula las sumas parciales S_N.
    """
    return np.cumsum(terminos)


# Verificamos la fórmula de la suma parcial
def verifica_formula(n, sumas):
    """
    Verifica que

        S_N = 2(1 - 1/2^N).
    """
    indices = np.arange(1, n + 1)

    formula = 2 * (1 - (1 / 2) ** indices)

    return np.allclose(sumas, formula)


# Medimos el error respecto al límite
def errores(sumas, limite):
    """Error absoluto |S_N - L|."""
    return np.abs(np.asarray(sumas) - limite)


RAIZ = Path(__file__).resolve().parent.parent
GRAFICAS = RAIZ / "graficas"
GRAFICAS.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    N = 30
    n = np.arange(1, N + 1)

    a = serie_geometrica(N)
    S = sumas_parciales(a)

    print("Primeros términos:", a[:5])
    print("Primeras sumas parciales:", S[:5])

    # Fórmula de la suma parcial
    formula = verifica_formula(N, S)

    print("\n--- Serie geométrica ---")
    print("¿Se cumple S_N = 2(1 - 1/2^N)?", formula)
    print(f"S_{N} = {S[-1]:.8f}")

    # Error respecto al límite L = 2
    e = errores(S, 2)
    razon = e[1:] / e[:-1]

    print("\n--- Velocidad de convergencia ---")
    print(f"Error en N=1:  {e[0]:.3e}")
    print(f"Error en N={N}: {e[-1]:.3e}")
    print("Razón e_{N+1}/e_N:", razon[:5])

    # Gráfica
    plt.plot(n, S, "o-", ms=4, label=r"$S_N$")
    plt.axhline(2, linestyle="--", label="Límite = 2")

    plt.xlabel("N")
    plt.ylabel("S_N")
    plt.title("Serie geométrica")
    plt.legend()
    plt.grid(True)

    plt.savefig(GRAFICAS / "serie02.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("\nFigura guardada en graficas/serie02.png")