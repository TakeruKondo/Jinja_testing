from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator


class contactForm(FlaskForm):
    name = StringField(label='お名前',validators=[DataRequired()])
    email = StringField(label='メールl', validators=[
      DataRequired(), Email(granular_message=True)])
    message= StringField(label='内容')
    submit = SubmitField(label='送信')