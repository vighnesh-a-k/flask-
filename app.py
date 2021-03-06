from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"]="sqlite:///test.db"
db=SQLAlchemy(app)




class todo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(200))
    completed=db.Column(db.Integer,default=0)
   
    def __init__(self, c="gava"):
        self.content=c

    def __repr__(self):
        return '<Task %r>' % self.id
db.create_all()


@app.route("/",methods=["POST","GET"])
def index():
    if request.method=="POST":
        task_content=request.form["content"]
        newtask=todo(task_content)
        
        print(task_content)
        try:
            db.session.add(newtask)
            db.session.commit()
            return redirect("/")
        except:
            return "error"
         

    else:
        task=todo.query.order_by(todo.id).all()

        return render_template('index.html',tasks=task)

@app.route("/delete/<int:id>")
def delete(id):
    task_del=todo.query.get(id)
    
    try:
        db.session.delete(task_del)
        db.session.commit()
        return redirect("/")
    except:
        return("oops")






if __name__=="__main__":
    app.run(debug=True)






