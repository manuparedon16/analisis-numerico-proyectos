import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


"""
SERIE 6

Verificar si la serie

    1/(1*3) + 1/(5*7) + 1/(9*11) + ...

converge o diverge.

El término general es:

    a_n = 1 / [(4n-3)(4n-1)]

Por fracciones parciales:

    a_n = 1/2 [1/(4n-3) - 1/(4n-1)]

Por lo tanto,

    sum a_n
    = 1/2 (1 - 1/3 + 1/5 - 1/7 + ...)

Como en la Serie 5 se obtuvo

    1 - 1/3 + 1/5 - 1/7 + ... = pi/4,

entonces

    sum a_n = pi/8.

Por lo tanto, la serie converge.
"""


# Generamos los términos de la serie
def serie_06(n):
    """
    Genera los primeros n términos:

        a_n = 1 / [(4n-3)(4n-1)].
    """
    indices = np.arange(1, n + 1)

    return 1 / ((4 * indices - 3) * (4 * indices - 1))


# Calculamos las sumas parciales
def sumas_parciales(terminos):
    """
    Calcula las sumas parciales S_N.
    """
    return np.cumsum(terminos)


# Verificamos la descomposición en fracciones parciales
def verifica_descomposicion(n):
    """
    Verifica que

    1/[(4n-3)(4n-1)]
    =
    1/2 [1/(4n-3) - 1/(4n-1)].
    """
    indices = np.arange(1, n + 1)

    izquierda = 1 / ((4 * indices - 3) * (4 * indices - 1))

    derecha = 0.5 * (
        1 / (4 * indices - 3)
        - 1 / (4 * indices - 1)
    )

    return np.allclose(izquierda, derecha)


# Medimos el error respecto al límite pi/8
def errores(sumas, limite):
    """
    Error absoluto |S_N - L|.
    """
    return np.abs(np.asarray(sumas) - limite)

RAIZ = Path(__file__).resolve().parent.parent
GRAFICAS = RAIZ / "graficas"
GRAFICAS.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    N = 50
    n = np.arange(1, N + 1)

    a = serie_06(N)
    S = sumas_parciales(a)

    print("Primeros términos:", a[:5])
    print("Primeras sumas parciales:", S[:5])

    # Fracciones parciales
    descomposicion = verifica_descomposicion(N)

    print("\n--- Fracciones parciales ---")
    print("¿Se cumple la descomposición?", descomposicion)

    # Error respecto al límite pi/8
    limite = np.pi / 8
    e = errores(S, limite)

    print("\n--- Convergencia ---")
    print(f"S_{N} = {S[-1]:.8f}")
    print(f"pi/8  = {limite:.8f}")
    print(f"Error = {e[-1]:.3e}")

    # Gráfica
    plt.plot(n, S, "o-", ms=3, label=r"$S_N$")
    plt.axhline(limite, linestyle="--", label=r"$\pi/8$")

    plt.xlabel("N")
    plt.ylabel("S_N")
    plt.title("Serie 1/[(4n-3)(4n-1)]")
    plt.legend()
    plt.grid(True)

    plt.savefig(GRAFICAS / "serie06.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("\nFigura guardada en graficas/serie06.png")