def load_document(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()