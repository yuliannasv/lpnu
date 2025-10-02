user_input = input("Введіть 4-значне число: ")

if len(user_input) == 4 and user_input.isdigit():
    digit_sum = sum(int(digit) for digit in user_input)
    print(f"Сума цифр {user_input} = {digit_sum}")
else:
    print("Будь ласка, введіть коректне 4-значне число.")