import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


"""
SERIE 3

Verificar si la serie

    1 + 1/1! + 1/2! + 1/3! + ...

converge o diverge.

Sus términos son:

    a_n = 1/n!

y sus sumas parciales son:

    S_N = 1 + 1/1! + ... + 1/N!

Esta serie converge al número e:

    S_N -> e.
"""


# Generamos los términos de la serie
def serie_03(n):
    """
    Genera los primeros n términos de la serie
    a_n = 1/n!, comenzando con a_0 = 1.
    """
    terminos = [1.0]

    for i in range(1, n):
        terminos.append(terminos[-1] / i)

    return np.array(terminos)


# Calculamos las sumas parciales
def sumas_parciales(terminos):
    """
    Calcula las sumas parciales S_N.
    """
    return np.cumsum(terminos)

def verifica_criterio_razon(terminos):
    """
    Verifica computacionalmente que

        a_{n+1}/a_n = 1/(n+1)

    para a_n = 1/n!.
    """
    terminos = np.asarray(terminos)

    razones = terminos[1:] / terminos[:-1]

    n = np.arange(len(razones))
    razones_teoricas = 1 / (n + 1)

    return {
        "formula": np.allclose(razones, razones_teoricas),
        "razones": razones,
        "ultima_razon": razones[-1]
    }

# Medimos el error respecto al límite e
def errores(sumas, limite):
    """
    Error absoluto |S_N - L|.
    """
    return np.abs(np.asarray(sumas) - limite)


RAIZ = Path(__file__).resolve().parent.parent
GRAFICAS = RAIZ / "graficas"
GRAFICAS.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    N = 15
    n = np.arange(N)

    a = serie_03(N)
    S = sumas_parciales(a)
    
    r = verifica_criterio_razon(a)

    print("\n--- Criterio de la razón ---")
    print(
        "¿Se cumple a_(n+1)/a_n = 1/(n+1)?",
        r["formula"]
    )
    print(
        f"Última razón calculada: {r['ultima_razon']:.6f}"
    )
    print("Como 1/(n+1) -> 0 < 1, la serie converge.")

    print("Primeros términos:", a[:5])
    print("Primeras sumas parciales:", S[:5])

    print("\n--- Convergencia ---")
    print(f"S_{N-1} = {S[-1]:.10f}")
    print(f"e = {np.e:.10f}")

    # Error respecto al límite e
    error = errores(S, np.e)
    razon_error = error[1:] / error[:-1]

    print("\n--- Velocidad de convergencia ---")
    print(f"Error inicial: {error[0]:.3e}")
    print(f"Error final:   {error[-1]:.3e}")
    print("Razón e_{n+1}/e_n:", razon_error[:5])

    # Gráfica
    plt.plot(n, S, "o-", ms=4, label=r"$S_N$")
    plt.axhline(np.e, linestyle="--", label=r"$e$")

    plt.xlabel("n")
    plt.ylabel("S_N")
    plt.title("Serie de 1/n!")
    plt.legend()
    plt.grid(True)

    plt.savefig(GRAFICAS / "serie03.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("\nFigura guardada en graficas/serie03.png")