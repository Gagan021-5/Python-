from flask import Flask
app = Flask(__name__)

@app.route("/wow")
def hello():
    return ("Hello this is backened of python!")

if __name__ == "__main__":
    app.run(debug=True)  