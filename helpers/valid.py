from string import whitespace, ascii_uppercase, punctuation


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
    if field.count(':') != 1:
        print('wrong format for field: \"<fieldName:type>\"')
        return False

    name, _type = field.split(':')

    if not is_valid_modelname(name.upper()):
        print('invalid field name: \"%s\"' % name)
        return False
    elif _type not in TYPES:
        print('field type not in: ', TYPES)
        return False
    else:
        return True
