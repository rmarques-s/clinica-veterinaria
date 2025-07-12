from flask import Blueprint, request, jsonify
import services.veterinario_service as service

bp = Blueprint('veterinario', __name__)

@bp.route('/veterinarios', methods=['POST'])
def criar():
    veterinario = service.cadastrar_veterinario(request.json)
    return jsonify(veterinario.to_dict()), 201

@bp.route('/veterinarios', methods=['GET'])
def listar():
    return jsonify([v.to_dict() for v in service.obter_veterinarios()])

@bp.route('/veterinarios/<int:id>/atendimentos', methods=['GET'])
def atendimentos(id):
    return jsonify([a.to_dict() for a in service.obter_atendimentos_do_veterinario(id)])