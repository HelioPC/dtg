from commands.create import INITIALIZED
from helpers.ops import unpack
from helpers.lists import ls_del_occ
from globals.assets import SPLITER


def show(args):
    if INITIALIZED:
        with open('./.dtg/models.dat', 'rb') as fb:
            line = fb.read()
            
            if len(unpack(line)) == 0:
                print("no models created")
            else:
                print(ls_del_occ(unpack(line).split(SPLITER), ''))
        exit(0)
    else:
        print("dtg folder not found")
        exit(1)
