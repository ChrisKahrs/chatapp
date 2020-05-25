from flask import Flask, render_template
from models import *

from wtforms_fields import *

app = Flask(__name__)
app.secret_key = 'replace later'

app.config['SQLALCHEMY_DATABASE_URI']='postgres://intwywydeknqcl:2f8af4fee69c19a90d03596a20a4cc7709f01842b13bb6d0d12177b6a8ea5f81@ec2-52-44-166-58.compute-1.amazonaws.com:5432/dfebf1qn1vjpl'
db = SQLAlchemy(app)


@app.route("/", methods=['GET','POST'])
def index():

    reg_form = RegistrationForm()   
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # check if username exists2233
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "Someone else has this username!"

        # add user
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB!"

    return render_template('index.html', form=reg_form)

if __name__ == "__main__":
    app.run(debug=True)