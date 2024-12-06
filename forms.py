from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

# Registration Form
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    security_question1 = StringField('Security Question 1', validators=[DataRequired()])
    security_answer1 = StringField('Answer 1', validators=[DataRequired()])
    security_question2 = StringField('Security Question 2', validators=[DataRequired()])
    security_answer2 = StringField('Answer 2', validators=[DataRequired()])
    security_question3 = StringField('Security Question 3', validators=[DataRequired()])
    security_answer3 = StringField('Answer 3', validators=[DataRequired()])
    submit = SubmitField('Register')

# Login Form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Recovery Form
class RecoveryForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    answer1 = StringField('Answer 1', validators=[DataRequired()])
    answer2 = StringField('Answer 2', validators=[DataRequired()])
    answer3 = StringField('Answer 3', validators=[DataRequired()])
    submit = SubmitField('Recover')
