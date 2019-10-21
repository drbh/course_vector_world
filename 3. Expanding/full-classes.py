import pandas as pd

df = pd.read_csv("unied.csv")
fd = pd.read_csv("index_list.csv", header=None)

fd["score"] = df["0"].values

# print(df.head(10), df.shape)
print(fd.head(10), fd.shape)

fd.columns = ["X","Y","S"]
# print(fd.query("Y == 1").shape)

xf = pd.read_csv("/media/drbh/Untitled/question-similarity/allclass_vectors.csv")
cls_index = xf["class"].values
del xf

xes = fd.X.values.tolist()
fd["X"] = [cls_index[i] for i in xes]
yes = fd.Y.values.tolist()
fd["Y"] = [cls_index[i] for i in yes]

fd.to_csv("complete_list_of_similar_classes", index=False)