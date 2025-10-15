items = [1, 2, 2, 3, 3, 3, 4]
freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1

print("Частота появи елементів:", freq)