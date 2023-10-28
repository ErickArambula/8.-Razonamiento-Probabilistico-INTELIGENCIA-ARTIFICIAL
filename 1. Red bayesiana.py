from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definición de la Red Bayesiana
modelo = BayesianNetwork([('Incendio', 'Alarma'), ('CocinaDesatendida', 'Alarma')])

# Probabilidades condicionales
cpd_incendio = TabularCPD(variable='Incendio', variable_card=2, values=[[0.7, 0.3]])
cpd_cocina = TabularCPD(variable='CocinaDesatendida', variable_card=2, values=[[0.9, 0.1]])

# La probabilidad de que la alarma suene depende de ambos eventos
cpd_alarma = TabularCPD(variable='Alarma', variable_card=2, 
                       values=[[0.95, 0.9, 0.7, 0.01],
                               [0.05, 0.1, 0.3, 0.99]],
                       evidence=['Incendio', 'CocinaDesatendida'], evidence_card=[2, 2])

# Agregar las CPDs al modelo
modelo.add_cpds(cpd_incendio, cpd_cocina, cpd_alarma)

# Verificar si el modelo es válido
modelo.check_model()

# Realizar inferencias
inferencia = VariableElimination(modelo)
probabilidad_alarma = inferencia.query(variables=['Alarma'], evidence={'Incendio': 1, 'CocinaDesatendida': 1})
print(probabilidad_alarma)
