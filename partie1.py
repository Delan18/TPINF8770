import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
import numpy as np
from scipy.stats import entropy

def analyse_texte(texte, type_fichier):

    # Extraire les mots avec regex
    mots = re.findall(r"\w+", texte.lower())

    nb_total_mots = len(mots)
    nb_mots_uniques = len(set(mots))
    pourcentage_mots_uniques = 0

    # Richesse lexicale
    if nb_total_mots > 0:
        pourcentage_mots_uniques = (nb_mots_uniques / nb_total_mots)*100

    print(f"Nombre total de mots : {nb_total_mots}")
    print(f"Nombre de mots uniques : {nb_mots_uniques}")
    print(f"Pourcentage de mots uniques : {pourcentage_mots_uniques}%")

    

    # Entropie de Shannon (caractères)
    caracteres = list(texte) 
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


    # Graphe mots les plus fréquents

    compteur = Counter(mots)
    top10 = compteur.most_common(10)
    mots_top, freq_top = zip(*top10)
    plt.figure(figsize=(10,6))
    plt.bar(mots_top, freq_top)
    plt.xticks(rotation=45)
    plt.title(f"Top 10 mots les plus fréquents pour {type_fichier}")
    plt.xlabel("Mots")
    plt.ylabel("Fréquence")
    plt.tight_layout()
    plt.show()

    # Graphe des caractères les plus frequents
    top_chars = Counter(texte).most_common(20)
    chars, freqs = zip(*top_chars)

    plt.figure(figsize=(10,5))
    plt.bar(chars, freqs, color="skyblue")
    plt.title(f"Top 20 caractères les plus fréquents pour {type_fichier}")
    plt.xlabel("Caractères")
    plt.ylabel("Fréquence")
    plt.show()



if __name__ == "__main__":

    # Fichier CSV
    chemin_csv = "data/text_structured/accumulation-accounts-2008-2023-provisional.csv"
    df = pd.read_csv(chemin_csv)
    texte_csv = " ".join(df.astype(str).values.flatten())

    # Fichier Code
    chemin_code = "data/text_code/code2.html"
    with open(chemin_code, 'r', encoding='utf-8', errors='ignore') as file:
        texte_code = file.read() 

    # Fichier Texte
    chemin_code = "data/text_natural/text_natural_1.txt"
    with open(chemin_code, 'r', encoding='utf-8', errors='ignore') as file:
        texte_natural = file.read()

    # Analyse
    print("=== Analyse CSV ===")
    analyse_texte(texte_csv, "Strutured CSV")

    print("\n=== Analyse fichier code ===")
    analyse_texte(texte_code, "Code html")

    print("\n=== Analyse fichier texte ===")
    analyse_texte(texte_natural, "Texte Naturel")





