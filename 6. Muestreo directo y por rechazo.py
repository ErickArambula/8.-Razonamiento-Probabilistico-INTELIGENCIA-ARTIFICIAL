import random

# Número de lanzamientos
num_lanzamientos = 10000

# Contador de sumas iguales a 7
sumas_igual_a_7 = 0

for _ in range(num_lanzamientos):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    if suma == 7:
        sumas_igual_a_7 += 1

probabilidad = sumas_igual_a_7 / num_lanzamientos
print("Probabilidad de obtener una suma igual a 7:", probabilidad)



import random

# Función de densidad de probabilidad de X
def pdf_X(x):
    return x if 0 <= x <= 1 else 0

# Función de densidad de probabilidad de Y (aproximada)
def pdf_Y(y):
    return 2 * y if 0 <= y <= 1 else 0

# Número de muestras
num_muestras = 10000

muestras_X = []

for _ in range(num_muestras):
    # Generar una muestra de Y
    y = random.uniform(0, 1)
    
    # Generar una muestra de X
    x = random.uniform(0, 1)
    
    # Calcular la probabilidad de aceptación
    p_aceptacion = pdf_X(x) / pdf_Y(y)
    
    if random.uniform(0, 1) < p_aceptacion:
        muestras_X.append(x)

# Calcular estadísticas sobre las muestras de X
media = sum(muestras_X) / len(muestras_X)
print("Media de X:", media)
