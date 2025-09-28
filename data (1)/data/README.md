# Partie 1 - Analyse de fichiers

Ce projet permet d'analyser nos fichiers afin de mesurer certains critères qui influencent sa **compressibilité**, notamment :
- Richesse lexicale (nombre de mots uniques / total de mots)
- Distribution des mots les plus fréquents
- Entropie de Shannon (caractères)
- Taux de redondance

Un histogramme des 10 mots les plus fréquents et aussi des 20 caractères les plus fréquents sont générés.

---


## Installation


```bash
pip install pandas scipy matplotlib
```

pandas :
Pour charger et manipuler facilement le fichier CSV. Elle nous permet de lire rapidement les colonnes et de transformer les données en chaînes de caractères.

scipy :
Pour calculer l’entropie de Shannon via scipy.stats.entropy. L’entropie permet de mesurer l’imprévisibilité du texte et donc d’évaluer la compressibilité du fichier.

matplotlib :
Pour visualiser les données, par exemple créer l’histogramme des 10 mots les plus fréquents. Cela aide à illustrer les répétitions et la redondance dans le texte.

Counter : 
Cette librairie de python est utilisée (pas à installer, car elle est inclue dans python) pour pouvoir calculer la fréquence des mots dans un ensemble de mots (liste)

Entropy :
Cette librairie du module scipy.stats nous facilite la tâche de calculer l'entropy de Shannon


```bash
pip install huffman

```