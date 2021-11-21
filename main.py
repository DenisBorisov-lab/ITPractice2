import sys
from encoding import *
from decoding import *
if __name__ == "__main__":
    mode = sys.argv[1]
    file_name = sys.argv[2]
    if mode == "-e":
        encode(file_name)
    elif mode == "-d":
        decode(file_name)
# decode("oblomov.pumrar")
