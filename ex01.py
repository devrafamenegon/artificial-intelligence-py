# import matplotlib.pyplot as plt
# import numpy as np
# import random
# import pandas as pd
# import time as tm

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# ENTRADAS
#   T3  T2  T1  ON
X = [
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
]

# SAÍDAS
#   R3  R2  R1  LED
y = [
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
]

#CRIANDO A ESTRUTURA DA REDE
chuveiro = MLPClassifier(
    solver='lbfgs',
    activation='logistic', 
    alpha=1e-8,
    hidden_layer_sizes=(450,450), 
    random_state=1
)

# TREINAMENTO
chuveiro.fit(X, y)

while(True):
    t1 = int(input("Digite o valor do Botão T1: "))
    t2 = int(input("Digite o valor do Botão T2: "))
    t3 = int(input("Digite o valor do Botão T3: "))
    on = int(input("Acionar botão ON? [0 - Nao, 1 - Sim]"))

    print(
        chuveiro.predict(
            [[t1,t2,t3, on]]
        )
    )