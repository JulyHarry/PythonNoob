import wtforms
from wtforms.validators import length, email, EqualTo


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=5, max=20)])
    nickname = wtforms.StringField(validators=[length(min=2, max=10)])
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=8, max=20)])
    passwordConfirm = wtforms.StringField(validators=[EqualTo("password")])

    def check_username(self, field):
        pass
