# lzw.py
# Compression LZW en Python 
import time

def lzw_compression(text):
    # Si str, on encode en UTF-8 pour gérer les accents.
    if isinstance(text, str):
        data = text.encode("utf-8")
    else:
        data = text  

    # Début du minuteur
    start = time.time()

    # Dictionnaire initial : toutes les séquences d'un octet 
    dict_size = 256
    dictionary = {bytes([i]): i for i in range(dict_size)}

    w = b""
    compressed = []

    for b in data:
        c = bytes([b])
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            
            compressed.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Ajouter le dernier code
    if w:
        compressed.append(dictionary[w])

    end = time.time()

    print("===== LZW Compression =====")
    print("Taille originale :", len(data), "octets")
    print("Taille compressée :", len(compressed), "codes")
    print("Taux de compression :", 100 * (1 - len(compressed)/len(data)), "%")
    print("Temps écoulé :", end - start, "secondes\n")
    return compressed


