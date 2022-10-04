# This is a sample Python script.
# https://www.mit.edu/~ecprice/wordlist.10000
# https://github.com/centraldedados/nomes_proprios/tree/master/data
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process a list of integers", prog="calc")
    subparsers = parser.add_subparsers(dest="command", required=True)

    soma_parser = subparsers.add_parser('sum', help="Sum all integers")
    mul_parser = subparsers.add_parser('mul', help="Multiply all integers")
    max_parser = subparsers.add_parser('max', help="Returns the largest integer")

    soma_parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    mul_parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    max_parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

    args = parser.parse_args()

    if args.command == 'sum':
        print(sum(args.integers))
    elif args.command == 'max':
        print(max(args.integers))
    elif args.command == 'mul':
        mul = 1
        for i in args.integers:
            mul *= i
        print(mul)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
