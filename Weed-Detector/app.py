from flask import Flask,render_template,request
from pred import predictions

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/action1', methods=["GET","POST"])
def action1():
    return render_template("action1.html")

@app.route("/sub",methods=["GET","POST"])
def sub():
    if request.method=="POST":
        image=request.files['imagefile']
        image_path="static/"+image.filename
        image.save(image_path)
        pred,acc=predictions.prediction(path=image_path)
        acc=max(acc[0][0],acc[0][1])
        acc=acc*100
        acc=acc.item()
        acc=round(acc,3)

    return render_template('sub.html',img=image_path,n=pred,a=acc)

if __name__=="__main__":
    app.run()