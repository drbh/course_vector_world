
from flask import Flask, make_response, current_app, request
import pandas as pd

df = pd.read_csv("./topn.csv")

app = Flask(__name__)

def two_level_unwind(cls):
    focal = df.query("source == @cls")
    unique_second_level = list(set(focal.target.tolist()))
    vals = [df.query("source == @u") for u in unique_second_level]
    return pd.concat([focal, pd.concat(vals)])

@app.route('/data')
def data():
    course = request.args.get('course')
    frame = two_level_unwind(course)
    resp = make_response(frame.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@app.route('/')
def hello():
    print("yo")
    return current_app.send_static_file('graph.html')

if __name__ == '__main__':
    app.run()