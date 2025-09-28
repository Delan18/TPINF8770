import time
from collections import Counter

def codage_plage_simple(data):
    start = time.time()
    
    freq = Counter(data)
    total = len(data)
    probs = {c: freq[c]/total for c in freq}
    
    low, high = 0.0, 1.0
    for c in data:
        range_ = high - low
        cumul = 0.0
        for s in sorted(probs):
            if s == c:
                high = low + range_ * (cumul + probs[s])
                low = low + range_ * cumul
                break
            cumul += probs[s]
    
    # code final approximatif
    compressed = [(low + high)/2]

    end = time.time()
    print("===== Compression Codage par plage simplifié =====")
    print("Taille originale :", len(data), "caractères")
    print("Taille compressée :", len(compressed), "codes")
    print("Taux de compression :", 100 * (1 - len(compressed)/len(data)), "%")
    print("Temps écoulé :", end - start, "secondes\n")
    
    return compressed
