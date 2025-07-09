from database import db
from datetime import datetime

class Atendimento(db.Model):
    __tablename__ = 'atendimentos'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    descricao = db.Column(db.Text, nullable=False)

    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'), nullable=False)
    pet = db.relationship('Pet', back_populates='atendimentos')

    veterinario_id = db.Column(db.Integer, db.ForeignKey('veterinarios.id'), nullable=False)
    veterinario = db.relationship('Veterinario', back_populates='atendimentos')