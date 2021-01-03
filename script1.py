from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
    # return "Website content goes here!"

@app.route('/about/')
def about():
    return render_template("about.html")

    # return "Website about content goes here!"

if __name__=="__main__":
    app.run(debug=True)