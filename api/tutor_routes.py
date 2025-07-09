from flask import Blueprint, request, jsonify
import services.tutor_service as service

bp = Blueprint('tutor', __name__)

@bp.route('/tutores', methods=['POST'])
def criar():
    return jsonify(service.cadastrar_tutor(request.json)), 201

@bp.route('/tutores/<int:id>/pets', methods=['GET'])
def pets(id):
    return jsonify([p.__dict__ for p in service.obter_pets_do_tutor(id)])