import json
from pathlib import Path

FILE_PATH = Path("data\students.json")


def load_students():

    if not FILE_PATH.exists():
        FILE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True)

        FILE_PATH.write_text("[]")

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_students(students):
    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)