import pandas as pd
import numpy as np
import itertools
import datetime

start = datetime.datetime.now()

df = pd.read_csv(
    "/media/drbh/Untitled/question-similarity/allclass_vectors.csv")

del df["Unnamed: 0"]
del df["class"]

loaded = datetime.datetime.now()
print("loadtime: {}".format(loaded - start))

m = df.values
del df

unique = m[np.triu_indices(len(m), k = 1)]

uniqued = datetime.datetime.now()
print("uniqued: {}".format(uniqued - loaded))

df = pd.DataFrame(unique)

df.to_csv("unied.csv", index=False)