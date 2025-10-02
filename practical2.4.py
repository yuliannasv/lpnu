import random

def calculate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate

num_samples = 1000000
pi_value = calculate_pi(num_samples)
print(f"цінка числа π: {pi_value}")