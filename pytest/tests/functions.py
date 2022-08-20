FILENAME = 'f.txt'


def write_to_file(text, mode='a'):
    with open(FILENAME, mode) as file:
        file.write(text)


def read_from_file():
    with open(FILENAME, 'r') as file:
        return file.read()