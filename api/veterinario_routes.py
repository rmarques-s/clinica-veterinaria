from flask import Blueprint, request, jsonify
import services.veterinario_service as service

bp = Blueprint('veterinario', __name__)

@bp.route('/veterinarios', methods=['POST'])
def criar():
    return jsonify(service.cadastrar_veterinario(request.json)), 201

@bp.route('/veterinarios', methods=['GET'])
def listar():
    return jsonify([v.__dict__ for v in service.obter_veterinarios()])

@bp.route('/veterinarios/<int:id>/atendimentos', methods=['GET'])
def atendimentos(id):
    return jsonify([a.__dict__ for a in service.obter_atendimentos_do_veterinario(id)])