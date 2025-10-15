numbers = []

while len(numbers) < 10:
    num = int(input("Введіть число: "))
    if num not in numbers:
        numbers.append(num)
    else:
        print("Це число вже є у списку!")

print("Остаточний список:", numbers)