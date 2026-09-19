LENGTH_TO_M = {
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001
}

M_TO_LENGTH = {
    "km": 0.001,
    "m": 1,
    "cm": 100,
    "mm": 1000
}

MASS_TO_G = {
    "g": 1,
    "kg": 1000
}

G_TO_MASS = {
    "g": 1,
    "kg": 0.001
}

def faren_to_c(faren):
    return (faren - 32) * 5/9

def kel_to_c(k):
    return k - 273.15

def c_to_kel(c):
    return c + 273.15

def c_to_faren(c):
    return c * 9/5 + 32

def execute_length(val, from_, to_):
    val_in_m = LENGTH_TO_M[from_] * val
    val_ans = M_TO_LENGTH[to_] * val_in_m
    return val_ans

def execute_mass(val, from_, to_):
    val_in_g = MASS_TO_G[from_] * val
    val_ans = G_TO_MASS[to_] * val_in_g
    return val_ans

def execute_temper(val, from_, to_):
    val_in_c = val
    if from_ == "f":
        val_in_c = faren_to_c(val)
    elif from_ == "k":
        val_in_c = kel_to_c(val)
    val_ans = val_in_c
    if to_ == "f":
        val_ans = c_to_faren(val_ans)
    elif to_ == "k":
        val_ans = c_to_kel(val_ans)
    return val_ans

def evaluate_from(val, from_, to_):
    if from_ in ["km", "m", "cm", "mm"]:
        return execute_length(float(val), from_, to_)
    elif from_ in ["g", "kg"]:
        return execute_mass(float(val), from_, to_)
    elif from_ in ["c", "f", "k"]:
        total_temp = execute_temper(float(val), from_, to_)
        total_zero = execute_temper(0, "k", to_)
        if (total_zero > total_temp):
            raise ValueError("YOUR TEMPERATURE IS BELOW ABSOLUTE ZERO")
        return total_temp
    raise SyntaxError(f"INCORRECT MEASURE: CAN'T CONVER FROM {from_} to {to_}")

def convert(val, from_, to_):
    return evaluate_from(val, from_, to_)