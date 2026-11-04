from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

"""
Proyecto 05 - Integración Numérica
Análisis Numérico 2027-1

Se implementan los métodos:
- Regla compuesta del Trapecio
- Regla compuesta de Simpson

También se analiza la rapidez de convergencia
y se estima el error mediante refinamiento.
"""


# Funciones de la tarea
def f(x):
    return np.exp(-x**2)

def g(x):
    return np.sin(x**2)

def h(x):
    return np.sqrt(np.maximum(0, 25 - (25 / 9) * x**2))


# Regla compuesta del Trapecio
def trapecio(funcion, a, b, n):
    c = (b - a) / n
    integral = 0

    for i in range(n):
        xi = a + i*c
        xi_1 = a + (i + 1)*c
        area = c * (funcion(xi) + funcion(xi_1)) / 2
        integral += area

    return integral


# Regla compuesta de Simpson
def simpson(funcion, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson requiere un número par de subintervalos.")

    c = (b - a) / n
    integral = 0

    for i in range(0, n, 2):
        xi = a + i*c
        xi_1 = a + (i + 1)*c
        xi_2 = a + (i + 2)*c

        area = (c / 3) * (
            funcion(xi)
            + 4*funcion(xi_1)
            + funcion(xi_2)
        )

        integral += area

    return integral


# Orden de convergencia y estimación del error
def analizar_metodo(funcion, a, b, n, metodo):
    I_medio = metodo(funcion, a, b, n // 2)
    I_n = metodo(funcion, a, b, n)
    I_2n = metodo(funcion, a, b, 2*n)

    diferencia_1 = abs(I_n - I_medio)
    diferencia_2 = abs(I_2n - I_n)

    limite_maquina = 10 * np.finfo(float).eps * max(1, abs(I_2n))

    if diferencia_1 <= limite_maquina or diferencia_2 <= limite_maquina:
        orden = np.nan
        error_estimado = np.nan
    else:
        orden = np.log2(diferencia_1 / diferencia_2)

        if orden > 0:
            error_estimado = diferencia_2 / (2**orden - 1)
        else:
            error_estimado = np.nan

    return I_n, I_2n, diferencia_2, orden, error_estimado


# Gráfica de convergencia
def graficar_convergencia(funcion, a, b, titulo, ruta):
    subdivisiones = np.array([100, 200, 400, 800, 1600])

    aproximaciones_trapecio = []
    aproximaciones_simpson = []

    for n in subdivisiones:
        aproximaciones_trapecio.append(
            trapecio(funcion, a, b, n)
        )

        aproximaciones_simpson.append(
            simpson(funcion, a, b, n)
        )

    errores_trapecio = np.abs(np.diff(aproximaciones_trapecio))
    errores_simpson = np.abs(np.diff(aproximaciones_simpson))

    plt.figure(figsize=(9, 5))

    plt.loglog(
        subdivisiones[1:],
        errores_trapecio,
        marker="o",
        label="Trapecio"
    )

    plt.loglog(
        subdivisiones[1:],
        errores_simpson,
        marker="o",
        label="Simpson"
    )

    plt.xlabel("Número de subintervalos")
    plt.ylabel("Diferencia entre aproximaciones")
    plt.title(f"Convergencia - {titulo}")

    plt.grid(alpha=0.3)
    plt.legend()

    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    plt.close()


def main():
    n = 1000

    carpeta_proyecto = Path(__file__).resolve().parent.parent
    carpeta_graficas = carpeta_proyecto / "graficas"
    carpeta_graficas.mkdir(exist_ok=True)

    problemas = [
        ("Integral 1", f, -100, 100, "integral_1"),
        ("Integral 2", g, 0, np.pi / 4, "integral_2"),
        ("Integral 3", h, 0, 3, "integral_3")
    ]

    for titulo, funcion, a, b, nombre in problemas:
        Tn, T2n, diferencia_T, orden_T, error_T = analizar_metodo(
            funcion, a, b, n, trapecio
        )

        Sn, S2n, diferencia_S, orden_S, error_S = analizar_metodo(
            funcion, a, b, n, simpson
        )

        print("\n", titulo)

        print("Trapecio")
        print("Aproximación:", Tn)
        print("Aproximación refinada:", T2n)
        print("Diferencia al refinar:", diferencia_T)

        if np.isnan(orden_T):
            print("Orden observado: no estimable por precisión de máquina")
            print("Error estimado: no confiable por redondeo")
        else:
            print("Orden observado:", orden_T)
            print("Error estimado:", error_T)

        print("Simpson")
        print("Aproximación:", Sn)
        print("Aproximación refinada:", S2n)
        print("Diferencia al refinar:", diferencia_S)

        if np.isnan(orden_S):
            print("Orden observado: no estimable por precisión de máquina")
            print("Error estimado: no confiable por redondeo")
        else:
            print("Orden observado:", orden_S)
            print("Error estimado:", error_S)

        graficar_convergencia(
            funcion,
            a,
            b,
            titulo,
            carpeta_graficas / f"{nombre}_convergencia.png"
        )


if __name__ == "__main__":
    main()