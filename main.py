import math

sqrt = math.sqrt

# def sqrt(D):
#     return D ** 0.5

def discrim(a, b, c):
    D = (b**2) - (4 * a * c)
    print(D)
    return D

def two_roots(a, b, D):
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    return [x1, x2]

def one_root(b, a):
    result = -b / 2*a
    return result

def get_roots(a, b, c):
    print(a, b, c)
    D = discrim(a, b, c)
    if(D > 0):
        return two_roots(a, b, D)
    elif(D == 0):
        return one_root(a, b)
    elif(D < 0):
        return False

def prepareArg(arg):
    return float(arg)


def main():
    #2, 4, 12 = False
    #2, 5, -3 = -3, 1/2
    a = prepareArg(input())
    b = prepareArg(input())
    c = prepareArg(input())
    result = get_roots(a, b, c)
    print(result)

main()






