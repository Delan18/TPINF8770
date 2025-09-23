import LZW
import LZ77
import huffmann
import ParPlage
import ParChaine
import Predictif

if __name__ == "__main__":

    ## ----- Text Structuré CSV ------- ##
    
    with open("C:/Users/delan/Documents/TP8770/TPINF8770/data (1)/data/text_structured/accumulation-accounts-2008-2023-provisional.csv", "r", encoding="utf-8") as f:
        text = f.read()

    compressed = LZW.lzw_compression(text)
    donnees_compressees, dictionnaire = huffmann.huffman_compress(text)
    compressed_data = LZ77.lz77_compress(text)
    compresse_chaine = ParChaine.codage_chaine(text)
    compresse_predictif = Predictif.codage_predictif(text)


