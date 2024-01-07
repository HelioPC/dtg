from helpers.valid import is_valid_field
from helpers.model import model_exists, get_model_index
from globals.assets import MODELS_BIN_FILE, SPLITER
from helpers.ops import pack, unpack
from helpers.lists import ls_del_occ


def add(args) -> None:
    if not model_exists(args.modelname):
        print('model \"%s\" does\'nt exists' % args.modelname)
        exit(1)
    elif not is_valid_field(args.field):
        print('field bad format:\n\tusage - "--fields "var:(VALUE)""\n\t\tVALUE = int | string | double')
        exit(1)
    else:
        index = get_model_index(args.modelname, skip=False)

        if index < 0:
            print('model \"%s\" does\'nt exists' % args.modelname)
            exit(1)

        with open(MODELS_BIN_FILE, "rb+") as fb:
            line = fb.read()
            content = ls_del_occ(unpack(line).split(SPLITER), '')
            to_write = ''

            if len(unpack(line)) != 0:
                for i in range(len(content)):
                    if i == index:
                        content[i] = content[i].removeprefix('{')
                        content[i] = content[i].removesuffix('}')
                        content[i] = content[i].split(';')
                        content[i].append(args.field)
                        content[i] = ls_del_occ(content[i], '')
                        content[i] = '{' + ','.join(content[i]) + '}'
                    to_write += content[i] + SPLITER

            fb.seek(0)
            fb.truncate()
            fb.write(pack(to_write))

        print('%s +=> %s' % (args.field, args.modelname))
