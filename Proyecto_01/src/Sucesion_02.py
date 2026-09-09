import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

"""
EJERCICIO 2

Verificar si la sucesión {1/2^n}, que va de n=1 hasta infinito, converge o diverge.

A diferencia del ejercicio 1, aquí los términos se acercan entre sí: cada uno es la
mitad del anterior. La suposición es que converge a 0.

Usaremos el Teorema del Sándwich
"""

# Función para generar la sucesión
def sucesion_02(N):
    """Sucesión {1/2^n} = 1/2, 1/4, 1/8, ..., N"""
    terminos = []
    
    for i in range(N):
        terminos.append(1/(2**(i+1)))
    
    return np.array(terminos)

# Función para verificar que se cumpla el Teorema del Sándwich
def verifica_sandwich(inferior, terminos, superior):
    """
    Verifica las hipótesis del Teorema del Sándwich.

    Comprobar que b_n <= a_n <= c_n en los términos calculados, y
    reporta hacia dónde tienden las cotas.

    Si ambas cotas tienden al mismo valor L y el sandwich se cumple,
    el teorema garantiza que a_n -> L.
    """
    sandwich = np.all((inferior <= terminos) & (terminos <= superior)) #np.all() verifica la condición para lo índices evaluados
    
    return {
        'emparedado': sandwich,
        'ultimo_inferior': inferior[-1],
        'ultimo_a': terminos[-1],
        'ultimo_superior': superior[-1],
    }

RAIZ = Path(__file__).resolve().parent.parent
GRAFICAS = RAIZ / "graficas"

# Función para medir el grado de error
def errores(terminos, limite):
    """Error absoluto |a_n - L| respecto al límite propuesto."""
    return np.abs(np.asarray(terminos) - limite)

# Ejecutamos el código y graficamos
if __name__ == "__main__":
    N = 30
    n = np.arange(1, N + 1)

    a = sucesion_02(N)      # a_n = 2^{-n}
    b = np.zeros(N)         # cota inferior: 0
    c = 1 / n               # cota superior: 1/n

    print("Términos:", a[:4], "...", a[-1])

    # Teorema del Sándwich
    r = verifica_sandwich(b, a, c)
    print("\n--- Teorema del Sándwich ---")
    print("¿Se cumple 0 < a_n < 1/n?", r['emparedado'])
    print(f"Último inferior: {r['ultimo_inferior']}")
    print(f"Último a_n:      {r['ultimo_a']:.3e}") # .3e notación científica de 3 decimales
    print(f"Último superior: {r['ultimo_superior']:.3e}")

    # Error respecto al límite L = 0
    e = errores(a, 0)
    razon = e[1:] / e[:-1]

    print("\n--- Velocidad de convergencia ---")
    print(f"Error en n=1:  {e[0]:.3e}")
    print(f"Error en n={N}: {e[-1]:.3e}")
    print("Razón e_{n+1}/e_n:", razon[:5])
    print(f"¿Razón constante = 1/2? {np.allclose(razon, 0.5)}")

    # ─────────────────────────────────────────────
    # Gráfica
    # ─────────────────────────────────────────────
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

    # Panel izquierdo: el emparedado
    ax1.plot(n, c, 's--', ms=4, color='crimson', label=r'$c_n = 1/n$')
    ax1.plot(n, a, 'o-',  ms=4, color='navy',    label=r'$a_n = 2^{-n}$')
    ax1.plot(n, b, '-',   lw=1, color='k',       label=r'$b_n = 0$')
    ax1.fill_between(n, b, c, color='crimson', alpha=0.10)
    ax1.set_xlabel('$n$'); ax1.set_ylabel('valor')
    ax1.set_title('Teorema del Sándwich: $0 < 2^{-n} < 1/n$')
    ax1.legend(fontsize=8); ax1.grid(True)

    # Panel derecho: error en escala logarítmica
    ax2.semilogy(n, e, 'o-', ms=4, color='seagreen', label=r'$|a_n - 0| = 2^{-n}$')
    ax2.set_xlabel('$n$'); ax2.set_ylabel('error (escala log)')
    ax2.set_title('Decaimiento geométrico: recta en escala log')
    ax2.legend(fontsize=8); ax2.grid(True, which='both')

    plt.tight_layout()
    plt.savefig(GRAFICAS / "ej02.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("\nFigura guardada en graficas/ej02.png")