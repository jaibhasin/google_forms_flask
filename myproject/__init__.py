import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    forms = models.Form.query.all()
    return render_template('index.html', forms=forms)

@app.route('/create', methods=['GET', 'POST'])
def create_form():
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            form = models.Form(name=title)
            db.session.add(form)
            db.session.commit()
            return redirect(url_for('add_question', form_id=form.id))
    return render_template('create_form.html')

@app.route('/form/<int:form_id>/add_question', methods=['GET', 'POST'])
def add_question(form_id):
    form = models.Form.query.get_or_404(form_id)
    if request.method == 'POST':
        text = request.form.get('text')
        q_type = request.form.get('question_type', 'text')
        options = request.form.get('options')
        if text:
            question = models.Question(text=text, form_id=form.id, question_type=q_type)
            db.session.add(question)
            db.session.commit()
            if q_type == 'multiple' and options:
                for opt in options.split(','):
                    opt_text = opt.strip()
                    if opt_text:
                        db.session.add(models.Option(question_id=question.id, text=opt_text))
            db.session.commit()
            return redirect(url_for('add_question', form_id=form.id))
    return render_template('add_question.html', form=form)

@app.route('/form/<int:form_id>', methods=['GET', 'POST'])
def fill_form(form_id):
    form = models.Form.query.get_or_404(form_id)
    if request.method == 'POST':
        for question in form.questions:
            answer_text = request.form.get(f'q_{question.id}')
            if answer_text:
                answer = models.Answer(question_id=question.id, answer_text=answer_text)
                db.session.add(answer)
        db.session.commit()
        return redirect(url_for('thank_you'))
    return render_template('fill_form.html', form=form)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/form/<int:form_id>/results')
def form_results(form_id):
    form = models.Form.query.get_or_404(form_id)
    return render_template('results.html', form=form)

