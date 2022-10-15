from json import dumps, load
from os import mkdir, path

from helpers.lists import ls_del_occ
from helpers.valid import validate_modelname
from helpers.ops import pack, unpack

_INITIALIZED_: bool = path.exists('./.dtg/') and path.exists('./.dtg/models.dat') and path.exists('./.dtg/index.json')
_SPLITER_ = '\x1a\xfe8\xc7\xd0|\xa3*\xb9\x97\xecb\xb3\xa8\r\t}\x85;\x9c\x81\xbdV\xb4\x92\xe9\x82\x98B\xa3+B'


def init(args) -> None:
    global _INITIALIZED_

    try:
        mkdir('./.dtg')
        print("Initializing dtg models repository...")
        _INITIALIZED_ = True
    except FileExistsError:
        print("Repository folder already exists")
        exit(1)
    except PermissionError:
        print("Apparently you don't have permission, try with sudo")
        exit(1)

    try:
        if path.exists('./.dtg/'):
            with open("./.dtg/models.dat", "w+b") as fb:
                fb.close()

            with open("./.dtg/index.json", "w") as fj:
                fj.write(dumps({}, sort_keys=True, indent=4))
                fj.close()

            _INITIALIZED_ = True
            print("Done.")
            exit(0)
        else:
            print("A weird problem just occurred 🤔, try deleting dtg folder and run again")
            exit(1)
    except IOError:
        print("Something went wrong, ups 🤦🏽")
        exit(1)
    exit(0)


def create(args) -> None:
    if _INITIALIZED_:
        if not validate_modelname(args.modelname.upper()):
            print('Invalid name for \'modelname\'')
            exit(1)
        else:
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
                        models[args.modelname.upper()] = models[list(models)[len(models) - 1]] + 1

                    fj.write(dumps(models, sort_keys=True, indent=4))
                    fj.close()

                with open("./.dtg/models.dat", "rb+") as fb:
                    lines = fb.readlines()
                    content = ''

                    if len(lines) != 0:
                        for i in ls_del_occ(unpack(lines[0]).split(_SPLITER_), ''):
                            content += i + _SPLITER_

                    content += '{}' + _SPLITER_

                    fb.seek(0)
                    fb.truncate()
                    fb.write(pack(content))
                    fb.close()

                print("\"%s\" model created" % args.modelname)
                exit(0)
            except IOError:
                print("Something went wrong, ups 🤦🏽")
                exit(1)
    else:
        print("dtg folder not found")
        exit(1)
