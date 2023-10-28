import numpy as np

# Función objetivo (distribución de probabilidad que queremos aproximar)
def funcion_objetivo(x):
    return np.exp(-x**2)  # Distribución Gaussiana

# Algoritmo de Monte Carlo para Cadenas de Markov (Metropolis-Hastings)
def metropolis_hastings(iteraciones):
    muestras = []
    x = 0  # Valor inicial

    for _ in range(iteraciones):
        propuesta = x + np.random.normal(0, 1)  # Generar una propuesta de nuevo valor
        alpha = funcion_objetivo(propuesta) / funcion_objetivo(x)
        if np.random.uniform(0, 1) < alpha:
            x = propuesta  # Aceptar la propuesta
        muestras.append(x)

    return muestras

# Realizar MCMC para aproximar la distribución de probabilidad
iteraciones = 10000
muestras = metropolis_hastings(iteraciones)

# Calcular estadísticas sobre las muestras
media_aproximada = np.mean(muestras)
varianza_aproximada = np.var(muestras)

print("Media aproximada:", media_aproximada)
print("Varianza aproximada:", varianza_aproximada)
