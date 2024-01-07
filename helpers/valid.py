from string import whitespace, ascii_uppercase, punctuation
from re import match


TYPES = ['string', 'int', 'char', 'number', 'bool', 'date', 'name']


def is_name(name: str) -> bool:
    for i in name:
        if not i.isalpha():
            return False
    return True


def is_valid_modelname(modelname: str) -> bool:
    invalid: [str] = [j for i in punctuation.split('_') for j in i]

    if len([i for i in modelname if i in whitespace]) > 0:
        return False
    elif len([i for i in modelname if i in invalid]) > 0:
        return False
    elif len(modelname) != len([i for i in modelname if i in ascii_uppercase + '_']):
        return False
    elif modelname.isnumeric():
        return False
    else:
        return True


def is_valid_field(field: str) -> bool:
    pattern = r"^[a-zA-Z]{2,}:(int|string|double|bool)(,[a-zA-Z]{2,}:(int|string|double|bool))*$"
    is_match = match(pattern, field)

    return is_match is not None
