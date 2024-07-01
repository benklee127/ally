import docx

def basic_chunker(file):
    with open(file) as file:
        while (chunk := file.read(500)) and (id < 10):
            print(chunk)
            print(id)
            id += 1


