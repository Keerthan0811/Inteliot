import json

def save_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)