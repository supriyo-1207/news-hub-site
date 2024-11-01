from functools import wraps
from flask import flash, redirect, session, url_for


def set_user_session(user):
    session['user'] = user
    session['is_logged_in'] = True
    session['active'] = True
    return True

def destroy_user_session():
    session['user'] = None
    session['is_logged_in'] = False
    session['active'] = False
    session.clear()
    return True


def dec_fun():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'user' in session and session.get('is_logged_in'):
                return func(*args, **kwargs)
            else:
                flash('You need to be logged in to access this page.', 'error')
                return redirect(url_for('auth.login'))
        return wrapper
    return decorator
