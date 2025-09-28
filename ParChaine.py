import time

def codage_chaine(data):
    start = time.time()
    if not data:
        return []
    code = []
    prev_char = data[0]
    count = 1
    for c in data[1:]:
        if c == prev_char:
            count += 1
        else:
            code.append((prev_char, count))
            prev_char = c
            count = 1
    code.append((prev_char, count))
    end = time.time()
    print("===== Compression Codage en chaîne =====")
    print("Taille originale :", len(data), "caractères")
    print("Taille compressée :", len(code), "codes")
    print("Taux de compression :", 100 * (1 - len(code)/len(data)), "%")
    print("Temps écoulé :", end - start, "secondes\n")

    return code

   
