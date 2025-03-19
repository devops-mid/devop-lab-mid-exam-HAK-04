from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User
import re

EMAIL_REGEX = r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"
PHONE_REGEX = r"^\d{10}$"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone', '')  # Optional field
    age = request.form.get('age', None)

    if not re.match(EMAIL_REGEX, email):
        flash("Invalid email address format. Please enter a valid email address.", "error")
        return redirect(url_for('index'))

    if phone and not re.match(PHONE_REGEX, phone):
        flash("Invalid phone number. It must contain exactly 10 digits.", "error")
        return redirect(url_for('index'))

    user = User(name=name, email=email, phone=phone, age=age)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
