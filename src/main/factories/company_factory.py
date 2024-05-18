from src.errors.http_bad_request_error import HttpBadRequestError
from src.errors.http_not_found_error import HttpNotFoundError
from src.main.models.company import Company
from src.main.database.database import db


def create_company_factory(data):
    name = data.get('name')
    responsible = data.get('responsible')
    email = data.get('email')
    active = data.get('active')

    if not (name and responsible):
        raise HttpBadRequestError(
            'Dados incompletos ou inválidos'
        )

    company = Company(
        name=name,
        responsible=responsible,
        email=email,
        active=active
        )

    db.session.add(company)
    db.session.commit()

    return True


def update_company_factory(data, company_id):
    name = data.get('name')
    responsible = data.get('responsible')
    email = data.get('email')
    active = data.get('active')


    company = Company.query.get(company_id)

    if not company:
        raise HttpNotFoundError(
            "Empresa não encontrada"
        )

    if name:
        company.name = name
    if responsible:
        company.responsible = responsible
    if email:
        company.email = email
    if active:
        company.active = active

    db.session.commit()

    return True
