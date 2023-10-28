from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definición de la Red Bayesiana
modelo = BayesianNetwork([('A', 'C'), ('B', 'C')])

# Probabilidades condicionales
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.7, 0.3]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.6, 0.4]])
cpd_c = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.9, 0.8, 0.8, 0.1],
                           [0.1, 0.2, 0.2, 0.9]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Agregar las CPDs al modelo
modelo.add_cpds(cpd_a, cpd_b, cpd_c)

# Realizar inferencias por enumeración
inferencia = VariableElimination(modelo)
probabilidad_c_dado_ab = inferencia.query(variables=['C'], evidence={'A': 1, 'B': 0})

print(probabilidad_c_dado_ab)
