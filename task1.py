import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a", type=str)
args = parser.parse_args()

list = list(''.join(args.a))

a = int(list[0])
b = str(list[1])
c = int(list[2])

dict = {'+': a + c, '-': a - c, '*': a * c, '/': a / c}

print(dict[list[1]])