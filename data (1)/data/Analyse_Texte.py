import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
import numpy as np
from scipy.stats import entropy

def analyse_texte(texte):

    # # --- Charger le CSV (dans le dataframe de Pandas) ---
    # df = pd.read_csv(filepath)

    # mots = re.findall(r"\w+", text.lower())
    # # --- Convertir tout le contenu du CSV en une seule chaîne de texte ---
    # text = " ".join(df.astype(str).values.flatten())

    # --- Extraire les mots avec regex: On prend tout ce qui est alpha num.rique, donc les virgules sont enlevées---
    mots = re.findall(r"\w+", texte.lower())

    # --- Nombre total de mots ---
    nb_total_mots = len(mots)

    # --- Nombre de mots uniques ---
    nb_mots_uniques = len(set(mots))
    pourcentage_mots_uniques = 0

    # --- Richesse lexicale ---
    if nb_total_mots > 0:
        pourcentage_mots_uniques = (nb_mots_uniques / nb_total_mots)*100

    print(f"Nombre total de mots : {nb_total_mots}")
    print(f"Nombre de mots uniques : {nb_mots_uniques}")
    print(f"Pourcentage de mots uniques : {pourcentage_mots_uniques}%")

    # --- Compter la fréquence des mots ---
    compteur = Counter(mots)

    # --- Top 20 mots les plus fréquents ---
    top10 = compteur.most_common(10)

    # --- Entropie de Shannon (caractères) ---
    caracteres = list(texte)  # sépare chaque caractère
    compteur_chars = Counter(caracteres)
    freqs = np.array(list(compteur_chars.values()))
    probas = freqs / freqs.sum()

    H = entropy(probas, base=2)  # entropie en bits par caractère
    Hmax = np.log2(len(compteur_chars))  # entropie maximale possible
    redondance = 1 - (H / Hmax if Hmax > 0 else 0)

    print("\n--- Entropie et redondance ---")
    print(f"Entropie de Shannon (caractères) : {H:.4f} bits/symbole")
    print(f"Entropie max possible : {Hmax:.4f} bits/symbole")
    print(f"Taux de redondance : {redondance:.2%}")


    # --- Visualisation histogramme ---
    mots_top, freq_top = zip(*top10)
    plt.figure(figsize=(10,6))
    plt.bar(mots_top, freq_top)
    plt.xticks(rotation=45)
    plt.title("Top 10 mots les plus fréquents")
    plt.xlabel("Mots")
    plt.ylabel("Fréquence")
    plt.tight_layout()
    plt.show()

    # --- Histogramme des caractères les plus fréquents ---
    top_chars = Counter(texte.lower()).most_common(20)
    chars, freqs = zip(*top_chars)

    plt.figure(figsize=(10,5))
    plt.bar(chars, freqs, color="skyblue")
    plt.title("Top 20 caractères les plus fréquents")
    plt.xlabel("Caractères")
    plt.ylabel("Fréquence")
    plt.show()
