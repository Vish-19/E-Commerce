from flask_wtf import FlaskForm
import email_validator
from wtforms import StringField, PasswordField, EmailField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, email_validator
from market.models import User, db
class RegistrationForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('UserName already exists! Please try a different UserName')
    def validate_email_address(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Email address already exists! please try a different email address')
    username = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
    email_address = EmailField(label='Email Address', validators=[Email() ,DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()]) 
    submit = SubmitField(label='Create account')
class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label='Login')
class Purchase_Item(FlaskForm):
    submit = SubmitField(label='Purchase Item')
class CartForm(FlaskForm):
    submit = SubmitField(label='Remove Item')
class SellForm(FlaskForm):
    name = StringField(label='Name', validators=[Length(min=2, max=30), DataRequired()])
    price = IntegerField(label="Price", validators=[DataRequired()])
    # barcode = IntegerField(label="Barcode", validators=[DataRequired()])
    description = StringField(label='Description')
    submit = SubmitField(label='Sell')
class AgreementForm(FlaskForm):
    submit = SubmitField(label="Agree")
class DisagreementForm(FlaskForm):
    submit = SubmitField(label="Disagree")