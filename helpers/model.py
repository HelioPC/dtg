from json import load

from globals.status import INITIALIZED
from globals.assets import INDEX_JSON_FILE, MODELS_BIN_FILE, SPLITER
from helpers.ops import unpack
from helpers.lists import ls_del_occ


def model_exists(model: str) -> bool:
    if not INITIALIZED:
        return False
    else:
        with open(INDEX_JSON_FILE, 'r') as fj:
            models = load(fj)

            with open(MODELS_BIN_FILE, "rb+") as fb:
                line = fb.read()

                return (
                        model.upper() in models and
                        len(ls_del_occ(unpack(line).split(SPLITER), '')) == len(models)
                )


def get_model_index(model: str, skip=True) -> int:
    if skip and not model_exists(model):
        return -1
    else:
        with open(INDEX_JSON_FILE, 'r') as fj:
            models = load(fj)
            try:
                return models[model.upper()]
            except KeyError:
                return -1
