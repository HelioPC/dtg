from create import _INITIALIZED_, _SPLITER_

from helpers.ops import unpack
from helpers.lists import ls_del_occ


def show(args):
    if _INITIALIZED_:
        with open('./.dtg/models.dat', 'rb') as fb:
            lines = fb.readlines()
            print(ls_del_occ(unpack(lines[0]).split(_SPLITER_), ''))
        exit(0)
    else:
        print("dtg folder not found")
        exit(1)
