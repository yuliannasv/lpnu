words = ['abc', 'xyz', 'aba', '1221']
n = 3
long_words = [w for w in words if len(w) > n]
print("Слова довші за", n, ":", long_words)
