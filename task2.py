import argparse

parser = argparse.ArgumentParser()
parser.add_argument('a', type=str)
parser.add_argument('b', type=int)
parser.add_argument('c', type=int)

args = parser.parse_args()

dict = {'add': args.b + args.c, 'sub': args.b - args.c,
		'mul': args.b * args.c, 'div': args.b / args.c}
print(dict[args.a])