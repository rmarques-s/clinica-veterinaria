from flask import Blueprint, request, jsonify
import services.veterinario_service as service

bp = Blueprint('veterinario', __name__)

@bp.route('/veterinarios', methods=['POST'])
def criar():
    """
    Cadastra um novo tutor
    ---
    tags:
      - Tutores
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - nome
            - telefone
          properties:
            nome:
              type: string
            telefone:
              type: string
    responses:
      201:
        description: Tutor cadastrado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            nome:
              type: string
            telefone:
              type: string
    """

    veterinario = service.cadastrar_veterinario(request.json)
    return jsonify(veterinario.to_dict()), 201

@bp.route('/veterinarios', methods=['GET'])
def listar():
    """
    Lista todos os veterinários
    ---
    tags:
      - Veterinários
    responses:
      200:
        description: Lista de veterinários
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
    """
    return jsonify([v.to_dict() for v in service.obter_veterinarios()])

@bp.route('/veterinarios/<int:id>/atendimentos', methods=['GET'])
def atendimentos(id):
    """
    Lista os atendimentos realizados por um veterinário específico
    ---
    tags:
      - Veterinários
    parameters:
      - name: id
        in: path
        required: true
        description: ID do veterinário
        schema:
          type: integer
    responses:
      200:
        description: Lista de atendimentos do veterinário
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  data:
                    type: string
                    format: date-time
                  descricao:
                    type: string
                  pet_id:
                    type: integer
                  veterinario_id:
                    type: integer
    """
    return jsonify([a.to_dict() for a in service.obter_atendimentos_do_veterinario(id)])