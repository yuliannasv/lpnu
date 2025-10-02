x = float(input("Введіть додатне дійсне число: "))

if x > 0:
    fractional_part = x - int(x)
    print(f"Дробова частина {x} = {fractional_part}")
else:
    print("Будь ласка, введіть додатне число.")
