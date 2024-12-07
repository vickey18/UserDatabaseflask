from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Configure the app to use a MySQL database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123%21%40%23qweQWE@localhost/users"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Corrected key name
db = SQLAlchemy(app)


class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(500),nullable=False)
    roll=db.Column(db.String(500),nullable=False)


#---------------Hello route---------------
@app.route("/hello")
def hello():
    #----Inserting sample data in users table----
    id =234
    name='vivek'
    email="sdfasdfdfs"
    roll="sdfasdfdfs"
    user=Users(id=id, name=name, email=email,roll=roll)
    db.session.add(user)
    db.session.commit()
    return "hello world"


#-------API route for getting all users details----

@app.route("/users" , methods={"GET","POST"})
def users():
    if request.method=='POST':
        id=request.form["query"]
        return redirect(f"/users/{id}")
    allUsers=Users.query.all()
    return render_template('users.html', users=allUsers)


#---------Home Page
@app.route("/")
def home():
    return render_template("index.html")




#----API route to get specific user---------------
@app.route("/users/<int:id>")
def get_user_by_id(id):
    # Query the database to find the user by ID
    user = Users.query.get(id)
    
    if user:
        # If user is found, render a template with the user details
        return render_template('user_info.html', user=user)
    else:
        # If no user is found, return an error message
        return render_template('user_info.html', user="not found")




# API route for adding new user details
@app.route("/new_user", methods={"GET","POST"})
def new_user():
    if request.method=='POST':
        id =request.form['id']
        name=request.form['name']
        email=request.form['email']
        roll=request.form['roll']
        user=Users(id=id, name=name, email=email,roll=roll)
        db.session.add(user)
        db.session.commit()
        return redirect("/users")
    allUsers=Users.query.all()
    return render_template('input_form.html')


if __name__ == "__main__":
    app.run(debug=True,port=8000)