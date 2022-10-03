# This is a sample Python script.
# https://www.mit.edu/~ecprice/wordlist.10000
# https://github.com/centraldedados/nomes_proprios/tree/master/data
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

if __name__ == '__main__':
    args = parser.parse_args()
    print(args.accumulate(args.integers))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
