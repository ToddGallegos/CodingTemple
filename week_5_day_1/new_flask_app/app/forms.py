from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class PokemonCatcherForm(FlaskForm):
    pokemon_name = StringField("Pokemon Name", validators = [DataRequired()])
    submit = SubmitField()
    
class SignUpForm(FlaskForm):
    user_name = StringField("User Name", validators= [DataRequired()])
    email = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    first_name = StringField("First Name", validators= [DataRequired()])
    last_name = StringField("Last Name", validators= [DataRequired()])
    submit = SubmitField()
    
class SignInForm(FlaskForm):
    user_name = StringField("User Name", validators= [DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField()