import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


"""
EJERCICIO 3

Verificar si la sucesión (-1)^(n+1) / n, que va de n=1 hasta infinito, converge o diverge.

La sucesión alterna entre valores positivos y negativos, por lo que no es monótona.
Sin embargo, la magnitud de sus términos disminuye conforme aumenta n.

Para probar la convergencia se usa el Teorema del Sándwich:

TEOREMA DEL SÁNDWICH

Si existen tres sucesiones a_n, b_n y c_n tales que:
a_n <= b_n <= c_n 
para todo n suficientemente grande, y además:
lim a_n = lim c_n = L,
entonces
lim b_n = L.
"""

# Generamos la sucesión
def sucesion_03(n):
    """
    Genera los primeros n términos de la sucesión
    a_n = (-1)^(n+1) / n.
    """
    terminos = []

    for i in range(1, n + 1):
        terminos.append(((-1)**(i + 1)) / i)

    return np.array(terminos)


# Verificamos el teorema del sándwich
def verificar_sandwich(inferior, a, superior):
    """
    Verifica computacionalmente que

        inferior <= a_n <= superior.
    """

    inferior = np.asarray(inferior)
    a = np.asarray(a)
    superior = np.asarray(superior)

    sandwich = np.all((inferior <= a) & (a <= superior))

    return {
        "sandwich": sandwich,
        "ultimo_inferior": inferior[-1],
        "ultimo_a": a[-1],
        "ultimo_superior": superior[-1]
    }


RAIZ = Path(__file__).resolve().parent.parent
GRAFICAS = RAIZ / "graficas"


# Medimos el error
def errores(terminos, limite):
    """Error absoluto |a_n - L| respecto al límite propuesto."""
    return np.abs(np.asarray(terminos) - limite)


if __name__ == "__main__":
    N = 30
    n = np.arange(1, N + 1)

    a = sucesion_03(N)
    b = -1 / n
    c = 1 / n

    print("Términos:", a[:4], "...", a[-1])

    # Teorema del Sándwich
    r = verificar_sandwich(b, a, c)

    print("\n--- Teorema del Sándwich ---")
    print("¿Se cumple -1/n <= a_n <= 1/n?", r["sandwich"])
    print(f"Último inferior: {r['ultimo_inferior']:.3e}")
    print(f"Último a_n:      {r['ultimo_a']:.3e}")
    print(f"Último superior: {r['ultimo_superior']:.3e}")

    # Error respecto a L = 0
    e = errores(a, 0)
    razon = e[1:] / e[:-1]

    print("\n--- Velocidad de convergencia ---")
    print(f"Error en n=1:   {e[0]:.3e}")
    print(f"Error en n={N}: {e[-1]:.3e}")
    print("Razón e_{n+1}/e_n:", razon[:5])

    # Gráfica
    plt.plot(n, c, '--', label='1/n')
    plt.plot(n, a, 'o-', ms=4, label='a_n')
    plt.plot(n, b, '--', label='-1/n')
    plt.axhline(0, color='k', lw=1)

    plt.xlabel('n')
    plt.ylabel('valor')
    plt.title('Teorema del Sándwich')
    plt.legend()
    plt.grid(True)

    plt.savefig(GRAFICAS / "ej03.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("\nFigura guardada en graficas/ej03.png")
