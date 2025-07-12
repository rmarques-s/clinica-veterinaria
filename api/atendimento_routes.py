from flask import Blueprint, request, jsonify
import services.atendimento_service as service

bp = Blueprint('atendimento', __name__)

@bp.route('/atendimentos', methods=['POST'])
def criar():
    atendimento = service.cadastrar_atendimento(request.json)
    return jsonify(atendimento.to_dict()), 201


@bp.route('/atendimentos', methods=['GET'])
def listar():
    return jsonify([a.to_dict() for a in service.obter_atendimentos()])