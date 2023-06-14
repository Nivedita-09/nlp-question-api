from flask import Flask, request
import pickle 
from helper import query_point_creator

# import nltk




app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
# def download_nltk_resources():
#     nltk.download('stopwords', quiet=True, halt_on_error=True, )
#     print("its done")

# # Call the function to download NLTK resources before running the Flask server
# download_nltk_resources()

@app.route("/" , methods=["GET","POST"])
def getQuestions():
    q1= request.form.get("Question1")
    q2 = request.form.get("Question2")
    query = query_point_creator(q1,q2)
    result = model.predict(query)[0]
    if result:
        return 'Duplicate'
    else:
        return 'Not Duplicate'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)