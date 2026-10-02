import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


"""
SERIE 1

Verificar si la serie armónica

    1 + 1/2 + 1/3 + 1/4 + ...

converge o diverge.

Para estudiar una serie analizamos sus sumas parciales:

    S_N = 1 + 1/2 + ... + 1/N.

Agrupando los términos en bloques de potencias de 2 se obtiene:

    S_(2^m) >= 1 + m/2.

Como 1 + m/2 tiende a infinito, las sumas parciales no están
acotadas superiormente.

Por lo tanto, la serie armónica diverge.
"""


# Generamos los términos de la serie
def serie_armonica(n):
    """
    Genera los primeros n términos de la serie armónica:
    a_n = 1/n.
    """
    indices = np.arange(1, n + 1)

    return 1 / indices


# Calculamos las sumas parciales
def sumas_parciales(terminos):
    """
    Calcula las sumas parciales:
    S_N = a_1 + a_2 + ... + a_N.
    """
    terminos = np.asarray(terminos)

    return np.cumsum(terminos)


# Verificamos la cota usada en la demostración
def verifica_cota_armonica(sumas):
    """
    Verifica en los índices N = 2^m que

        S_(2^m) >= 1 + m/2.
    """
    N = len(sumas)

    m = np.arange(1, int(np.log2(N)) + 1)
    indices = 2**m

    valores = sumas[indices - 1]
    cotas = 1 + m / 2

    return np.all(valores >= cotas)


RAIZ = Path(__file__).resolve().parent.parent
GRAFICAS = RAIZ / "graficas"
GRAFICAS.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    N = 100
    n = np.arange(1, N + 1)

    a = serie_armonica(N)
    S = sumas_parciales(a)

    print("Primeros términos:", a[:5])
    print("Primeras sumas parciales:", S[:5])

    # Verificamos que los términos tienden hacia cero
    print("\n--- Término general ---")
    print(f"a_1 = {a[0]:.4f}")
    print(f"a_{N} = {a[-1]:.4f}")

    # Verificamos la cota de la demostración
    cota = verifica_cota_armonica(S)

    print("\n--- Divergencia de la serie armónica ---")
    print("¿Se cumple S_(2^m) >= 1 + m/2?", cota)
    print(f"Última suma parcial S_{N}: {S[-1]:.4f}")

    # Gráfica
    plt.plot(n, S, label=r"$S_N=\sum_{n=1}^{N}1/n$")

    plt.xlabel("N")
    plt.ylabel("S_N")
    plt.title("Sumas parciales de la serie armónica")
    plt.legend()
    plt.grid(True)

    plt.savefig(GRAFICAS / "serie01.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("\nFigura guardada en graficas/serie01.png")