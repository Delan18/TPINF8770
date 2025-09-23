# codage_predictif.py
import time

def codage_predictif(data):
    start = time.time()
    valeurs = [int(c) for c in data if c.isdigit()]
    if not valeurs:
        return []
    code = [valeurs[0]]
    for i in range(1, len(valeurs)):
        code.append(valeurs[i] - valeurs[i-1])
    
    end = time.time()
    print("===== Compression Codage prédictif =====")
    print("Taille originale :", len(valeurs), "valeurs numériques")
    print("Taille compressée :", len(code), "codes")
    print("Taux de compression :", 100 * (1 - len(code)/len(valeurs)), "%")
    print("Temps écoulé :", end - start, "secondes\n")

    return code


  
