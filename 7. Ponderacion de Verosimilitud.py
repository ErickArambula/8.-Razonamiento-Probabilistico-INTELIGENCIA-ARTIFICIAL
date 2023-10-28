# Datos observados de A y B
datos_observados = [
    {'A': 0, 'B': 0},
    {'A': 1, 'B': 1},
    {'A': 0, 'B': 1},
    {'A': 1, 'B': 1},
    {'A': 1, 'B': 0}
]

# Contadores de ocurrencias
contador_A = 0
contador_AB = 0

for dato in datos_observados:
    if dato['A'] == 1:
        contador_A += 1
        if dato['B'] == 1:
            contador_AB += 1

# Estimación de P(B|A) utilizando ponderación de verosimilitud
probabilidad_B_dado_A = contador_AB / contador_A if contador_A > 0 else 0

print("Probabilidad de B dado A:", probabilidad_B_dado_A)
