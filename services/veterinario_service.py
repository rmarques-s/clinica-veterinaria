import repositories.veterinario_repository as repo

def cadastrar_veterinario(data):
    return repo.criar_veterinario(data['nome'], data['especialidade'], data['clinica_id'])

def obter_veterinarios():
    return repo.listar_veterinarios()

def obter_atendimentos_do_veterinario(id):
    return repo.buscar_atendimentos_do_veterinario(id)