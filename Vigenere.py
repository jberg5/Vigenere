def Vigenere(text,size):
    combos = [text[i:i+size] for i in range(len(text)-size)]
    results = []
    for string in combos:
        if combos.count(string) > 2:
            results.append((string,combos.count(string)))
    return set(results)

def freq(text,start,size,threshold):
    text = text.lower()
    letters = [text[i] for i in range(0,len(text),size)]
    results = []
    for letter in "abcdefghijklmnopqrstuvwxyz":
        freq = float(letters.count(letter)/len(letters))*100
        if freq > threshold:
            results.append((letter,freq))
    return results
