from flask import Blueprint, request, jsonify
import services.tutor_service as service

bp = Blueprint('tutor', __name__)

@bp.route('/tutores', methods=['POST'])
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

    tutor = service.cadastrar_tutor(request.json)
    return jsonify(tutor.to_dict()), 201


@bp.route('/tutores/<int:id>/pets', methods=['GET'])
def pets(id):
    """
    Lista todos os pets de um tutor específico
    ---
    tags:
      - Tutores
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
        description: ID do tutor
    responses:
      200:
        description: Lista de pets do tutor
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
                  especie:
                    type: string
                  idade:
                    type: integer
                  tutor_id:
                    type: integer
      404:
        description: Tutor não encontrado ou sem pets
    """
    return jsonify([p.to_dict() for p in service.obter_pets_do_tutor(id)])
