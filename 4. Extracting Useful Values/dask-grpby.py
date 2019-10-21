import dask.dataframe as dd

import datetime


start = datetime.datetime.now()

df = dd.read_csv("/home/drbh/Desktop/complete_list_of_similar_classes.csv")
df = df.persist()

g = df.groupby("Y").apply(lambda x: x.sort_values(by="S",ascending=False).head(6), meta={"X":"f8","Y":"f8","S":"f8"})
ooutput = g.compute()

end = datetime.datetime.now()

ooutput.columns = ["target","source","value"]
ooutput = ooutput.reset_index(drop=True)
ooutput = ooutput[["source","target","value"]]
ooutput.to_csv("topn.csv", index=False)

print(end-start)