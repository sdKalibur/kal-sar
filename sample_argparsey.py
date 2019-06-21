import argparse


parser = argparse.ArgumentParser(description='Process some arguments.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='A helpful text line.')

parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_intermixed_args()
print(args.accumulate(args.integers))
