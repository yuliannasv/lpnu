nums = [1, 2, 3, 4, -1, 77, 29]
low, high = 3, 40
count = 0

for x in nums:
    if low <= x <= high:
        count += 1

print("Кількість елементів у діапазоні [3, 40]:", count)