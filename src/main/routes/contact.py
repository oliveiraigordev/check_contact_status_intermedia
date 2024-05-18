from flask import Blueprint, jsonify, request
from src.errors.error_controller import handle_errors
from src.main.factories.contact_factory import (
    create_contact_factory,
    get_contact_by_number,
    update_contact_factory
)


contact_bp = Blueprint('contact', __name__)


@contact_bp.post('/contact')
def create_contact():
    try:
        data = request.json
        create_contact_factory(data)
        return jsonify(
            {"message": "Contato cadastrado com sucesso!"}, 201
        )
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response['status_code']


@contact_bp.get('/contact/<string:number>')
def check_contact_active_by_number(number):
    try:
        response = get_contact_by_number(number)
        return jsonify(
            {"active": response}, 200
        )
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response['status_code']


@contact_bp.put('/contact/<int:contact_id>')
def update_contact(contact_id):
    try:
        data = request.json
        update_contact_factory(data, contact_id)
        return jsonify(
            {"message": "Contato atualizado com sucesso!"}, 200
        )
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response['status_code']
