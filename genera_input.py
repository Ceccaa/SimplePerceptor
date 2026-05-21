
import random
import os
import sys

FEATURES = 5
THRESHOLD = 1.5
N_CAMPIONI = 500


def carica_pesi(filename):
    if not os.path.exists(filename):
        print(f"Errore: file '{filename}' non trovato!")
        sys.exit(1)
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        weights = [float(lines[i].split(":")[1].strip()) for i in range(FEATURES)]
        bias = float(lines[FEATURES].split(":")[1].strip())
        return weights, bias
    except Exception as e:
        print(f"Errore nella lettura dei pesi: {e}")
        sys.exit(1)


def activation(x):
    if x > THRESHOLD:
        return 1
    else:
        return 0


def prevedi(weights, bias, inputs):
    somma = bias
    for i in range(FEATURES):
        somma += inputs[i] * weights[i]
    return activation(somma)


def main():
    random.seed(42)

    weights, bias = carica_pesi("pesi_concerto.txt")

    print(f"Pesi: {weights}")
    print(f"Bias: {bias}")
    print(f"Soglia: {THRESHOLD}")
    print(f"Campioni: {N_CAMPIONI}")
    print()

    vai = 0
    resta = 0

    for idx in range(1, N_CAMPIONI + 1):
        inputs = [random.randint(0, 1) for _ in range(FEATURES)]
        risultato = prevedi(weights, bias, inputs)

        if risultato == 1:
            vai += 1
            print(f"[{idx:>3}] {inputs} -> VAI al concerto")
        else:
            resta += 1
            print(f"[{idx:>3}] {inputs} -> RESTA a casa")

    print()
    print(f"Risultati su {N_CAMPIONI} campioni:")
    print(f"  Vai al concerto: {vai} ({vai / N_CAMPIONI * 100:.1f}%)")
    print(f"  Resta a casa:    {resta} ({resta / N_CAMPIONI * 100:.1f}%)")


if __name__ == "__main__":
    main()
