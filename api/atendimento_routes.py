from flask import Blueprint, request, jsonify
import services.atendimento_service as service

bp = Blueprint('atendimento', __name__)

@bp.route('/atendimentos', methods=['POST'])
def criar():
    """
    Cadastra um novo atendimento
    ---
    tags:
      - Atendimentos
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            descricao:
              type: string
              example: "Consulta de rotina e vacinação."
            pet_id:
              type: integer
              example: 1
            veterinario_id:
              type: integer
              example: 2
    responses:
      201:
        description: Atendimento criado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            data:
              type: string
            descricao:
              type: string
            pet_id:
              type: integer
            veterinario_id:
              type: integer
      400:
        description: Erro na requisição
    """
    atendimento = service.cadastrar_atendimento(request.json)
    return jsonify(atendimento.to_dict()), 201


@bp.route('/atendimentos', methods=['GET'])
def listar():
    """
    Lista todos os atendimentos
    ---
    tags:
      - Atendimentos
    responses:
      200:
        description: Lista de atendimentos
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
    return jsonify([a.to_dict() for a in service.obter_atendimentos()])