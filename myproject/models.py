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

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    question_type = db.Column(db.String(20), nullable=False, default='text')
    form_id = db.Column(db.Integer, db.ForeignKey('forms.id'), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy='dynamic')
    options = db.relationship('Option', backref='question', lazy='dynamic')

    def __init__(self, text, form_id, question_type='text'):
        self.text = text
        self.form_id = form_id
        self.question_type = question_type

class Option(db.Model):
    __tablename__ = 'options'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    text = db.Column(db.String(200), nullable=False)

    def __init__(self, question_id, text):
        self.question_id = question_id
        self.text = text

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer , primary_key=True)
    question_id = db.Column(db.Integer , db.ForeignKey('questions.id') , nullable=False)
    email = db.Column(db.String(120), nullable=False)
    answer_text = db.Column(db.String(200) , nullable=False)
    def __init__(self, question_id, answer_text, email):
        self.question_id = question_id
        self.answer_text = answer_text
        self.email = email
    
    def __repr__(self):
        return (
            f"Id : {self.id} , Question Id : {self.question_id} , "
            f"Email : {self.email} , Answer : {self.answer_text} "
        )

