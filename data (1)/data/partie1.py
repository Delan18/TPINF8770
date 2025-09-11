import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
import numpy as np
from scipy.stats import entropy

# --- Charger le CSV ---
df = pd.read_csv("C:/Users/delan/Documents/TP8770/TPINF8770/data (1)/data/text_structured/accumulation-accounts-2008-2023-provisional.csv")

# --- Convertir tout le contenu du CSV en une seule chaîne de texte ---
text = " ".join(df.astype(str).values.flatten())

# --- Tokenisation simple : extraire les mots avec regex ---
mots = re.findall(r"\w+", text.lower())

# --- Nombre total de mots ---
nb_total_mots = len(mots)

# --- Nombre de mots uniques ---
nb_mots_uniques = len(set(mots))

# --- Richesse lexicale ---
richesse = nb_mots_uniques / nb_total_mots if nb_total_mots > 0 else 0

print(f"Nombre total de mots : {nb_total_mots}")
print(f"Nombre de mots uniques : {nb_mots_uniques}")
print(f"Richesse lexicale : {richesse:.4f}")

# --- Compter la fréquence des mots ---
compteur = Counter(mots)

# --- Top 20 mots les plus fréquents ---
top20 = compteur.most_common(20)

# --- Visualisation histogramme ---
mots_top, freq_top = zip(*top20)
plt.figure(figsize=(10,6))
plt.bar(mots_top, freq_top)
plt.xticks(rotation=45)
plt.title("Top 20 mots les plus fréquents")
plt.xlabel("Mots")
plt.ylabel("Fréquence")
plt.tight_layout()
plt.show()

# --- Entropie de Shannon (caractères) ---
caracteres = list(text)  # sépare chaque caractère
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
