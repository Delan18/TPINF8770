# lzw.py
# Compression et décompression LZW en Python

def lzw_compression(text):
    # Dictionnaire initial : tous les caractères uniques
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    compressed = []

    for c in text:
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

    print("===== LZW Compression =====")
    print("Taille originale :", len(text), "caractères")
    print("Taille compressée :", len(compressed), "codes")
    print("Taux de compression :", 100 * (1 - len(compressed)/len(text)), "%")
    
    return compressed


