from argparse import ArgumentParser
from sys import stdin

from AFD import AFD

def main():
    arg_parser = ArgumentParser(prog='fap', description='Finite automata parser')
    arg_parser.add_argument('-i', '--ifile', required=True)

    args = arg_parser.parse_args()

    afd = AFD.from_xml(args.ifile)

    for line in stdin:
        line = line.strip()
        print(f'Input `{line}` is {"" if afd.parse(line) else "not "}valid')

if __name__ == "__main__":
    main()
