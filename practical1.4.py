import math

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Корені рівняння: x1 = {x1:.2f}, x2 = {x2:.2f}")
elif D == 0:
    x = -b / (2*a)
    print(f"Є один корінь: x = {x:.2f}")
else:
    print("Коренів немає (дискримінант менше нуля).")