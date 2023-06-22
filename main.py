import sys

from AFD import AFD
from AFN import AFN

def main(argv):

    if len(argv) < 2:
        filename = input('Enter the XML file name: ')
    else:
        filename = argv[1]

    afd = input('Is the automaton deterministic? (y/n): ')
    if afd == 'y':
        a = AFD.from_xml(filename)
    else:
        a = AFN.from_xml(filename)
        

    a.quintuple()

    while True:
        line = input('\nEnter the input string: ')
        if line == '	':
            break
        line = line.strip()
        print(f'Input `{line}` is {"" if a.parse(line) else "not "}valid')

if __name__ == "__main__":
    main(sys.argv)
