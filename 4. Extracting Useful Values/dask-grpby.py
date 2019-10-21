import dask.dataframe as dd

import datetime


start = datetime.datetime.now()

df = dd.read_csv("/home/drbh/Desktop/complete_list_of_similar_classes.csv")
df = df.persist()

g = df.groupby("Y").apply(lambda x: x.sort_values(by="S",ascending=False).head(2), meta={"X":"f8","Y":"f8","S":"f8"})
ooutput = g.compute()

end = datetime.datetime.now()

ooutput.to_csv("topn.csv")

print(end-start)