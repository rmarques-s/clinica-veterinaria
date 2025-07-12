from flask import Blueprint, request, jsonify
import services.pet_service as service

bp = Blueprint('pet', __name__)

@bp.route('/pets', methods=['POST'])
def criar():
    pet = service.cadastrar_pet(request.json)
    return jsonify(pet.to_dict()), 201


@bp.route('/pets', methods=['GET'])
def listar():
    return jsonify([p.to_dict() for p in service.obter_pets()])


@bp.route('/pets/<int:id>/atendimentos', methods=['GET'])
def atendimentos(id):
    return jsonify([a.to_dict() for a in service.obter_atendimentos_do_pet(id)])
