import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def criar_sistema_fuzzy():
    # Entradas
    colesterol = ctrl.Antecedent(np.arange(100, 301, 1), 'colesterol')
    pressao = ctrl.Antecedent(np.arange(90, 181, 1), 'pressao')
    idade = ctrl.Antecedent(np.arange(20, 101, 1), 'idade')

    # Saída
    risco = ctrl.Consequent(np.arange(0, 101, 1), 'risco')

    # Membership functions
    colesterol['baixo'] = fuzz.trimf(colesterol.universe, [100, 150, 180])
    colesterol['medio'] = fuzz.trimf(colesterol.universe, [160, 200, 240])
    colesterol['alto'] = fuzz.trimf(colesterol.universe, [220, 260, 300])

    pressao['baixa'] = fuzz.trimf(pressao.universe, [90, 110, 120])
    pressao['media'] = fuzz.trimf(pressao.universe, [115, 130, 145])
    pressao['alta'] = fuzz.trimf(pressao.universe, [140, 160, 180])

    idade['jovem'] = fuzz.trimf(idade.universe, [20, 30, 40])
    idade['adulto'] = fuzz.trimf(idade.universe, [35, 50, 65])
    idade['idoso'] = fuzz.trimf(idade.universe, [60, 75, 100])

    risco['baixo'] = fuzz.trimf(risco.universe, [0, 10, 30])
    risco['medio'] = fuzz.trimf(risco.universe, [20, 50, 70])
    risco['alto'] = fuzz.trimf(risco.universe, [60, 80, 100])

    # Regras Fuzzy
    regras = [
        ctrl.Rule(colesterol['alto'] & pressao['alta'], risco['alto']),
        ctrl.Rule(colesterol['medio'] & pressao['media'], risco['medio']),
        ctrl.Rule(colesterol['baixo'] & pressao['baixa'], risco['baixo']),
        ctrl.Rule(idade['idoso'] & colesterol['alto'], risco['alto']),
        ctrl.Rule(idade['adulto'] & pressao['alta'], risco['medio']),
        ctrl.Rule(colesterol['alto'] & pressao['media'], risco['medio']),
        ctrl.Rule(idade['jovem'] & colesterol['baixo'], risco['baixo']),
    ]


    sistema_ctrl = ctrl.ControlSystem(regras)
    sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

    return sistema

def calcular_risco_fuzzy(idade_val, colesterol_val, pressao_val):
    sistema = criar_sistema_fuzzy()

    sistema.input['idade'] = idade_val
    sistema.input['colesterol'] = colesterol_val
    sistema.input['pressao'] = pressao_val

    sistema.compute()

    return sistema.output['risco']
