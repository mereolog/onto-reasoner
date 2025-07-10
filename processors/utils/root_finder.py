import pathlib


def find_project_root(filename="requirements.txt"):
    current = pathlib.Path(__file__).resolve().parent
    for parent in [current, *current.parents]:
        if (parent / filename).exists():
            return parent
    raise FileNotFoundError(f"{filename} not found in any parent directory")
