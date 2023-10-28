# Matriz de transición de la cadena de Markov
matriz_transicion = {
    'soleado': {'soleado': 0.7, 'nublado': 0.2, 'lluvioso': 0.1},
    'nublado': {'soleado': 0.3, 'nublado': 0.4, 'lluvioso': 0.3},
    'lluvioso': {'soleado': 0.2, 'nublado': 0.3, 'lluvioso': 0.5}
}

# Estado presente
estado_presente = 'soleado'

# Estado futuro
estado_futuro = 'nublado'

# Probabilidad de cambiar al estado futuro desde el estado presente
probabilidad_cambio = matriz_transicion[estado_presente][estado_futuro]

print(f"Probabilidad de cambiar de {estado_presente} a {estado_futuro}:", probabilidad_cambio)
