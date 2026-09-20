import json
from pathlib import Path
from .errors import InvalidValueError

JSON_FILE = Path(__file__).parent / "converts.json"
LENGTH_TO_M = {}

def load_conversions():
    with open(JSON_FILE, "r") as file:
        return json.load(file)

convers =  load_conversions()

def faren_to_c(faren):
    return (faren - 32) * 5/9

def kel_to_c(k):
    return k - 273.15

def c_to_kel(c):
    return c + 273.15

def c_to_faren(c):
    return c * 9/5 + 32

def execute_length(val, from_, to_):
    convert_to_m = convers[from_]["m"] * val
    convert_to_goal = convers["m"][to_] * convert_to_m
    return convert_to_goal

def execute_mass(val, from_, to_):
    convert_to_g = convers[from_]["g"] * val
    convert_to_goal = convers["g"][to_] * convert_to_g
    return convert_to_goal

def execute_temper(val, from_, to_):
    convert_to_c = convers[from_]["c"]["mult"] * val + convers[from_]["c"]["offset"]
    convert_to_goal = convers["c"][to_]["mult"] * convert_to_c + convers["c"][to_]["offset"]
    return convert_to_goal

def evaluate_from(val, from_, to_):
    if from_ in ["km", "m", "cm", "mm"]:
        return execute_length(float(val), from_, to_)
    elif from_ in ["g", "kg"]:
        return execute_mass(float(val), from_, to_)
    elif from_ in ["c", "f", "k"]:
        total_temp = execute_temper(float(val), from_, to_)
        total_zero = execute_temper(0, "k", to_)
        if total_zero > total_temp:
            raise InvalidValueError("You have temperature below absolute zero")
        return total_temp
    raise InvalidValueError(f"You can't convert {from_} to {to_}")

def convert(val, from_, to_):
    return evaluate_from(val, from_, to_)