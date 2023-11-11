from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
app = Flask(__name__)
@app.route('/') 
def file(): 
    return render_template('resume.html')
    
@app.route('/upload', methods=['GET','POST']) 
def flk_up():     
    if request.method=='POST': 
        fl= request.files['file']        
        fl.save(secure_filename(fl.filename))         
        a=request.form.get('name')         
        b=request.form.get('dob')         
        c=request.form.get('email')        
        d=request.form.get('clg')         
        e=request.form.get('deg')         
        f=request.form.get('cgpa')         
        g=request.form.get('year')         
        h=request.form.get('lan') 
        return render_template("displayResume.html",a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,y=fl.filename) 
if __name__=='__main__':    
        app.run(debug = True) 

