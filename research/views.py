from flask import Blueprint, render_template, redirect, url_for, send_file
from flask_login import login_required, current_user
from .forms import AddResearchForm
from models import *
from .process import create_report

research_blueprint = Blueprint('research', __name__)


@research_blueprint.route('/all/')
@login_required
def all_research():
    researches = Researches.select().where(Researches.owner == current_user.id).dicts()
    for research in researches:
        respondents = Respondents.select().where(
            (Respondents.owner == research['id']) & (Respondents.filled_all == True)).dicts()
        research['count'] = len(respondents)
    return render_template('all_research.html', researches=researches)


@research_blueprint.route('/add/', methods=('GET', 'POST'))
@login_required
def add_research():
    form = AddResearchForm()
    if form.validate_on_submit():
        new_research = Researches(
            owner=current_user.id,
            name=form.name.data,
            material=form.material.data,
            task=form.task.data,
            fields=form.fields.data
        )
        new_research.save()
        return redirect(url_for('research.all_research'))
    return render_template('add_research.html', form=form)


# @research_blueprint.route('/<int:id>')
# @login_required
# def research(id):
#     return 'Страница исследования с id= ' + str(id)


@research_blueprint.route('/<int:id>/download')
@login_required
def download(id):
    create_report(id)
    return send_file('temp.xlsx')
