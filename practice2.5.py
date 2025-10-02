import math

def pi_leibniz_err(target_err):
    s = 0.0
    k = 0
    while True:
        s += ((-1) ** k) / (2 * k + 1)
        pi_approx = 4 * s
        error = abs(math.pi - pi_approx)
        if error < target_err:
            return k + 1, pi_approx, error
        k += 1

err_target = 1e-5
n, pi_val, err = pi_leibniz_err(err_target)
print(f"Для похибки {err_target} потрібно {n} членів")
print(f"Наближене значення π = {pi_val}")
print(f"Похибка = {err}")