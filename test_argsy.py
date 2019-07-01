# def sum(*args):
# #     sum = 0
# #     for _ in args:
# #         sum += _
# #     print(sum)
# #     return sum
# #
# # sum(1,2,3,4,5,6)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("testArg")

print(parser.parse_args())
args = parser.parse_args()
print(args)