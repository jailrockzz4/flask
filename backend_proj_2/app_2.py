from flask import Flask,render_template,request
app=Flask(__name__)

notes=[]
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/note",methods=["GET","POST"])
def note():
    note=request.form.get("note")
    if note and note.strip():
        notes.append(note)
    return render_template("output.html",notes=notes)


if __name__=="__main__":
    app.run(debug=True)