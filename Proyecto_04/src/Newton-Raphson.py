from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

"""
Se implementa el método de Newton-Raphson:

x_(n+1) = x_n - f(x_n) / f'(x_n)

para aproximar las raíces de las tres funciones de la tarea.

Además, se observa la convergencia mediante la diferencia
entre aproximaciones consecutivas y se compara el número
de iteraciones con el método de Bisección.
"""


# FUNCIONES DE LA TAREA
def f(x):
    return np.sin(x) - x


def df(x):
    return np.cos(x) - 1


def g(x):
    return np.exp(-x) - x**2


def dg(x):
    return -np.exp(-x) - 2*x


def h(x):
    return x**5 - 3*x**2 + x - 4


def dh(x):
    return 5*x**4 - 6*x + 1


# MÉTODO DE NEWTON-RAPHSON
def newton_raphson(funcion, derivada, x0, tolerancia=1e-8):

    aproximaciones = [x0]
    errores = []

    xn = x0

    for i in range(100):

        fxn = funcion(xn)
        dfxn = derivada(xn)

        # Si la computadora ya identifica una raíz
        if fxn == 0:
            break

        # Newton no puede continuar si la derivada es cero
        if dfxn == 0:
            raise ValueError("La derivada es cero.")

        # Fórmula de Newton-Raphson
        xn_nuevo = xn - fxn / dfxn

        # Diferencia entre aproximaciones
        error = abs(xn_nuevo - xn)

        aproximaciones.append(xn_nuevo)
        errores.append(error)

        xn = xn_nuevo

        # Criterio de paro
        if error < tolerancia:
            break

    return xn, np.array(aproximaciones), np.array(errores)


# ORDEN DE CONVERGENCIA
def orden_convergencia(errores):
    """
    Estima el orden p a partir de tres errores consecutivos:

    p = log(e_(n+1)/e_n) / log(e_n/e_(n-1))

    p cerca de 2 indica convergencia cuadrática
    p cerca de 1 indica convergencia lineal
    """
    if len(errores) < 3:
        return None

    return np.log(errores[-1] / errores[-2]) / np.log(errores[-2] / errores[-3])


# BISECCIÓN
# Solo para comparar con el Proyecto 03
def biseccion(funcion, a, b, tolerancia=1e-8):

    iteraciones = 0

    while abs(b - a) >= tolerancia:

        xr = (a + b) / 2
        fxr = funcion(xr)

        iteraciones += 1

        if fxr == 0:
            return xr, iteraciones, abs(b - a) / 2

        if funcion(a) * fxr < 0:
            b = xr
        else:
            a = xr

    raiz = (a + b) / 2
    error = abs(b - a) / 2

    return raiz, iteraciones, error


# GRÁFICA DE CONVERGENCIA
def graficar_error(errores, titulo, ruta):

    n = np.arange(1, len(errores) + 1)

    plt.figure(figsize=(9, 5))

    plt.semilogy(
        n,
        errores,
        marker="o"
    )

    plt.xlabel("Iteración")
    plt.ylabel(r"$|x_{n+1}-x_n|$")
    plt.title(f"Convergencia - {titulo}")

    plt.grid(alpha=0.3)

    plt.savefig(
        ruta,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# MAIN
def main():

    tolerancia = 1e-8

    # Aproximación inicial usada en el ejemplo del profesor
    x0 = 2

    # Carpeta de gráficas
    carpeta_proyecto = Path(__file__).resolve().parent.parent
    carpeta_graficas = carpeta_proyecto / "graficas"
    carpeta_graficas.mkdir(exist_ok=True)

    problemas = [
        ("f(x) = sen(x) - x", f, df, -1, 0.5, "funcion_1"),
        ("g(x) = e^(-x) - x^2", g, dg, 0, 1, "funcion_2"),
        ("h(x) = x^5 - 3x^2 + x - 4", h, dh, 1, 2, "funcion_3")
    ]

    for titulo, funcion, derivada, a, b, nombre in problemas:

        # Newton-Raphson
        raiz, aproximaciones, errores = newton_raphson(
            funcion,
            derivada,
            x0,
            tolerancia
        )

        # Bisección
        raiz_bis, iter_bis, error_bis = biseccion(
            funcion,
            a,
            b,
            tolerancia
        )

        print("\n", titulo)

        print("Newton-Raphson")
        print("Raíz aproximada:", raiz)
        print("Iteraciones:", len(errores))

        if len(errores) > 0:
            print("Última diferencia:", errores[-1])

        p = orden_convergencia(errores)

        if p is not None:
            print("Orden estimado de convergencia:", round(p, 2))

        print("Bisección")
        print("Raíz aproximada:", raiz_bis)
        print("Iteraciones:", iter_bis)
        print("Cota del error:", error_bis)

        # Gráfica de convergencia de Newton
        graficar_error(
            errores,
            titulo,
            carpeta_graficas / f"{nombre}_newton.png"
        )


if __name__ == "__main__":
    main()