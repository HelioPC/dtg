# This is a sample Python script.
# https://www.mit.edu/~ecprice/wordlist.10000
# https://github.com/centraldedados/nomes_proprios/tree/master/data
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import argparse
from create import init

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A command line utility to generate dummy data", prog="dtg")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser('init', help="Initialize a dtg repository")

    # init_parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

    args = parser.parse_args()

    if args.command == 'init':
        init()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
