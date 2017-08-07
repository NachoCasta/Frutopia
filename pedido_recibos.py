import json

productos = {
    "frutillas": {
        "2": {
            "nombre": "Frutillas 2 kg",
            "variable": "frutillas",
            "variable_precio": "f_precio",
            "formato": "cajas"
            }
        },
    "paltas": {
        "2": {
            "nombre": "Paltas 2 kg",
            "variable": "paltas",
            "variable_precio": "p_precio",
            "formato": "mallas"
            }
        },
    "naranjas": {
        "5": {
            "nombre": "Naranjas 5 kg",
            "variable": "naranjas",
            "variable_precio": "nar_precio",
            "formato": "mallas"
            }
        },
    "mandarinas": {
        "4": {
            "nombre": "Mandarinas 4 kg",
            "variable": "mandarinas",
            "variable_precio": "m_precio",
            "formato": "mallas"
            }
        },
    "quesos": {
        "1050": {
            "nombre": "Quesos 1050 gr",
            "variable": "quesos",
            "variable_precio": "q_precio",
            "formato": "packs"
            }
        },
    "tomate cherry": {
        "1": {
            "nombre": "Tomate Cherry 1 kg",
            "variable": "tomatecherry",
            "variable_precio": "t_precio",
            "formato": "cajas"
            }
        },
    "nueces": {
        "500": {
            "nombre": "Nueces 500 gr",
            "variable": "nueces",
            "variable_precio": "nue_precio",
            "formato": "cajas"
            }
        }
    }

with open("productos.json", "w") as file:
    json.dump(productos, file, sort_keys=True, indent=4)


with open("productos.json", "r") as file:
    p = json.load(file)
