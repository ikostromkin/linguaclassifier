from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import AddRespondentForm
from models import *


respondent_blueprint = Blueprint('respondent', __name__)


@respondent_blueprint.route('/add/<int:research_id>', methods=('GET', 'POST'))
def add_respondent(research_id):
    form = AddRespondentForm()
    if form.validate_on_submit():
        new_respondent = Respondents(
            owner=research_id,
            field1=form.field1.data,
            field2=form.field2.data,
            field3=form.field3.data,
            field4=form.field4.data,
            field5=form.field5.data,
        )
        new_respondent.save()
        return redirect(url_for('group.add_group', research_id=research_id, respondent_id=new_respondent.id))
    try:
        research = Researches.get(id=research_id)
        if research:
            fields = research.fields.split(' ')
            fields = list(filter(None, fields))
            count = len(fields)
            return render_template('add_respondent.html', form=form, fields=fields, count=count, research_id=research_id)
    except DoesNotExist:
        return redirect(url_for('index'))


@respondent_blueprint.route('/end/<int:id>')
def end(id):
    try:
        full_respondent = Respondents.get(id=id)
        if full_respondent:
            full_respondent.filled_all = True
            full_respondent.save()
            return 'Успех, исследование завершено!'
    except DoesNotExist:
        return redirect(url_for('index'))


@respondent_blueprint.route('/<int:id>')
@login_required
def respondent(id):
    return 'Страница респондента с id= ' + str(id)

