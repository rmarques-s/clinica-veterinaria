from models.tutor import Tutor
from database import db

def criar_tutor(nome, telefone):
    novo = Tutor(nome=nome, telefone=telefone)
    db.session.add(novo)
    db.session.commit()
    return novo

def buscar_pets_do_tutor(tutor_id):
    tutor = Tutor.query.get(tutor_id)
    return tutor.pets if tutor else None