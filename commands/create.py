from json import dumps, load
from os import mkdir, path
from sys import exit

from helpers.lists import ls_del_occ
from helpers.valid import is_valid_modelname, is_valid_field
from helpers.ops import pack, unpack
from globals.status import INITIALIZED
from globals.assets import SPLITER


def init(args) -> None:
    try:
        if not INITIALIZED:
            mkdir('./.dtg')
            print("Initializing dtg models repository...")
        else:
            print("Repository folder already exists")
            exit(1)
        
        mkdir('./.dtg/.keep')
    except FileExistsError:
        print("Repository folder already exists")
        exit(1)
    except PermissionError:
        print("Apparently you don't have permission, try with sudo")
        exit(1)

    try:
        if path.exists('./.dtg/'):
            with open("./.dtg/models.dat", "w+b") as fb:
                pass

            with open("./.dtg/index.json", "w") as fj:
                fj.write(dumps({}, sort_keys=True, indent=4))

            with open("./.dtg/.keep/data.json", "w") as fj:
                fj.write(dumps({}, sort_keys=True, indent=4))

            print("Done.")
            exit(0)
        else:
            print("A weird problem just occurred 🤔, try deleting dtg folder and run again")
            exit(1)
    except IOError:
        print("Something went wrong, ups 🤦🏽")
        exit(1)


def create(args) -> None:
    if INITIALIZED:
        if not is_valid_modelname(args.modelname.upper()):
            print('Invalid name for \'modelname\'')
            exit(1)
        else:
            if len(args.fields) != 0:
                if not is_valid_field(args.fields):
                    print('field bad format:\n\tusage - "--fields "var:(VALUE)""\n\t\tVALUE = int | string | double')
                    exit(1)
            try:
                with open("./.dtg/index.json", "r+") as fj:
                    models = load(fj)

                    if args.modelname in models:
                        print("modelname \"%s\" already exists" % args.modelname)
                        exit(1)

                    fj.seek(0)
                    fj.truncate()
                    if len(models) == 0:
                        models[args.modelname.upper()] = 0
                    else:
                        models[args.modelname.upper()] = len(models)

                    fj.write(dumps(models, sort_keys=True, indent=4))

                with open("./.dtg/models.dat", "rb+") as fb:
                    line = fb.read()
                    content = ''

                    if len(unpack(line)) != 0:
                        for i in ls_del_occ(unpack(line).split(SPLITER), ''):
                            content += i + SPLITER

                    content += '{%s}' % (args.fields) + SPLITER

                    fb.seek(0)
                    fb.truncate()
                    fb.write(pack(content))

                print("\"%s\" model created" % args.modelname)
                exit(0)
            except IOError:
                print("Something went wrong, ups 🤦🏽")
                exit(1)
    else:
        print("dtg folder not found")
        exit(1)
