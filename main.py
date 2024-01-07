# This is a sample Python script.
# https://www.mit.edu/~ecprice/wordlist.10000
# https://github.com/centraldedados/nomes_proprios/tree/master/data
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import argparse

from commands.create import init, create
from commands.generate import generate
from commands.show import show
from commands.add import add
from globals.assets import CURRENT_VERSION


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A command line utility to generate dummy data', prog='dtg')
    parser.add_argument('-v', '--version', help='Display the current version', action="store_true")

    subparsers = parser.add_subparsers(dest='command', help='command help')

    init_parser = subparsers.add_parser('init', help='Initialize a dtg repository')
    init_parser.set_defaults(func=init)

    show_parser = subparsers.add_parser('show', help='Show all dtg models created')
    show_parser.set_defaults(func=show)

    create_parser = subparsers.add_parser('create', help='Creates a new dtg model')
    create_parser.add_argument('modelname', help='name of the model')
    create_parser.add_argument('--fields', default='', type=str, help='fields of the model')
    create_parser.set_defaults(func=create)

    add_parser = subparsers.add_parser(
        'add',
        help='Add a field to a model',
        description='Insert a new field into a model'
    )
    add_parser.add_argument('field', help='field')
    add_parser.add_argument('modelname', help='modelname')
    add_parser.set_defaults(func=add)

    generate_parser = subparsers.add_parser(
        'generate',
        help='Generate the dummy',
        description='Generate the dummy data based on a model'
    )
    generate_parser.add_argument('modelname', help='modelname')
    generate_parser.add_argument(
        '-c', '--count', default=1, type=int,
        help='number of records to generate'
    )
    generate_parser.add_argument(
        '-o', '--output', default='stdout', type=str,
        help='output file'
    )
    generate_parser.add_argument(
        '-k', '--keep', default=False, action='store_true',
        help='keep the generated data in the repository'
    )
    generate_parser.set_defaults(func=generate)

    args = parser.parse_args()

    if args.version:
        print("dtg version %s" % CURRENT_VERSION)
    else:
        args.func(args)

    exit(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
