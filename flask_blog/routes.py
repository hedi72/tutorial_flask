from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm

# Import models after creating the db instance
from flask_blog.models import User, Post

# dummy data
posts = [
    {
        'author': 'Rohit',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'hedi',
        'title': 'Blog Post 2',
        'content': 'Hello Hadhoud, I am very proud of your progress. Please continue to learn and grow, as you are on the right path.',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Your form submission handling code here
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    else:
        # Flash each validation error separately
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field.capitalize()}: {error}', 'danger')
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'hedi@gmail.com' and form.password.data == 'password':
            flash(
                f'You have been logged in welcome {form.email.data} ', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', title='login', form=form)


@app.route('/forget_password')
def forget_password():
    return render_template('forget_password.html', title='Forget password')

