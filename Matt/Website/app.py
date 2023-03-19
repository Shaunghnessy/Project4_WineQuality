from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper



# Create an instance of Flask
app = Flask(__name__)
app.config['WINE_IS_AWESOME'] = True

modelHelper = ModelHelper()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/works_cited")
def works_cited():
    return render_template("works_cited.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/data2")
def data2():
    return render_template("data2.html")

@app.route("/dashboard1")
def dashboard1():
    return render_template("dashboard1.html")

@app.route("/dashboard2")
def dashboard2():
    return render_template("dashboard2.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/wine_predictions", methods=["POST"])
def make_predictions():
    data = request.get_json()
    features = data['data']
    print(features)

    fixed_acidity = float(features['fixed_acidity'])
    residual_sugar = float(features['residual_sugar'])
    chlorides = float(features['chlorides'])
    volatile_acidity = float(features['volatile_acidity'])
    citric_acid = float(features['citric_acid'])
    free_sulfur_dioxide = float(features['free_sulfur_dioxide'])
    total_sulfur_dioxide = float(features['total_sulfur_dioxide'])
    density = float(features['density'])
    pH = float(features['pH'])
    sulphates = float(features['sulphates'])
    alcohol = float(features['alcohol'])

    prediction = modelHelper.predict(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol)
    return jsonify({'prediction': str(prediction)})

@app.route("/wine_predictions")
def wine_predictions():
    return render_template("/wine_predictions.html")

@app.route("/paper")
def paper():
    return render_template("paper.html")

#####################################################################
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)