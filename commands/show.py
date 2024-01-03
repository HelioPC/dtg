from commands.create import INITIALIZED
from helpers.ops import unpack
from helpers.lists import ls_del_occ
from globals.assets import SPLITER


def show(args):
    if INITIALIZED:
        with open('./.dtg/models.dat', 'rb') as fb:
            lines = fb.readlines()
            
            if len(lines) == 0:
                print("no models created")
            else:
                print(ls_del_occ(unpack(lines[0]).split(SPLITER), ''))
        exit(0)
    else:
        print("dtg folder not found")
        exit(1)
