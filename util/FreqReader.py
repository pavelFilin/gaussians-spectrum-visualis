import re
import pandas as pd

def read_freq(path):
    freq = []
    file = open(path, "r")
    i = 0
    for line in file:
        if line.__len__ != 0 and line[0] != '#' and line[0] != '\n':
            numbers = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", line)
            freq.append([float(numbers[0]), float(numbers[1]), float(numbers[2])] )
    file.close()
    df = pd.DataFrame(freq, columns=["X", "Y", "dY"])
    return df