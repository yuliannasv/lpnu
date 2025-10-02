import math

def get_numbers():
    a = int(input("Введіть перше ціле число (a): "))
    b = int(input("Введіть друге ціле число (b): "))
    return a, b

def calculate_and_display(a, b):
    sum_ab = a + b
    diff_ab = a - b
    product_ab = a * b
    avg_arithmetic = sum_ab / 2
    avg_geometric = math.sqrt(product_ab)
    distance = abs(diff_ab)
    maximum = max(a, b)
    minimum = min(a, b)
    sum_of_squares = a**2 + b**2
    square_of_sum = sum_ab**2
    power_ab = a ** b

    print(f"Сума: {sum_ab}")
    print(f"Різниця: {diff_ab}")
    print(f"Добуток: {product_ab}")
    print(f"Середнє арифметичне: {avg_arithmetic}")
    print(f"Середнє геометричне: {avg_geometric}")
    print(f"Відстань (абсолютне значення різниці): {distance}")
    print(f"Максимум: {maximum}")
    print(f"Мінімум: {minimum}")
    print(f"Сума квадратів: {sum_of_squares}")
    print(f"Квадрат суми: {square_of_sum}")
    print(f"{a} в степені {b}: {power_ab}")

if __name__ == "__main__":
    a, b = get_numbers()
    calculate_and_display(a, b)