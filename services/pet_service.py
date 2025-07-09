import repositories.pet_repository as repo

def cadastrar_pet(data):
    return repo.criar_pet(data['nome'], data['especie'], data['idade'], data['tutor_id'])

def obter_pets():
    return repo.listar_pets()

def obter_atendimentos_do_pet(id):
    return repo.buscar_atendimentos_do_pet(id)