from helpers.ops import unpack
from faker import Faker
from globals.assets import MODELS_BIN_FILE, SPLITER
from helpers.lists import ls_del_occ
from helpers.model import get_model_index
from helpers.valid import is_valid_modelname
from helpers.ops import most_similar
from globals.assets import TYPES_OF_FIELDS


def generate(args):
    if not is_valid_modelname(args.modelname.upper()):
        print("Invalid name for 'modelname'")
        exit(1)
    else:
        model_as_dict = extract_model(args.modelname)

        if len(model_as_dict) == 0:
            print("program error Extract")
            exit(1)

        for _ in range(args.count):
            for field in model_as_dict:
                model_as_dict[field] = get_data_by_field(field)

            print(model_as_dict)

    exit(0)


def extract_model(modelname: str) -> dict:
    model_index = get_model_index(modelname.upper(), skip=False)

    if model_index < 0:
        print('model "%s" does\'nt exists' % modelname)
        exit(1)

    model_as_dict = {}

    with open(MODELS_BIN_FILE, "rb+") as fb:
        lines = fb.readlines()
        content = ls_del_occ(unpack(lines[0]).split(SPLITER), "")

        if len(lines) != 0:
            for i in range(len(content)):
                if i == model_index:
                    content[i] = content[i].removeprefix("{")
                    content[i] = content[i].removesuffix("}")

                    for field in content[i].split(","):
                        field = field.split(":")
                        model_as_dict[field[0]] = field[1]

    return model_as_dict


def get_data_by_field(fieldname: str) -> str:
    fake = Faker()

    refined_fieldname = most_similar(fieldname.lower(), TYPES_OF_FIELDS)

    if refined_fieldname == "name":
        return fake.name()
    elif refined_fieldname == "age":
        return fake.random_int(min=1, max=100)
    elif refined_fieldname == "address":
        return fake.address()
    elif refined_fieldname == "city":
        return fake.city()
    elif refined_fieldname == "country":
        return fake.country()
    elif refined_fieldname == "email":
        return fake.email()
    elif refined_fieldname == "phone":
        return fake.phone_number()
    elif refined_fieldname == "company":
        return fake.company()
    elif refined_fieldname == "job":
        return fake.job()
    elif refined_fieldname == "date":
        return fake.date()
    else:
        return fake.text()
