from flask import Flask, render_template, redirect

# Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/works_cited")
def works_cited():
    return render_template("works_cited.html")

@app.route("/data")
def data():
    return render_template("data.html")














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