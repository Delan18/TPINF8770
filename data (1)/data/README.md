# Analyse de fichiers CSV - Compression et Entropie

Ce projet permet d'analyser un fichier CSV afin de mesurer certains critères qui influencent sa **compressibilité**, notamment :
- Richesse lexicale (nombre de mots uniques / total de mots)
- Distribution des mots les plus fréquents
- Entropie de Shannon (caractères)
- Taux de redondance

Un histogramme des 20 mots les plus fréquents est également généré.

---


## Installation


```bash
pip install pandas scipy matplotlib
