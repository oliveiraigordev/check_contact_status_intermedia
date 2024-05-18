from flask import Blueprint, jsonify, request
from src.errors.error_controller import handle_errors
from src.main.factories.company_factory import (
    create_company_factory,
    update_company_factory
)


company_bp = Blueprint('company', __name__)


@company_bp.post('/company')
def create_company():
    try:
        data = request.json
        create_company_factory(data)
        return jsonify(
            {"message": "Empresa cadastrada com sucesso!"}, 201
        )
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response['status_code']


@company_bp.put('/company/<int:company_id>')
def update_company(company_id):
    try:
        data = request.json
        update_company_factory(data, company_id)
        return jsonify(
            {"message": "Empresa atualizada com sucesso!"}, 200
        )
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response['status_code']
