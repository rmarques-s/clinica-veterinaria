from flask import Blueprint, request, jsonify
import services.clinica_service as service

bp = Blueprint('clinica', __name__)

@bp.route('/clinicas', methods=['POST'])
def criar():
    return jsonify(service.cadastrar_clinica(request.json)), 201

@bp.route('/clinicas', methods=['GET'])
def listar():
    return jsonify([c.__dict__ for c in service.obter_clinicas()])

@bp.route('/clinicas/<int:id>', methods=['GET'])
def buscar(id):
    c = service.obter_clinica(id)
    return jsonify(c.__dict__) if c else ('', 404)

@bp.route('/clinicas/<int:id>/veterinarios', methods=['GET'])
def veterinarios(id):
    return jsonify([v.__dict__ for v in service.obter_veterinarios_da_clinica(id)])