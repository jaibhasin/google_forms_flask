from myproject import db

class Form(db.Model):
    __tablename__ = 'forms' 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50) , nullable=False)
    questions = db.relationship('Question', backref='form', lazy='dynamic')
    def __init__(self, name):
        self.title = name
    
    def __repr__(self):
        return (f"Id : {self.id} , Title : {self.title} ")

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer , primary_key=True)
    text = db.Column(db.String(200) , nullable=False)
    form_id = db.Column(db.Integer, db.ForeignKey('forms.id'), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy='dynamic')

    def __init__(self, text, form_id):
        self.text = text
        self.form_id = form_id

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer , primary_key=True)
    question_id = db.Column(db.Integer , db.ForeignKey('questions.id') , nullable=False)
    answer_text = db.Column(db.String(200) , nullable=False)
    def __init__(self, question_id, answer_text):
        self.question_id = question_id
        self.answer_text = answer_text
    
    def __repr__(self):        return f"Id : {self.id} , Question Id : {self.question_id} , Answer : {self.answer_text} "

