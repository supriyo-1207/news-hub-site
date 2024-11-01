from flask import (
    Flask,Blueprint,render_template,request,redirect,url_for,flash,session
)

from model.auth_model import Auth
from database.db_connection import db
from extensions import bcrypt
from utility_function.utility import dec_fun, destroy_user_session, set_user_session
auth=Blueprint('auth',__name__)




# register page----------------------------------------------------
@auth.route('/register')
def get_register():
    return render_template('register.html',title='Register Page')





@auth.route('/register',methods=['POST'])
def register():
    
    form_data = request.get_json()
    print("form_data",form_data)

    name = form_data['name']
    email = form_data['email']
    password = form_data['password'].strip()
    print(name,email,password)
    # Validate user input
    if not name or not email or not password:
        flash('Please fill in all fields.', 'error')
        return redirect(url_for('auth.register'))
    # valid email

    # Check if user already exists
    user_exists=Auth.query.filter_by(email=email).first()
    if  user_exists:
        flash('User alreay exists, please login','error')
        return redirect(url_for('auth.register'))
        
    # hased password
    hash_password=bcrypt.generate_password_hash(password).decode('utf-8')
    print("hash_password",hash_password)

    new_auth = Auth(name=name, email=email, password=hash_password)
    # Add and commit to the database
    db.session.add(new_auth)
    db.session.commit()
    flash('Registration successful.', 'success')
    return {'message':'Registration successful.', 'status':200}


    




# login page----------------------------------------------------------------


@auth.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        form_data=request.get_json()
         
        email = form_data['email']
        password = form_data['password'].strip()
        print(email,password)
        # Validate user input
        if not email or not password:
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('auth.login'))
        
        # check if user exists
        check_user=Auth.query.filter_by(email=email).first()
        if not check_user:
            flash('User does not exist, please register','error')
            return redirect(url_for('auth.login'))
        # check if password is correct
        print("check_user",check_user.password)
        check_password=bcrypt.check_password_hash(check_user.password,password)
        print("check_password",check_password)
        if not check_password:
            flash('Incorrect password','error')
            return {'message':'Registration successful.', 'status':200}
        else:
            set_user_session(check_user.email)
            flash('Login successful','success')
            return {'message':'Registration successful.', 'status':200}


    return render_template('login.html',title='Login Page')




# logout page ---------------------------------------------------------------


@auth.route('/logout')
@dec_fun()
def logout():
    destroy_user_session()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))
    
