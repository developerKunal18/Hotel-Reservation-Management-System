import json
import os


def load_data(filename):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(filename, data):
    folder = os.path.dirname(filename)

    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
