import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# --- Charger le CSV ---
# Remplace "mon_fichier.csv" par ton fichier
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

# --- Visualisation ---
mots_top, freq_top = zip(*top20)
plt.figure(figsize=(10,6))
plt.bar(mots_top, freq_top)
plt.xticks(rotation=45)
plt.title("Top 20 mots les plus fréquents")
plt.xlabel("Mots")
plt.ylabel("Fréquence")
plt.tight_layout()
plt.show()



# 1. Compter le nombre de mots uniques.
# 2. Comparer ce nombre au total de mots (richesse lexicale = mots_uniques / mots_total).
# 3. Exemple de graphique : un histogramme des mots les plus fréquents (top 20).