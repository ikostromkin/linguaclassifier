from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


def validate_fields_list(form, field):
    if not field.data:
        raise ValidationError('Введите названия полей')
    fields_list = field.data.split(' ')
    fields_list = list(filter(None, fields_list))
    if len(fields_list) > 5:
        raise ValidationError('Слишком много полей, максимум 5')


class AddResearchForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    material = TextAreaField('Material', validators=[DataRequired()])
    task = TextAreaField('Task', validators=[DataRequired()])
    fields = StringField('Fields', validators=[validate_fields_list])



