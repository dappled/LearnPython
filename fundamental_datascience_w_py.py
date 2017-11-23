
import numpy as np
import pandas as pd
if __name__ == "__main__":

    #s = np.arange(13) ** 2

    a = pd.Series({'a':0,
                   'b':1,
                   'c':2,
                   'd':3})
    b = pd.Series({'e':4,
                   'f':5,
                   'g':6,
                   'h':7})
    c = a.append(b)

    input()