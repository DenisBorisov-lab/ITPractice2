def read_file(file_name: str):
    file = open(file_name, "rb")
    dictionary = {}
    symbol = ""
    code = bytes()

    while 1:
        current = file.read(1)

        if current[0] == ord("$"):
            dictionary[symbol] = code.decode("utf-8")
            symbol = ""
            code = bytes()
            continue

        if not symbol:
            if current[0] == ord('|'):
                break
            symbol = chr(int.from_bytes(current + file.read(1), "little"))
            continue

        code += current
    print(dictionary)


def decode(file_name: str):
    read_file(file_name)
