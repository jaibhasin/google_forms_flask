from myproject import db

class Form(db.Model):
    __tablename__ = 'forms'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50) , nullable=False)
    is_public = db.Column(db.Boolean, nullable=False, default=False)
    questions = db.relationship(
        'Question', backref='form', lazy='dynamic', cascade='all, delete-orphan'
    )
    def __init__(self, name, is_public=False):
        """
        Initialize a new form with optional public visibility.

        :param name: Title of the form
        :param is_public: Whether the form is publicly visible (default: False)
        """
        self.title = name
        self.is_public = is_public

    def __repr__(self):
        """
        Provide a string representation of the form, including visibility status.

        :return: Descriptive string of form details
        """
        visibility = "Public" if self.is_public else "Private"
        return (f"Id: {self.id}, Title: {self.title}, Visibility: {visibility}")

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    question_type = db.Column(db.String(20), nullable=False, default='text')
    form_id = db.Column(db.Integer, db.ForeignKey('forms.id'), nullable=False)
    is_required = db.Column(db.Boolean, nullable=False, default=True)
    answers = db.relationship(
        'Answer', backref='question', lazy='dynamic', cascade='all, delete-orphan'
    )
    options = db.relationship(
        'Option', backref='question', lazy='dynamic', cascade='all, delete-orphan'
    )

    def __init__(self, text, form_id, question_type='text', is_required=True):
        self.text = text
        self.form_id = form_id
        self.question_type = question_type
        self.is_required = is_required

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

