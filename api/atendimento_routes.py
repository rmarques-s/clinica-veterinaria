from flask import Blueprint, request, jsonify
import services.atendimento_service as service

bp = Blueprint('atendimento', __name__)

@bp.route('/atendimentos', methods=['POST'])
def criar():
    return jsonify(service.cadastrar_atendimento(request.json)), 201

@bp.route('/atendimentos', methods=['GET'])
def listar():
    return jsonify([a.__dict__ for a in service.obter_atendimentos()])