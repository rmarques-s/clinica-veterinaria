from database import db

class Veterinario(db.Model):
    __tablename__ = 'veterinarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)

    clinica_id = db.Column(db.Integer, db.ForeignKey('clinicas.id'), nullable=False)
    clinica = db.relationship('Clinica', back_populates='veterinarios')

    atendimentos = db.relationship('Atendimento', back_populates='veterinario', cascade='all, delete-orphan')