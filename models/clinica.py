from database import db

class Clinica(db.Model):
    __tablename__ = 'clinicas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)

    veterinarios = db.relationship('Veterinario', back_populates='clinica', cascade='all, delete-orphan')