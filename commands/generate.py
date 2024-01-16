from faker import Faker
from json import dumps
from sys import exit

from helpers.ops import unpack
from globals.assets import MODELS_BIN_FILE, SPLITER
from helpers.lists import ls_del_occ
from helpers.model import get_model_index
from helpers.valid import is_valid_modelname
from helpers.ops import most_similar
from globals.assets import TYPES_OF_FIELDS, LOCALES


def generate(args):
    if not is_valid_modelname(args.modelname.upper()):
        print("Invalid name for 'modelname'")
        exit(1)
    else:
        model_as_dict = extract_model(args.modelname)
        rows = []

        if len(model_as_dict) == 0:
            print("program error Extract")
            exit(1)
        
        results_as_dict = model_as_dict.copy()

        for _ in range(args.count):
            for field in model_as_dict:
                results_as_dict[field] = get_data_by_field(field, fieldtype=model_as_dict[field], force=args.force, langs=args.lang)

            rows.append(results_as_dict.copy())
        
        if args.output == 'stdout':
            for row in rows:
                print(row)
        else:
            try:
                output_filename = './'
                output_data = {}

                if args.output.endswith('.json'):
                    output_filename += args.output
                else:
                    output_filename += args.output + '.json'

                with open(output_filename, "w+") as f:
                    for i in range(len(rows)):
                        output_data[i] = rows[i]

                    f.write(dumps(output_data, sort_keys=True, indent=4))
            except PermissionError:
                print('Apparently you don\'t have permission, try with sudo')
                exit(1)
            except IOError:
                print("Something went wrong, ups 🤦🏽")
                exit(1)

    exit(0)


def extract_model(modelname: str) -> dict:
    model_index = get_model_index(modelname.upper(), skip=False)

    if model_index < 0:
        print('model "%s" does\'nt exists' % modelname)
        exit(1)

    model_as_dict = {}

    with open(MODELS_BIN_FILE, "rb+") as fb:
        line = fb.read()
        content = ls_del_occ(unpack(line).split(SPLITER), '')

        if len(unpack(line)) != 0:
            for i in range(len(content)):
                if i == model_index:
                    content[i] = content[i].removeprefix('{')
                    content[i] = content[i].removesuffix('}')

                    for field in content[i].split(','):
                        field = field.split(':')
                        model_as_dict[field[0]] = field[1]

    return model_as_dict


def get_data_by_field(fieldname: str, fieldtype: str='', force: bool=False, langs: list[str]=['pt_PT', 'en_US']) -> str:
    if fieldname == '' or fieldtype == '':
        print('Invalid field')
        exit(1)
    
    for lang in langs:
        if lang not in LOCALES:
            print('Invalid language\nAvailable languages: %s' % LOCALES)
            exit(1)

    fake = Faker(locale=langs)
    field_generators = {
        'name': fake.name,
        'age': lambda: fake.random_int(min=1, max=100),
        'address': fake.address,
        'city': fake.city,
        'country': fake.country,
        'email': fake.email,
        'phone': fake.phone_number,
        'company': fake.company,
        'job': fake.job,
        'date': fake.date,
    }

    field_similarity = most_similar(fieldname.lower(), TYPES_OF_FIELDS)
    refined_fieldname = field_similarity[0]
    similarity_value = field_similarity[1]

    if similarity_value >= 0.7 and refined_fieldname in field_generators:
        return field_generators[refined_fieldname]()
    elif not force:
        return fake.text()

    if fieldtype == 'bool':
        return fake.boolean()
    elif fieldtype == 'int':
        return fake.random_int(min=0, max=1000000000)
    elif fieldtype == 'double':
        return fake.pyfloat(right_digits=2, positive=True)
    else:
        return fake.text(max_nb_chars=50)
