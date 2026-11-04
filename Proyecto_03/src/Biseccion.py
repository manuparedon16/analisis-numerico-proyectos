from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

"""
El método de bisección parte de un intervalo [a,b] donde la función
es continua y existe un cambio de signo:

f(a) * f(b) < 0

Por el Teorema de Bolzano sabemos que existe al menos una raíz
dentro del intervalo.

La idea consiste en calcular repetidamente el punto medio:

xr = (a + b) / 2

y conservar el subintervalo donde continúa existiendo el cambio
de signo.

El proceso termina cuando el intervalo es menor que la tolerancia.
"""

# Funciones de la tarea
def f(x):
    return np.sin(x) - x


def g(x):
    return np.exp(-x) - x**2


def h(x):
    return x**5 - 3*x**2 + x - 4


# Método de bisección
def biseccion(funcion, a, b, tolerancia=1e-8):

    # Verificamos la condición de Bolzano
    if funcion(a) * funcion(b) >= 0:
        raise ValueError("El intervalo no presenta cambio de signo.")

    iteraciones = []
    errores = []

    while abs(a - b) >= tolerancia:
        # Punto medio
        xr = (a + b) / 2

        # Guardamos la aproximación
        iteraciones.append(xr)

        # Cota del error
        errores.append(abs(b - a) / 2)

        fxr = funcion(xr)

        # Si la máquina encuentra la raíz
        if fxr == 0:
            error_final = abs(b - a) / 2
            return xr, np.array(iteraciones), np.array(errores), error_final

        # Revisamos en qué intervalo se encuentra la raíz
        elif funcion(a) * fxr < 0:
            b = xr

        else:
            a = xr

    raiz = (a + b) / 2
    error_final = abs(b - a) / 2

    return raiz, np.array(iteraciones), np.array(errores), error_final


# Gráfica de la función y las aproximaciones
def graficar_biseccion(funcion, a, b, raiz, puntos, titulo, ruta):

    x = np.linspace(a, b, 500)

    plt.figure(figsize=(9, 5))

    plt.plot(x, funcion(x), label=titulo)
    plt.axhline(0)

    plt.scatter(
        puntos,
        funcion(puntos),
        s=25,
        label="Aproximaciones"
    )

    plt.scatter(
        raiz,
        funcion(raiz),
        s=60,
        label=f"Raíz ≈ {raiz:.8f}"
    )

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de bisección")
    plt.grid(alpha=0.3)
    plt.legend()

    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    plt.close()


# Gráfica del error
def graficar_error(errores, titulo, ruta):

    n = np.arange(1, len(errores) + 1)

    plt.figure(figsize=(9, 5))

    plt.semilogy(n, errores, marker="o")

    plt.xlabel("Iteración")
    plt.ylabel("Cota del error")
    plt.title(f"Convergencia - {titulo}")
    plt.grid(alpha=0.3)

    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    plt.close()


def main():
    tolerancia = 1e-8

    # Carpeta para las gráficas
    carpeta_proyecto = Path(__file__).resolve().parent.parent
    carpeta_graficas = carpeta_proyecto / "graficas"
    carpeta_graficas.mkdir(exist_ok=True)

    problemas = [
        ("f(x) = sen(x) - x", f, -1, 0.5, "funcion_1"),
        ("g(x) = e^(-x) - x^2", g, 0, 1, "funcion_2"),
        ("h(x) = x^5 - 3x^2 + x - 4", h, 1, 2, "funcion_3")
    ]

    for titulo, funcion, a, b, nombre in problemas:

        raiz, puntos, errores, error_final = biseccion(
            funcion,
            a,
            b,
            tolerancia
        )

        print("\n", titulo)
        print("Raíz aproximada:", raiz)
        print("Iteraciones:", len(puntos))
        print("Error:", error_final)    

        graficar_biseccion(
            funcion,
            a,
            b,
            raiz,
            puntos,
            titulo,
            carpeta_graficas / f"{nombre}_biseccion.png"
        )

        graficar_error(
            errores,
            titulo,
            carpeta_graficas / f"{nombre}_error.png"
        )


if __name__ == "__main__":
    main()