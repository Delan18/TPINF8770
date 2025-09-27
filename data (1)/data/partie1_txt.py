import matplotlib.pyplot as plt
from collections import Counter
import re
import numpy as np
from scipy.stats import entropy
from pathlib import Path

# --- Charger le TXT ---
txt_path = "data (1)/data/text_natural/text_natural_1.txt"  # <- mets ton chemin .txt ici
text = Path(txt_path).read_text(encoding="utf-8", errors="ignore")

# --- Extraire les mots avec regex: on prend tout ce qui est alphanumérique (accents gérés), en minuscules ---
mots = re.findall(r"\w+", text.lower(), flags=re.UNICODE)

# --- Nombre total de mots ---
nb_total_mots = len(mots)

# --- Nombre de mots uniques ---
nb_mots_uniques = len(set(mots))
pourcentage_mots_uniques = 0

# --- Richesse lexicale ---
if nb_total_mots > 0:
    pourcentage_mots_uniques = (nb_mots_uniques / nb_total_mots) * 100

print(f"Nombre total de mots : {nb_total_mots}")
print(f"Nombre de mots uniques : {nb_mots_uniques}")
print(f"Pourcentage de mots uniques : {pourcentage_mots_uniques:.2f}%")

# --- Compter la fréquence des mots ---
compteur = Counter(mots)

# --- Top 10 mots les plus fréquents ---
top10 = compteur.most_common(10)

# --- Entropie de Shannon (caractères) ---
caracteres = list(text)
compteur_chars = Counter(caracteres)
freqs = np.array(list(compteur_chars.values()), dtype=float)
probas = freqs / freqs.sum() if freqs.sum() > 0 else np.array([])

H = entropy(probas, base=2) if probas.size > 0 else 0.0  # entropie en bits par caractère
Hmax = np.log2(len(compteur_chars)) if len(compteur_chars) > 0 else 0.0  # entropie maximale possible
redondance = 1 - (H / Hmax if Hmax > 0 else 0)

print("\n--- Entropie et redondance ---")
print(f"Entropie de Shannon (caractères) : {H:.4f} bits/symbole")
print(f"Entropie max possible : {Hmax:.4f} bits/symbole")
print(f"Taux de redondance : {redondance:.2%}")

# --- Visualisation histogramme (Top 10 mots) ---
mots_top, freq_top = zip(*top10)
plt.figure(figsize=(10, 6))
plt.bar(mots_top, freq_top)
plt.xticks(rotation=45)
plt.title("Top 10 mots les plus fréquents")
plt.xlabel("Mots")
plt.ylabel("Fréquence")
plt.tight_layout()
plt.show()

# --- Histogramme des caractères les plus fréquents ---
top_chars = Counter(text.lower()).most_common(20)
chars, freqs = zip(*top_chars)
plt.figure(figsize=(10, 5))
plt.bar(chars, freqs)
plt.title("Top 20 caractères les plus fréquents")
plt.xlabel("Caractères")
plt.ylabel("Fréquence")
plt.tight_layout()
plt.show()
