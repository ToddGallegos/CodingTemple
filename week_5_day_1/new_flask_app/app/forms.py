from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class PokemonCatcherForm(FlaskForm):
    pokemon_name = StringField("Pokemon Name", validators = [DataRequired()])
    submit = SubmitField()
    