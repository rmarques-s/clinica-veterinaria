import repositories.clinica_repository as repo

def cadastrar_clinica(nome, cidade):
    return repo.criar_clinica(nome, cidade)

def obter_clinicas():
    return repo.listar_clinicas()

def obter_clinica(id):
    return repo.buscar_clinica_por_id(id)

def obter_veterinarios_da_clinica(id):
    return repo.listar_veterinarios_da_clinica(id)