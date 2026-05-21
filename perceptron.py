

import os
import sys

FEATURES = 5
THRESHOLD = 1.5


def activation(x):
    if x > THRESHOLD:
        return 1
    else:
        return 0


def carica_pesi(filename):
    if not os.path.exists(filename):
        print(f"Errore: file {filename} non trovato!")
        sys.exit(1)

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        weights = []
        for i in range(FEATURES):
            valore = lines[i].split(":")[1].strip()
            weights.append(float(valore))

        bias = float(lines[FEATURES].split(":")[1].strip())
        return weights, bias

    except Exception as e:
        print(f"Errore nella lettura del file: {e}")
        sys.exit(1)


def prevedi(weights, bias, inputs):
    somma = bias
    for i in range(FEATURES):
        somma += inputs[i] * weights[i]
    return activation(somma)


def main():
    weights, bias = carica_pesi("pesi_concerto.txt")

    print("Inserisci i dati:")

    domande = [
        "Artista famoso? (1=Si, 0=No): ",
        "Bel meteo? (1=Si, 0=No): ",
        "Amici presenti? (1=Si, 0=No): ",
        "Cibo buono? (1=Si, 0=No): ",
        "Alcool disponibile? (1=Si, 0=No): "
    ]

    inputs = []
    for domanda in domande:
        while True:
            try:
                risposta = int(input(domanda))
                if risposta in (0, 1):
                    inputs.append(risposta)
                    break
                else:
                    print("Errore: devi inserire solo 1 o 0.")
            except ValueError:
                print("Errore: input non valido. Inserisci 1 o 0.")

    decisione = prevedi(weights, bias, inputs)

    if decisione == 1:
        print("\nVai al concerto!")
    else:
        print("\nResta a casa!")


if __name__ == "__main__":
    main()
