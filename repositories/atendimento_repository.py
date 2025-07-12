from models.atendimento import Atendimento
from database import db

def criar_atendimento(descricao, pet_id, veterinario_id):
    novo = Atendimento(descricao=descricao, pet_id=pet_id, veterinario_id=veterinario_id)
    db.session.add(novo)
    db.session.commit()
    return novo

def listar_atendimentos():
    return Atendimento.query.all()