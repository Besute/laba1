import json

OPERANDS = "+-*/()!?№%"
REAL_OPERANDS = "+-*/()%"

def load_json(JSON_FILE):
    with open(JSON_FILE, "r") as file:
        return json.load(file)

def save_data(data, path):
    with open(path, "w") as file:
        json.dump(data, file, indent=2)

def is_int(num):
    return int(num) == num

def is_oper(symb):
    return symb in OPERANDS
