import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


"""
SERIE 7

Verificar si la serie

    1/4 tan(pi/4) + 1/8 tan(pi/8) + 1/16 tan(pi/16) + ...

converge o diverge.

Usamos la identidad:

    tan(x) = cot(x) - 2cot(2x)

Esto convierte la serie en una serie telescópica.

Las sumas parciales cumplen:

    S_N = 1/(2^(N+1)) * cot(pi / 2^(N+1))

y cuando N -> infinito:

    S_N -> 1/pi.

Por lo tanto, la serie converge a 1/pi.
"""


# Generamos los términos de la serie
def serie_07(n):
    """
    Genera los primeros n términos de la serie.
    """
    k = np.arange(2, n + 2)

    return (1 / (2**k)) * np.tan(np.pi / (2**k))


# Calculamos las sumas parciales
def sumas_parciales(terminos):
    """
    Calcula las sumas parciales S_N.
    """
    return np.cumsum(terminos)

def cot(x):
    """
    Cotangente definida como cos(x)/sin(x).
    """
    return np.cos(x) / np.sin(x)

# Verificamos la identidad trigonométrica
def verifica_identidad(n):
    """
    Verifica numéricamente la identidad

        tan(x) = cot(x) - 2cot(2x).
    """
    k = np.arange(2, n + 2)
    x = np.pi / (2**k)

    izquierda = np.tan(x)
    derecha = cot(x) - 2 * cot(2 * x)

    return np.allclose(izquierda, derecha)

def verifica_suma_telescopica(sumas):
    """
    Verifica que las sumas parciales cumplen

        S_N = 1/2^(N+1) * cot(pi/2^(N+1)).
    """
    sumas = np.asarray(sumas)

    N = np.arange(1, len(sumas) + 1)

    formula = (
        1 / (2 ** (N + 1))
        * cot(np.pi / (2 ** (N + 1)))
    )

    return np.allclose(sumas, formula)

# Medimos el error respecto al límite
def errores(sumas, limite):
    """
    Error absoluto |S_N - L|.
    """
    return np.abs(np.asarray(sumas) - limite)


RAIZ = Path(__file__).resolve().parent.parent
GRAFICAS = RAIZ / "graficas"
GRAFICAS.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    N = 20
    n = np.arange(1, N + 1)

    a = serie_07(N)
    S = sumas_parciales(a)

    print("Primeros términos:", a[:5])
    print("Primeras sumas parciales:", S[:5])

    # Identidad trigonométrica
    identidad = verifica_identidad(N)
    telescopica = verifica_suma_telescopica(S)

    print("\n--- Serie telescópica ---")
    print(
        "¿Se cumple tan(x) = cot(x) - 2cot(2x)?",
        identidad
    )
    print(
        "¿Se cumple la fórmula de S_N?",
        telescopica
    )
    
    x = np.pi / (2 ** (N + 1))

    print("\n--- Límite ---")
    print(f"x*cot(x) = {x * cot(x):.10f}")
    print("Este valor se aproxima a 1.")

    # Error respecto al límite 1/pi
    limite = 1 / np.pi
    e = errores(S, limite)

    print("\n--- Convergencia ---")
    print(f"S_{N} = {S[-1]:.8f}")
    print(f"1/pi  = {limite:.8f}")
    print(f"Error = {e[-1]:.3e}")

    # Gráfica
    plt.plot(n, S, "o-", ms=4, label=r"$S_N$")
    plt.axhline(limite, linestyle="--", label=r"$1/\pi$")

    plt.xlabel("N")
    plt.ylabel("S_N")
    plt.title("Serie telescópica")
    plt.legend()
    plt.grid(True)

    plt.savefig(GRAFICAS / "serie07.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("\nFigura guardada en graficas/serie07.png")