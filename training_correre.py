
EPOCHS = 100
LEARNING_RATE = 0.1
THRESHOLD = 0.5


def activation(x):
    if x > THRESHOLD:
        return 1
    else:
        return 0


def main():

    inputs = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1],
    ]


    expected = []
    for row in inputs:
        sole, tempo, stanco = row
        if (tempo or sole) and not stanco:
            expected.append(1)
        else:
            expected.append(0)


    print("Dataset di addestramento:")
    print("  Sole  Tempo  Stanco  =>  Correre")
    for i in range(len(inputs)):
        s, t, st = inputs[i]
        print(f"   {s}      {t}       {st}   =>     {expected[i]}")

    # Pesi e bias partono da zero
    weights = [0.0, 0.0, 0.0]
    bias = 0.0

    print(f"\nTraining: max {EPOCHS} epoche, lr={LEARNING_RATE}\n")

    # Addestramento
    for epoch in range(EPOCHS):
        errori = 0

        for i in range(len(inputs)):
            somma = bias
            for j in range(3):
                somma += weights[j] * inputs[i][j]

            output = activation(somma)
            error = expected[i] - output

            if error != 0:
                errori += 1
                for j in range(3):
                    weights[j] += LEARNING_RATE * error * inputs[i][j]
                bias += LEARNING_RATE * error

        if errori == 0:
            print(f"Convergenza raggiunta all'epoca {epoch + 1}!\n")
            break

    # Pesi finali
    print("Pesi allenati:")
    print(f"  Peso 0 (sole)  : {weights[0]:.6f}")
    print(f"  Peso 1 (tempo) : {weights[1]:.6f}")
    print(f"  Peso 2 (stanco): {weights[2]:.6f}")
    print(f"  Bias           : {bias:.6f}")

    # Test finale
    print("\nTest del percettrone:")
    tutti_ok = True
    for i in range(len(inputs)):
        somma = bias
        for j in range(3):
            somma += weights[j] * inputs[i][j]
        output = activation(somma)
        ok = (output == expected[i])
        if not ok:
            tutti_ok = False
        stato = "OK" if ok else "ERRORE"
        print(f"  Input {inputs[i]} => Correre: {output} (Atteso: {expected[i]})  {stato}")

    if tutti_ok:
        print("\nTutti gli esempi classificati correttamente!")
    else:
        print("\nAttenzione: alcuni esempi non classificati correttamente.")


if __name__ == "__main__":
    main()
