import repositories.tutor_repository as repo

def cadastrar_tutor(data):
    return repo.criar_tutor(data['nome'], data['telefone'])

def obter_pets_do_tutor(id):
    return repo.buscar_pets_do_tutor(id)