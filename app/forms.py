from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, IntegerField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User

class SubmitTextForm(FlaskForm):
    text = TextAreaField('Text to Summarize')
    submit = SubmitField('Summarize')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Register')

    # Custom email validation to check if email already exists
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already registered. Please choose a different email.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
