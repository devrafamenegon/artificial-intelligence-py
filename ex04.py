from sklearn.neural_network import MLPClassifier

# ENTRIES
# T2  T1  N2  ON/OFF
entries =[
    [0., 0., 0., 1.],
    [0., 1., 0., 1.],
    [1., 0., 0., 1.],
    [1., 1., 0., 1.],
    [0., 0., 1., 1.],
    [0., 1., 1., 1.],
    [1., 1., 1., 1.],
    [0., 0., 0., 0.],
    [0., 1., 0., 0.],
    [1., 0., 0., 0.],
    [1., 1., 0., 0.],
    [0., 0., 1., 0.],
    [0., 1., 1., 0.],
    [1., 1., 1., 0.],
]

# EXITS
# WATERENTRYVALVE  WATERENGINE  WATERHEATER
exits=[
    [0., 0., 0.],
    [0., 0., 0.],
    [0., 0., 0.],
    [0., 0., 0.],
    [1., 1., 1.],
    [1., 1., 1.],
    [0., 1., 1.],
    [0., 0., 0.],
    [0., 0., 0.],
    [0., 0., 0.],
    [0., 0., 0.],
    [0., 0., 0.],
    [0., 0., 0.],
    [0., 0., 0.],
]

exitLabel = ["CLOSED", "OPEN"]

# CREATING NEURAL NETWORK
jacuzzi = MLPClassifier(
    solver="lbfgs",
    activation="logistic",
    alpha=1e-8,
    hidden_layer_sizes=(20, 20),
    random_state=1,
)

# TRAINING
print("Start training...\n")
jacuzzi.fit(entries, exits)

while True:
    on = int(input("It's jacuzzi ON? [0/1]: "))
    t1 = int(input("It's T1 active? [0/1]: "))
    t2 = int(input("It's T2 active? [0/1]: "))
    n2 = int(input("It's N2 active? [0/1]: "))

    auxInput = [t2, t1, n2, on]
    result = jacuzzi.predict([auxInput])

    print("\nNeural network result: ", result)

    waterEntry=result[0][2]
    print("Water entry valve: ", exitLabel[waterEntry])

    engine=result[0][1]   
    print("Water engine:      ", exitLabel[engine])

    heater=result[0][0]   
    print("Water heater:      ", exitLabel[heater]) 

    # CLOSE OR CONTINUE
    close = int(input("Want to exit? [0/1]: "))
    if close == 1:
        break

    print("\n\n")
