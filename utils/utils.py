import uuid


def only_number(value: str) -> str:
    # Remova qualquer caractere não numérico do valor
    value_only_numbers = ''.join(filter(str.isdigit, value))

    return value_only_numbers


def generate_uuid():
    return uuid.uuid4().bytes
