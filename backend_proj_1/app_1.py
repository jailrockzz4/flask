from flask import Flask, render_template, request
import re

app = Flask(__name__)

#############################

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def matches():
    regex = request.form["regex"]
    target = request.form["target"]
    find = re.findall(regex,target)
    return render_template("output.html",finds=find)

##############################

if __name__ == '__main__':
    app.run(debug=True)


