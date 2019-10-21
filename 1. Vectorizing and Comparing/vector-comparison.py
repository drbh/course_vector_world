import pandas as pd
import tensorflow_hub as hub
import tensorflow as tf
import datetime
import numpy as np
from sqlalchemy import create_engine



fname = "/Volumes/Untitled 1/question-similarity/universal-sentence-encoder-large/"

module_url = fname

start = datetime.datetime.now()
# Create graph and finalize (optional but recommended).
g = tf.Graph()
with g.as_default():
    text_input = tf.placeholder(dtype=tf.string, shape=[None])
    embed = hub.Module(module_url)
    my_result = embed(text_input)
    init_op = tf.group(
        [tf.global_variables_initializer(), tf.tables_initializer()])
        
g.finalize()

# Create session and initialize.
session = tf.Session(graph=g)
session.run(init_op)

end_tf_init = datetime.datetime.now()

path ="postgresql://{}:{}@{}:{}/{}".format(
    "postgres", "YOUR PASSWORD",
    "YOUR HOST",
    "5432","postgres")
                                    
engine = create_engine(path)

dataframe = pd.read_sql('SELECT * FROM course_descriptions', engine)

# get the data
sentences = dataframe.description.values.tolist()
sentences = [ str(x) for x in sentences ]
print("sentences ready to be proccessed")

sentence_groups = np.array_split(sentences, 20)

start_process = datetime.datetime.now()

results = []
index = 0
for group in sentence_groups:
    start_ml = datetime.datetime.now()
    vectors = session.run( my_result, feed_dict={text_input: group})
    end_ml = datetime.datetime.now()
    result = {
        "time": (end_ml-start).total_seconds() * 1000,
        "vectors": vectors
    }
    results+=[result]
    index += 1
    print(index, "- finished ",len(group))
    
end_process = datetime.datetime.now()
print("took {} ms".format((end_process-start_process).total_seconds() * 1000))



vecs = []
for v in results:
#     for r in :
    vecs+=list(v["vectors"])


classes_as_vectors = pd.DataFrame(vecs)

classes_as_vectors.to_csv(
    "/Volumes/Untitled 1/question-similarity/classes_as_vectors.csv",index=False)

# https://en.wikipedia.org/wiki/Triangular_number
all_corrs = np.inner(vecs,vecs)
corr_frame = pd.DataFrame(all_corrs)
corr_frame["class"] = dataframe["code"]
corr_frame.to_csv(
    "/Volumes/Untitled 1/question-similarity/allclass_vectors.csv")