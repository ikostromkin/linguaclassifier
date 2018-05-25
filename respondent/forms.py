from flask_wtf import FlaskForm
from wtforms import StringField


class AddRespondentForm(FlaskForm):
    field1 = StringField('Field1')
    field2 = StringField('Field2')
    field3 = StringField('Field3')
    field4 = StringField('Field4')
    field5 = StringField('Field5')
