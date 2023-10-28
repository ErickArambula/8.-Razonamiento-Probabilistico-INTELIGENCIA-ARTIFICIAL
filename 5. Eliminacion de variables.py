from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definición de la Red Bayesiana
modelo = BayesianNetwork([('A', 'C'), ('B', 'C'), ('C', 'D')])

# Probabilidades condicionales
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6, 0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7, 0.3]])
cpd_c = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.8, 0.2],
                           [0.2, 0.8]],
                   evidence=['A', 'B'], evidence_card=[2, 2])
cpd_d = TabularCPD(variable='D', variable_card=2, 
                   values=[[0.9, 0.7],
                           [0.1, 0.3]],
                   evidence=['C'], evidence_card=[2])

# Agregar las CPDs al modelo
modelo.add_cpds(cpd_a, cpd_b, cpd_c, cpd_d)

# Realizar eliminación de variables para calcular P(A|C)
inferencia = VariableElimination(modelo)
probabilidad_a_dado_c = inferencia.query(variables=['A'], evidence={'C': 1})

print(probabilidad_a_dado_c)
