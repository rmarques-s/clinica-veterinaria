from models.pet import Pet
from database import db

def criar_pet(nome, especie, idade, tutor_id):
    novo = Pet(nome=nome, especie=especie, idade=idade, tutor_id=tutor_id)
    db.session.add(novo)
    db.session.commit()
    return novo

def listar_pets():
    return Pet.query.all()

def buscar_atendimentos_do_pet(pet_id):
    pet = Pet.query.get(pet_id)
    return pet.atendimentos if pet else None