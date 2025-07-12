from flask import Blueprint, request, jsonify
import services.pet_service as service

bp = Blueprint('pet', __name__)

@bp.route('/pets', methods=['POST'])
def criar():
    """
    Cadastra um novo pet
    ---
    tags:
      - Pets
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - nome
            - especie
            - idade
            - tutor_id
          properties:
            nome:
              type: string
            especie:
              type: string
            idade:
              type: integer
            tutor_id:
              type: integer
    responses:
      201:
        description: Pet cadastrado com sucesso
        schema:
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
    """

    pet = service.cadastrar_pet(request.json)
    return jsonify(pet.to_dict()), 201


@bp.route('/pets', methods=['GET'])
def listar():
    """
    Lista todos os pets cadastrados
    ---
    tags:
      - Pets
    responses:
      200:
        description: Lista de pets
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
    """
    return jsonify([p.to_dict() for p in service.obter_pets()])


@bp.route('/pets/<int:id>/atendimentos', methods=['GET'])
def atendimentos(id):
    """
    Lista os atendimentos de um pet específico
    ---
    tags:
      - Pets
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
        description: ID do pet
    responses:
      200:
        description: Lista de atendimentos do pet
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
      404:
        description: Pet não encontrado ou sem atendimentos
    """
    return jsonify([a.to_dict() for a in service.obter_atendimentos_do_pet(id)])
