import LZW
import LZ77
import huffmann
import ParPlage
import ParChaine
import Predictif

if __name__ == "__main__":

    ## ----- Text Structuré CSV ------- ##
    print("=== Compression CSV ===")
    with open("text_structured/accumulation-accounts-2008-2023-provisional.csv", "r", encoding="utf-8") as f:
        text = f.read()

    
    compressed = LZW.lzw_compression(text)
    compressed_data = LZ77.lz77_compress(text)
    donnees_compressees, dictionnaire = huffmann.huffman_compress(text)
    compresse_chaine = ParChaine.codage_chaine(text)
    compresse_predictif = Predictif.codage_predictif(text)

    ## ----- Text Code Html ------- ##
    print("=== Compression Code ===")
    with open("text_code/code2.html", 'r', encoding='utf-8', errors='ignore') as file:
        texte_code = file.read()

    html_LZW = LZW.lzw_compression(texte_code)
    html_LZ77 = LZ77.lz77_compress(texte_code)
    html_huffman , html_dictionnaire = huffmann.huffman_compress(texte_code)
    html_chaine = ParChaine.codage_chaine(texte_code)
    html_predictif = Predictif.codage_predictif(texte_code)

    ## ----- Text Natural ------- ##
    print("=== Compression Texte Naturel ===")
    with open("text_natural/text_natural_1.txt", 'r', encoding='utf-8', errors='ignore') as file:
        texte_natural = file.read()

    nat_LZW = LZW.lzw_compression(texte_natural)
    nat_LZ77 = LZ77.lz77_compress(texte_natural)
    nat_huffman , nat_dictionnaire = huffmann.huffman_compress(texte_natural)
    nat_chaine = ParChaine.codage_chaine(texte_natural)
    nat_predictif = Predictif.codage_predictif(texte_natural)



    

