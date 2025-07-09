from models.veterinario import Veterinario
from database import db

def criar_veterinario(nome, especialidade, clinica_id):
    novo = Veterinario(nome=nome, especialidade=especialidade, clinica_id=clinica_id)
    db.session.add(novo)
    db.session.commit()
    return novo

def listar_veterinarios():
    return Veterinario.query.all()

def buscar_atendimentos_do_veterinario(veterinario_id):
    vet = Veterinario.query.get(veterinario_id)
    return vet.atendimentos if vet else None