from string import whitespace, ascii_uppercase, punctuation


def validate_modelname(modelname: str) -> bool:
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
