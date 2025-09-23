# huffman_text.py
import huffman
from collections import Counter
import time

def huffman_compress(text):
    """
    Compresse un texte en utilisant Huffman.
    text : chaîne de caractères
    Retourne : encoded (texte compressé en bits), codes (dictionnaire Huffman)
    """

    # Débuter le compteur 
    start = time.time()      
    # Compter les caractères
    freq = Counter(text)

    # Construire le code Huffman
    codes = huffman.codebook(freq.items())

    # Encoder le texte
    encoded = ''.join(codes[c] for c in text)

    end = time.time()         # Temps après l'exécution

    

    # Taille originale et compressée
    original_bits = len(text) * 8
    compressed_bits = len(encoded)
    taux = 100 * (1 - compressed_bits / original_bits)

    print("===== Huffman Compression =====")
    print("Taille originale :", original_bits, "bits")
    print("Taille compressée :", compressed_bits, "bits")
    print("Taux de compression :", taux, "%")
    print("Temps écoulé :", end - start, "secondes \n")

    return encoded, codes
