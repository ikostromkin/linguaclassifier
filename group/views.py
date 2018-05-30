from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from werkzeug.datastructures import MultiDict

from models import *

group_blueprint = Blueprint('group', __name__)


@group_blueprint.route('/add/<int:research_id>/<int:respondent_id>', methods=('GET', 'POST'))
def add_group(research_id, respondent_id):
    if request.method == "GET":
        try:
            researche = Researches.get(id=research_id)
            if researche:
                material = []
                for word in researche.material.split(' '):
                    material.append(word)

                return render_template('add_group.html', material=material, research_id=research_id,
                                       respondent_id=respondent_id, task=researche.task)
        except DoesNotExist:
            return redirect(url_for('index'))
    if request.method == "POST":
        r = MultiDict(request.form)
        new_group = Groups(
            owner=respondent_id,
            name=request.form['name'],
            elements=' '.join(r.getlist('check'))
        )
        new_group.save()
        return jsonify()
