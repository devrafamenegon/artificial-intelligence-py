from sklearn.neural_network import MLPClassifier

# ENTRIES
# N3  N2  N1  ON/OFF
waterLevels = [
    [0., 0., 0., 1.],  # N0 ON
    [0., 0., 1., 1.],  # N1 ON
    [0., 1., 1., 1.],  # N2 ON
    [1., 1., 1., 1.],  # N3 ON
    [0., 0., 0., 0.],  # N0 OFF
    [0., 0., 1., 0.],  # N1 OFF
    [0., 1., 1., 0.],  # N3 OFF
    [1., 1., 1., 0.]   # N3 OFF
]

# EXITS
# EXITVALVE  ENTRYVALVE
waterControls = [
    [0., 1.], # ENTRYVALVE OPEN
    [0., 1.], # ENTRYVALVE OPEN
    [0., 0.], # OPERATIONAL (ALL VALVES CLOSED)
    [1., 0.], # EXITVALVE OPEN
    [1., 0.], # EXITVALVE OPEN
    [1., 0.], # EXITVALVE OPEN
    [1., 0.], # EXITVALVE OPEN
    [1., 0.]  # EXITVALVE OPEN
]

waterValveLabel = ["CLOSED", "OPEN"]

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
jacuzzi.fit(waterLevels, waterControls)

while True:
    on = int(input("It's jacuzzi ON? [0/1]: "))
    n1 = int(input("It's N1 active? [0/1]: "))
    n2 = int(input("It's N2 active? [0/1]: "))
    n3 = int(input("It's N3 active? [0/1]: "))

    auxInput = [n3, n2, n1, on]
    result = jacuzzi.predict([auxInput])

    print("\nNeural network result: ", result)

    WaterExitValve = result[0][0]
    print("\nWater exit valve : ", waterValveLabel[WaterExitValve])

    waterEntryValve = result[0][1]   
    print("Water entry valve: ", waterValveLabel[waterEntryValve])

    # CLOSE OR CONTINUE
    close = int(input("Want to exit? [0/1]: "))
    if close == 1:
        break

    print("\n\n")
