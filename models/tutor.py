from database import db

class Tutor(db.Model):
    __tablename__ = 'tutores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    pets = db.relationship('Pet', back_populates='tutor', cascade='all, delete-orphan')