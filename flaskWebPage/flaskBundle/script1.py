from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # File home.html should be under templates folder
    return render_template("home.html")

@app.route('/about')
def about():
    return "I am a coold app"

# name will be main if you run this script directly
# it will be script1 if you import this library somewhere else
if __name__ == "__main__":
    app.run(debug = True)