import argparse

parser = argparse.ArgumentParser()
a = parser.add_argument('a', type=str)
parser.add_argument('b', type=str)

possible_values = '1234567890+-'
signs = ['+-','++', '-+', '--']

args = parser.parse_args()

for val in args.a:
    if val in possible_values:
        formula = True
    else:
        formula = False

for string in signs:
    if string in args.a:
        formula = False

result = eval(args.a)

if formula:
    print(formula, result)
else:
    print(formula, 'none')