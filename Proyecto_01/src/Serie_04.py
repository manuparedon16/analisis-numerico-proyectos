import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


"""
SERIE 4

Verificar si la serie

    1 - 1/2 + 1/3 - 1/4 + 1/5 - ...

converge o diverge.

Es una serie alternante:

    sum (-1)^(n+1) / n

Para aplicar el criterio de Leibniz verificamos que:

    1/n > 0
    1/(n+1) <= 1/n
    1/n -> 0

Por lo tanto, la serie converge.

Además, su suma es:

    ln(2)
"""


# Generamos los términos de la serie
def serie_04(n):
    """
    Genera los primeros n términos de la serie
    a_n = (-1)^(n+1) / n.
    """
    indices = np.arange(1, n + 1)

    return ((-1) ** (indices + 1)) / indices


# Calculamos las sumas parciales
def sumas_parciales(terminos):
    """
    Calcula las sumas parciales S_N.
    """
    return np.cumsum(terminos)

# Verificamos leibniz
def verifica_leibniz(n):
    """
    Verifica computacionalmente que b_n = 1/n
    sea positiva y decreciente.

    También devuelve el último término calculado
    como evidencia numérica de que b_n se aproxima a 0.
    """
    indices = np.arange(1, n + 1)
    b = 1 / indices

    positiva = np.all(b > 0)
    decreciente = np.all(np.diff(b) < 0)

    return {
        "positiva": positiva,
        "decreciente": decreciente,
        "ultimo_b": b[-1]
    }


# Medimos el error respecto al límite ln(2)
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

    a = serie_04(N)
    S = sumas_parciales(a)

    print("Primeros términos:", a[:6])
    print("Primeras sumas parciales:", S[:6])

    leibniz = verifica_leibniz(N)

    print("\n--- Criterio de Leibniz ---")
    print("¿b_n > 0?", leibniz["positiva"])
    print("¿b_n es decreciente?", leibniz["decreciente"])
    print(f"Último b_n calculado: {leibniz['ultimo_b']:.4f}")
    print("Matemáticamente, 1/n -> 0.")

    # Error respecto al límite ln(2)
    limite = np.log(2)
    e = errores(S, limite)

    print("\n--- Convergencia ---")
    print(f"S_{N} = {S[-1]:.8f}")
    print(f"ln(2) = {limite:.8f}")
    print(f"Error = {e[-1]:.3e}")

    # Gráfica
    plt.plot(n, S, "o-", ms=3, label=r"$S_N$")
    plt.axhline(limite, linestyle="--", label=r"$\ln(2)$")

    plt.xlabel("N")
    plt.ylabel("S_N")
    plt.title("Serie armónica alternada")
    plt.legend()
    plt.grid(True)

    plt.savefig(GRAFICAS / "serie04.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("\nFigura guardada en graficas/serie04.png")