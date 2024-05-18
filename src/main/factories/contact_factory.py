from src.errors.http_bad_request_error import HttpBadRequestError
from src.errors.http_not_found_error import HttpNotFoundError
from src.errors.http_unauthorized_error import HttpUnauthorizedError
from src.main.models.contact import Contact
from src.main.models.company import Company
from src.main.database.database import db


def create_contact_factory(data):
    company_id = data.get('company_id')
    number = data.get('number')
    active = data.get('active')

    if not (company_id and number):
        raise HttpBadRequestError(
            'Dados incompletos ou inválidos'
        )

    company = Company.query.get(company_id)

    if not company:
        raise HttpNotFoundError(
            "Empresa não encontrada"
        )

    contact = Contact(
        company_id=company_id,
        number=number,
        active=active
        )

    db.session.add(contact)
    db.session.commit()

    return True


def get_contact_by_number(number):
    contact = Contact.query.filter_by(number=number).first()
    if not contact:
        raise HttpNotFoundError(
            "Contato não encontrado"
        )

    company = Company.query.get(contact.company_id)

    if not (company.active and contact.active):
        raise HttpUnauthorizedError(
            "Contato inativo"
            )

    return True


def update_contact_factory(data, contact_id):
    company_id = data.get('company_id')
    number = data.get('number')
    active = data.get('active')

    contact = Contact.query.get(contact_id)

    if not contact:
        raise HttpNotFoundError(
            "Contato não encontrado"
        )

    if company_id:
        company_id = Company.query.get(company_id)
        if not company_id:
            raise HttpNotFoundError(
                "Empresa não encontrada"
            )
        contact.company_id = company_id
    if number:
        contact.number = number
    if active:
        contact.active = active

    db.session.commit()

    return True
