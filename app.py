from flask import Flask, request
import pickle 
from helper import query_point_creator



model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route("/")
def Main():
    q1= request.form.get("Question1")
    q2 = request.form.get("Question2")
    query = query_point_creator(q1,q2)
    result = model.predict(query)[0]
    if result:
        return 'Duplicate'
    else:
        return 'Not Duplicate'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)