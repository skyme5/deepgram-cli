import os


def get_ext(filepth):
    _, ext = os.path.splitext(filepth)
    return ext


def save_file(data, filepath):
    with open(filepath, "w") as f:
        f.write(data)
