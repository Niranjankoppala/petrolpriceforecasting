from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("oil_price.pkl","rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("petrol.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        da=request.form["date"]
        day=int(pd.to_datetime(da, format="%Y-%m-%d").day)
        month=int(pd.to_datetime(da, format="%Y-%m-%d").month)
        year=int(pd.to_datetime(da, format="%Y-%m-%d").year)

        prediction=model.predict([[day,month,year]])
        output=round(prediction[0],2)
        return render_template('petrol.html',prediction_text="Petrol price is USD($). {}".format(output))
    return render_template("petrol.html")

if __name__ == "__main__":
    app.run(debug=True)