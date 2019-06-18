def sum(*args):
    sum = 0
    for _ in args:
        sum += _
    print(sum)
    return sum

sum(1,2,3,4,5,6)