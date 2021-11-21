def read_chunked(file):
    while True:
        s = file.read(1)
        if not s:
            return
        else:
            yield bin(int.from_bytes(s, "little"))[2:].zfill(8)


def read_file(file_name: str):
    file = open(file_name, "rb")
    dictionary = dict()

    alphabet = bytes()
    end = '####'.encode('utf-8')
    while not alphabet.endswith(end):
        alphabet += file.read(1)
    alphabet = alphabet.removesuffix(end)

    while alphabet:
        end = alphabet.index('$$'.encode('utf-8'))
        dictionary[chr(int.from_bytes(alphabet[0:4], 'little'))] = alphabet[4:end].decode('utf-8')
        alphabet = alphabet[end + 2:]

    codes = {v: k for k, v in dictionary.items()}

    binary_view = read_chunked(file)

    file = open("decoded" + file_name[:-7] + ".txt", "w", encoding="utf-8", newline='\n')

    string = ""
    for chunk in binary_view:
        for ch in chunk:
            string += ch
            if string in codes:
                file.write(codes[string])
                string = ""


def decode(file_name: str):
    read_file(file_name)
