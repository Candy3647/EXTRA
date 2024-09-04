from flask import Flask
from flask import render_template, request
import pyodbc
app = Flask(__name__)
# Home page
@app.route("/")
def home():
        print('Loading Home page')
        return render_template("/index.html")
# Form page
@app.route("/register", methods=["GET", "POST"])
def form():
        con=('Driver={SQL Server};' 'Server=.;' 'Database=master;' 'Trusted_connection=yes;')
        conn=pyodbc.connect(con)
        cursor=conn.cursor()
        print("creating a new table")
        print('Loading Registration page')
        if request.method == "POST":
                Name = request.form["name"]
                Email = request.form["email"]
                Comments = request.form["message"]
                Number = request.form["number"]
                cursor.execute("create table customerdata (Username varchar(20),Email varchar(30),Phonenumber varchar(15),Comment varchar(150))")
                conn.commit()
                cursor.execute("insert into customerdata values(?,?,?,?)",(Name,Email,Number,Comments))
                conn.commit()
                conn.close()
                print("information has inserted successfully")
                return render_template('regsuccess.html',name=Name,email=Email,number=Number)
        else:
                Name = request.args.get("name")
                Email = request.args.get("email")
                Comments = request.args.get("message")
                Number = request.args.get("number")
                return render_template('regsuccess.html',name=Name,email=Email,number=Number)

if __name__ == "__main__":
        app.run(debug=True)
        print('Web service Started')
else:
        print('Web service Stopped')
