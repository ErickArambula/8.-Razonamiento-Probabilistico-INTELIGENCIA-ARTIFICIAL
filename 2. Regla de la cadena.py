# Probabilidad P(A)
probabilidad_A = 0.4

# Probabilidad P(B|A)
probabilidad_B_dado_A = 0.3

# Probabilidad P(C|A, B)
probabilidad_C_dado_A_B = 0.2

# Calculamos P(A, B, C) utilizando la Regla de la Cadena
probabilidad_A_B_C = probabilidad_A * probabilidad_B_dado_A * probabilidad_C_dado_A_B

print("Probabilidad conjunta P(A, B, C) =", probabilidad_A_B_C)
