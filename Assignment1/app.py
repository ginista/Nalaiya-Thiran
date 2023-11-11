from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')
@app.route('/login',methods=["POST"])
def login():
    if request.method=="POST":
        uname = request.form["uname"]
        email = request.form["email"]
        phone = request.form["phone"]
        return render_template("app1.html",username=uname,email=email,phone=phone)

if __name__ =='__main__':
    app.run(debug = True)