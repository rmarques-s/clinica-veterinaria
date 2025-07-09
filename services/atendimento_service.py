import repositories.atendimento_repository as repo

def cadastrar_atendimento(data):
    return repo.criar_atendimento(data['data'], data['descricao'], data['pet_id'], data['veterinario_id'])

def obter_atendimentos():
    return repo.listar_atendimentos()