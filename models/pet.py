from database import db

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    tutor_id = db.Column(db.Integer, db.ForeignKey('tutores.id'), nullable=False)
    tutor = db.relationship('Tutor', back_populates='pets')

    atendimentos = db.relationship('Atendimento', back_populates='pet', cascade='all, delete-orphan')