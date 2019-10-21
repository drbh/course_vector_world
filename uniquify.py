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
# unique.tofile("uniqued.dat", dtype=int)

# nx = len(m)
# print(nx)
# lst = range(0,nx)

# p = itertools.product(lst, range(0,nx))
# q = [tuple(reversed(x)) for x in p] 
# del p

# bindexed = datetime.datetime.now()
# print("build indexs: {}".format(bindexed - uniqued))

# def divide_chunks(l, n): 
#     # looping till length l 
#     for i in range(0, len(l), n):  
#         yield l[i:i + n] 
        
# mtrx = np.array(divide_chunks(q, nx))

# splited = datetime.datetime.now()
# print("split indexs: {}".format(splited - bindexed))

# locs = mtrx[np.triu_indices(4, k = 1)]

# list1, list2 = zip(*locs)

# example = pd.DataFrame([list1,list2, unique]).T