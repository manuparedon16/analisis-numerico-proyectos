import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


"""
EJERCICIO 1

Verificar si la sucesión 5n, que va de n=1 hasta infinito, converge o diverge.

Como los saltos de la sucesión siempre son de 5 en 5, la suposición es que diverge.
Para probarlo se usa la negación de la definición de convergencia:

NEGACIÓN DE LA DEFINICIÓN DE CONVERGENCIA

Definición original (a_n -> L):
    Para todo epsilon > 0, existe n_0 tal que para todo n >= n_0, |a_n - L| < epsilon.

Negación (a_n NO converge a L):
    Existe epsilon > 0 tal que para todo n_0, existe n >= n_0 con |a_n - L| >= epsilon.

La sucesión diverge si lo anterior se cumple para todo L en los reales.

Estrategia: como |a_{n+1} - a_n| = 5 para todo n, dos términos consecutivos no caben
ambos en un intervalo de ancho 5 centrado en L. Tomando epsilon = 5/2, al menos uno
de los índices n_0 o n_0 + 1 sirve como testigo.
"""


# Función para generar la sucesión
def sucesion_01(N):
    """Sucesión a_n = 5n para n = 1, ..., N"""
    terminos = []                      # lista vacía

    for i in range(N):                 # i = 0, 1, ..., N-1
        terminos.append(5 * (i + 1))   # i+1 corre de 1 a N

    return np.array(terminos)


# Función para calcular las diferencias consecutivas
def diferencias_consecutivas(terminos):
    """
    Calcula |a_{n+1} - a_n| para una sucesión

    Si la sucesión converge, estas diferencias deben tender a 0 (condición
    necesaria del criterio de Cauchy). Si no tienden a 0, la sucesión diverge
    """
    return np.abs(np.diff(terminos))


# Función para comprobar la divergencia usando la negación de la definición
def testigo_divergencia(terminos, L, n0, epsilon):
    """
    Busca n >= n0 tal que |a_n - L| >= epsilon

    Exhibe el término que se sale del intervalo (L - epsilon, L + epsilon)
    Retorna (n, distancia) o None si ninguno de los dos índices cumple
    """
    terminos = np.asarray(terminos)

    if n0 <= len(terminos):
        d = abs(terminos[n0 - 1] - L)   # a_n vive en terminos[n-1]
        if d >= epsilon:
            return n0, d

    if n0 + 1 <= len(terminos):
        d = abs(terminos[n0] - L)
        if d >= epsilon:
            return n0 + 1, d

    return None

RAIZ = Path(__file__).resolve().parent.parent
GRAFICAS = RAIZ / "graficas"

# Ejecutamos el código y graficamos
if __name__ == "__main__":
    N = 30
    a = sucesion_01(N)
    n = np.arange(1, N + 1)
    d = diferencias_consecutivas(a)
    
    print("Términos:", a[:5], "...", a[-1])
    print("Diferencias:", d[:5])
    print("¿Todas iguales a 5?", np.all(d == 5))

    for L_prueba in [0, 100, 1000]:
        print(f"L={L_prueba}:", testigo_divergencia(a, L_prueba, n0=19, epsilon=2.5))

    # Gráfica
    L, eps, n0 = 100, 2.5, 19

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

    ax1.plot(n, a, 'o-', ms=4, label=r'$a_n = 5n$')
    ax1.axhline(L, color='crimson', ls='--', lw=1, label=f'$L={L}$')
    ax1.axhspan(L - eps, L + eps, color='crimson', alpha=0.15)
    ax1.set_xlabel('$n$'); ax1.set_ylabel('$a_n$')
    ax1.set_title('Términos y banda de radio $\\varepsilon$')
    ax1.legend(fontsize=8); ax1.grid(True)

    ax2.plot(n[:-1], d, 'o-', ms=4, color='seagreen')
    ax2.axhline(0, color='k', ls=':', lw=1, label='requerido si converge')
    ax2.set_ylim(-0.5, 6)
    ax2.set_xlabel('$n$'); ax2.set_ylabel(r'$|a_{n+1} - a_n|$')
    ax2.set_title('Criterio de Cauchy')
    ax2.legend(fontsize=8); ax2.grid(True)

    plt.tight_layout()
    plt.savefig(GRAFICAS / "ej01.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Figura guardada en graficas/ej01.png")