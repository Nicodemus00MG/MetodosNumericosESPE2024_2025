import math

def coeficiente_newton(n):
  """
  Calcula el coeficiente de Newton para la serie que aproxima la raíz cuadrada de 17.

  Args:
    n: El índice del término en la serie (empezando desde 1).

  Returns:
    El valor del coeficiente de Newton.
  """
  if n == 0:
    return 1  # Caso base para n = 0
  else:
    producto = 1
    for i in range(1, n):
      producto *= -(2*i - 1) / 2
    return (1/2) * producto / (math.factorial(n) * 16**n)

def raiz17Aprox(N):
    """
    Aproxima el valor de la raíz cuadrada de 17 usando la serie dada.

    Args:
      N: Número de términos en la serie.

    Returns:
      El valor aproximado de la raíz cuadrada de 17.
    """
    raiz17 = 4.0  # Inicializar como float
    for n in range(1, N + 1):
        raiz17 += 4 * coeficiente_newton(n)
    return raiz17

def N_raiz17(precision):
    """
    Estima el número de términos necesarios para aproximar la raíz cuadrada de 17
    con una precisión dada.

    Args:
      precision: Precisión deseada.

    Returns:
      El valor estimado de N.
    """
    N = 0
    raiz17_aprox = 0
    while abs(raiz17_aprox - math.sqrt(17)) > precision:
        N += 1
        raiz17_aprox = raiz17Aprox(N)
    return N