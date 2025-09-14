# lz77_compress.py
import gzip

def lz77_compress(data):
    """
    Compresse des données avec gzip (LZ77 + Huffman).
    data : bytes ou texte encodé en bytes
    Retourne : compressed (données compressées en bytes)
    """
    # Si data est du texte, convertir en bytes
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Compression avec gzip
    compressed = gzip.compress(data)

    # Taille originale et compressée
    original_size = len(data)
    compressed_size = len(compressed)
    taux = 100 * (1 - compressed_size / original_size)

    print("===== LZ77/Gzip Compression =====")
    print("Taille originale :", original_size, "octets")
    print("Taille compressée :", compressed_size, "octets")
    print("Taux de compression :", taux, "%")

    return compressed
