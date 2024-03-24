# A CHAMA SOMENTE PODERÁ SE ACIONADA SE O NÍVEL DE ÁGUA FOR
# SUPERIOR AO NÍVEL (N2) E INFERIOR AO NÍVEL (N3)

# SE O NÍVEL DE ÁGUA ESTIVER INFERIOR AO NÍVEL (N2), ABRIR A
# VÁLVULA DE ENTRADA DE ÁGUA

# A VÁLVULA DE ENTRADA DE GÁS SOMENTE PODERÁ SER ABERTA SE O
# DISPOSITIVO DE IGNIÇÃO DA CHAMA ESTIVER ATIVADO

# SE O SENSOR DE TEMPERATURA MÁXIMA (TMAX) FOR ATIVADO, A CHAMA
# DEVERÁ SER DESLIGADA DESATIVANDO A VÁLVULA DE ENTRADA DE GÁS

# SE O SENSOR DE PRESSÃO MÁXIMA (PMAX) FOR ATIVADO, A CHAMA
# DEVERÁ SER DESLIGADA DESATIVANDO A VÁLVULA DE ENTRADA DE GÁS

# A VÁLVULA DE CONTROLE DE SAÍDA DE VAPOR SOMENTE PODERÁ SER
# ABERTA SE O SENSOR DE PRESSÃO OPERACIONAL E O SENSOR DE TEMPERATURA FOREM ATIVADOS

# EM CASO DE EMERGÊNCIA OPERACIONAL, DESLIGAR A ENTRADA DE
# GÁS

# import matplotlib.pyplot as plt
# import numpy as np
# import random
# import pandas as pd
# import time as tm
# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split

from sklearn.neural_network import MLPClassifier

# ENTRADAS
#   ON/OFF  N1  N2  N3  TEMPERATURAMAX  PRESSAOMAX   PRESSAOOPERACIONAL  TEMPERATURAOPERACIONAL
entrypoints = [
    [1., 0., 0., 0., 0., 0., 0., 0.],  # ON - Nenhum sensor ativado
    [1., 1., 0., 0., 0., 0., 0., 0.],  # ON - N1 ativado
    [1., 1., 1., 0., 0., 0., 0., 0.],  # ON - N1, N2 ativados
    [1., 1., 1., 1., 0., 0., 0., 0.],  # ON - N1, N2, N3 ativados
    [1., 1., 1., 0., 1., 0., 0., 0.],  # ON - N1, N2, TMAX ativados
    [1., 1., 1., 0., 0., 1., 0., 0.],  # ON - N1, N2, PMAX ativados
    [1., 1., 1., 0., 0., 1., 0., 0.],  # ON - N1, N2, TMAX e PMAX ativados
    [1., 1., 1., 0., 0., 0., 1., 1.],  # ON - N1, N2, POper, TOper ativados
    [0., 0., 0., 0., 0., 0., 0., 0.],  # OFF - Nenhum sensor ativado
    [0., 1., 0., 0., 0., 0., 0., 0.],  # OFF - N1 ativado
    [0., 1., 1., 0., 0., 0., 0., 0.],  # OFF - N1, N2 ativados
    [0., 1., 1., 1., 0., 0., 0., 0.],  # OFF - N1, N2, N3 ativados
    [0., 1., 1., 0., 1., 0., 0., 0.],  # OFF - N1, N2, TMAX ativados
    [0., 1., 1., 0., 0., 1., 0., 0.],  # OFF - N1, N2, PMAX ativados
    [0., 1., 1., 0., 0., 1., 0., 0.],  # OFF - N1, N2, TMAX e PMAX ativados
    [0., 1., 1., 0., 0., 0., 1., 1.],  # OFF - N1, N2, POper, TOper ativados
]

# SAÍDAS
#   VALVULACHAMA  ENTRADAAGUA  VALVULAGAS  SAIDAVAPOR  SAIDAAGUA
expectedReturns = [
    [0., 1., 0., 0., 0.],  # Válvula de entrada de água aberta
    [0., 1., 0., 0., 1.],  # Válvula de entrada de água aberta
    [1., 0., 1., 0., 0.],  # Válvula de chama e válvula de gás abertas
    [0., 0., 0., 0., 1.],  # Saída de água aberta
    [0., 0., 0., 0., 0.],  # Desligado devido ao TMAX ativado
    [0., 0., 0., 0., 0.],  # Desligado devido ao PMAX ativado
    [0., 0., 0., 0., 0.],  # Desligado devido ao TMAX e PMAX ativados
    [1., 0., 1., 1., 0.],  # Válvula de chama, válvula de gás e saída de vapor abertas
    [0., 0., 0., 1., 1.],  # Saída de água e de vapor abertas
    [0., 0., 0., 1., 1.],  # Saída de água e de vapor abertas
    [0., 0., 0., 1., 1.],  # Saída de água e de vapor abertas
    [0., 0., 0., 1., 1.],  # Saída de água e de vapor abertas
    [0., 0., 0., 1., 1.],  # Saída de água e de vapor abertas
    [0., 0., 0., 1., 1.],  # Saída de água e de vapor abertas
    [0., 0., 0., 1., 1.],  # Saída de água e de vapor abertas
    [0., 0., 0., 1., 1.],  # Saída de água e de vapor abertas
]

# CRIANDO A ESTRUTURA DA REDE
caldeira = MLPClassifier(
    solver="lbfgs",
    activation="logistic",
    alpha=1e-8,
    hidden_layer_sizes=(100, 100),
    random_state=1,
)

# TREINAMENTO
caldeira.fit(entrypoints, expectedReturns)

while True:
    ON = int(input("Acionar botão ON? [0 - Não, 1 - Sim]: "))
    N1 = int(input("Digite o nível de água N1 (0 - desligado, 1 - ligado): "))
    N2 = int(input("Digite o nível de água N2 (0 - desligado, 1 - ligado): "))
    N3 = int(input("Digite o nível de água N3 (0 - desligado, 1 - ligado): "))
    TMAX = int(input("Sensor de temperatura máxima ativado? [0 - Não, 1 - Sim]: "))
    PMAX = int(input("Sensor de pressão máxima ativado? [0 - Não, 1 - Sim]: "))
    PressaoOperacional = int(
        input("Sensor de pressão operacional ativado? [0 - Não, 1 - Sim]: ")
    )
    TOperacional = int(
        input("Sensor de temperatura operacional ativado? [0 - Não, 1 - Sim]: ")
    )

    # Realizar a previsão com base nas entradas
    predicted_output = caldeira.predict(
        [[ON, N1, N2, N3, TMAX, PMAX, PressaoOperacional, TOperacional]]
    )

    # Imprimir saídas previstas
    print(
        "Saídas previstas (VálvulaChama, EntradaAgua, VálvulaGás, SaídaVapor, SaídaÁgua):",
        predicted_output,
    )

    # Verificar se o usuário deseja continuar
    continuar = input("Deseja continuar? [s/n]: ")
    if continuar.lower() != "s":
        break
