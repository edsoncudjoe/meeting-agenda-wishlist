from flask_wtf import Form
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp

regex_string = '^[A-Za-z0-9 ]{3,}$'
regex_err = "Messages must consist of letters, numbers and spaces."


class TopicForm(Form):
    message = TextAreaField('Message: ', validators=[DataRequired(),
                                                     Length(1, 8192)])
