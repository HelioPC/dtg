from helpers.valid import is_valid_field
from helpers.model import model_exists, get_model_index
from globals.assets import MODELS_BIN_FILE, SPLITER
from helpers.ops import pack, unpack
from helpers.lists import ls_del_occ


USAGE = 'usage: dtg add <FIELD> <MODELNAME>'


def add(args) -> None:
    if not model_exists(args.modelname):
        print('model \"%s\" does\'nt exists' % args.modelname)
        exit(1)
    elif not is_valid_field(args.field):
        exit(1)
    else:
        index = get_model_index(args.modelname, skip=False)

        if index < 0:
            print('model \"%s\" does\'nt exists' % args.modelname)
            exit(1)

        with open(MODELS_BIN_FILE, "rb+") as fb:
            lines = fb.readlines()
            content = ls_del_occ(unpack(lines[0]).split(SPLITER), '')
            to_write = ''

            if len(lines) != 0:
                for i in range(len(content)):
                    if i == index:
                        content[i] = content[i].removeprefix('{')
                        content[i] = content[i].removesuffix('}')
                        content[i] = content[i].split(';')
                        content[i].append(args.field)
                        content[i] = ls_del_occ(content[i], '')
                        content[i] = '{' + ';'.join(content[i]) + '}'
                    to_write += content[i] + SPLITER

            fb.seek(0)
            fb.truncate()
            fb.write(pack(to_write))
            fb.close()

        print('%s +=> %s' % (args.field, args.modelname))
