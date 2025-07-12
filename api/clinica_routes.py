from flask import Blueprint, request, jsonify
import services.clinica_service as service

bp = Blueprint('clinica', __name__)

@bp.route('/clinicas', methods=['POST'])
def criar():
    """
    Cadastra uma nova clínica
    ---
    tags:
      - Clínicas
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: Clínica São Francisco
            cidade:
              type: string
              example: São Paulo
    responses:
      201:
        description: Clínica criada com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            nome:
              type: string
            cidade:
              type: string
      400:
        description: Dados inválidos
    """

    data = request.get_json()
    nome = data['nome']
    cidade = data['cidade']
    clinica = service.cadastrar_clinica(nome, cidade)
    return jsonify(clinica.to_dict()), 201

@bp.route('/clinicas', methods=['GET'])
def listar():
    """
    Lista todas as clínicas
    ---
    tags:
      - Clínicas
    responses:
      200:
        description: Lista de clínicas cadastradas
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  nome:
                    type: string
                  cidade:
                    type: string
    """
    return jsonify([c.to_dict() for c in service.obter_clinicas()])

@bp.route('/clinicas/<int:id>', methods=['GET'])
def buscar(id):
    """
    Busca uma clínica pelo ID
    ---
    tags:
      - Clínicas
    parameters:
      - in: path
        name: id
        schema:
          type: integer
        required: true
        description: ID da clínica
    responses:
      200:
        description: Clínica encontrada
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                nome:
                  type: string
                cidade:
                  type: string
      404:
        description: Clínica não encontrada
    """
    c = service.obter_clinica(id)
    return jsonify(c.to_dict()) if c else ('', 404)

@bp.route('/clinicas/<int:id>/veterinarios', methods=['GET'])
def veterinarios(id):
    """
    Lista os veterinários de uma clínica
    ---
    tags:
      - Clínicas
    parameters:
      - in: path
        name: id
        schema:
          type: integer
        required: true
        description: ID da clínica
    responses:
      200:
        description: Lista de veterinários da clínica
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  nome:
                    type: string
                  especialidade:
                    type: string
                  clinica_id:
                    type: integer
      404:
        description: Clínica não encontrada ou sem veterinários
    """
    return jsonify([v.to_dict() for v in service.obter_veterinarios_da_clinica(id)])