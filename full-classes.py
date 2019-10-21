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

# qwert = fd.query("Y == @u | X == @u")


# u = 6789

# def maketopn(u):
# 	qwert = fd.query("Y == @u | X == @u")
# 	topn = qwert.sort_values("S", ascending=False).head(5)
# 	xes = topn.X.values.tolist()
# 	topn["X"] = [cls_index[i] for i in xes]
# 	yes = topn.Y.values.tolist()
# 	topn["Y"] = [cls_index[i] for i in yes]
# 	return topn


# results = []
# for i in range(0,14065):
# 	r = maketopn(i)
# 	results += [r]


# output = pd.concat(results)


# output.to_csv("top5.csv", index=False)