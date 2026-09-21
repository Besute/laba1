import decimal
import json
from pathlib import Path
from .errors import InvalidValueError
from decimal import *

JSON_FILE = Path(__file__).parent / "converts.json"
LENGTH_TO_M = {}

def load_conversions():
    with open(JSON_FILE, "r") as file:
        return json.load(file)

convers =  load_conversions()

def execute_length(val, from_, to_):
    convert_to_m = convers["length_to_m"][from_] * val
    convert_to_goal = convers["m_to_length"][to_] * convert_to_m
    return convert_to_goal

def execute_mass(val, from_, to_):
    convert_to_g = convers["mass_to_g"][from_] * val
    convert_to_goal = convers["g_to_mass"][to_] * convert_to_g
    return convert_to_goal

def execute_temper(val, from_, to_):
    convert_to_c = convers[from_]["c"]["mult"] * val + convers[from_]["c"]["offset"]
    convert_to_goal = convers["c"][to_]["mult"] * convert_to_c + convers["c"][to_]["offset"]
    return convert_to_goal

def evaluate_from(val, from_, to_):
    if from_ in ["km", "m", "cm", "mm"] and to_ in ["km", "m", "cm", "mm"]:
        if float(val) < 0:
            raise InvalidValueError("Length can't be negative")
        return decimal.Decimal(execute_length(float(val), from_, to_))
    elif from_ in ["g", "kg"] and to_ in ["kg", "g"]:
        if float(val) < 0:
            raise InvalidValueError("Mass can't be negative")
        return decimal.Decimal(execute_mass(float(val), from_, to_))
    elif from_ in ["c", "f", "k"] and to_ in ["c", "f", "k"]:
        total_temp = execute_temper(val, from_, to_)
        total_zero = execute_temper(0, "k", to_)
        if total_zero > total_temp:
            raise InvalidValueError("You have temperature below absolute zero")
        return decimal.Decimal(total_temp)
    raise InvalidValueError(f"You can't convert {from_} to {to_}")

def convert(val, from_, to_):
    return evaluate_from(val, from_, to_)