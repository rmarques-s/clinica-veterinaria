from models.clinica import Clinica
from database import db

def criar_clinica(nome, cidade):
    nova = Clinica(nome=nome, cidade=cidade)
    db.session.add(nova)
    db.session.commit()
    return nova

def listar_clinicas():
    return Clinica.query.all()

def buscar_clinica_por_id(clinica_id):
    return Clinica.query.get(clinica_id)

def listar_veterinarios_da_clinica(clinica_id):
    clinica = Clinica.query.get(clinica_id)
    return clinica.veterinarios if clinica else None

def deletar_clinica(clinica_id):
    clinica = Clinica.query.get(clinica_id)
    if clinica:
        db.session.delete(clinica)
        db.session.commit()
        return True
    return False