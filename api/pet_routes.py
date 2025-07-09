from flask import Blueprint, request, jsonify
import services.pet_service as service

bp = Blueprint('pet', __name__)

@bp.route('/pets', methods=['POST'])
def criar():
    return jsonify(service.cadastrar_pet(request.json)), 201

@bp.route('/pets', methods=['GET'])
def listar():
    return jsonify([p.__dict__ for p in service.obter_pets()])

@bp.route('/pets/<int:id>/atendimentos', methods=['GET'])
def atendimentos(id):
    return jsonify([a.__dict__ for a in service.obter_atendimentos_do_pet(id)])