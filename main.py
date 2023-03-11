def sqrt(D):
    return D ** 0.5

def discrim(a, b, c):
    D = (b**2) - (4 * a * c)
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
    #result = 0
    discrim(a, b, c)
    if(discrim(a, b, c) > 0):
        return two_roots(a, b, c)
    elif(discrim(a, b, c)== 0):
        return one_root(a, b)
    elif(discrim(a, b, c) < 0):
        return False

def init(*args):
    print(args)
    if(len(args) != 3):
        return False
    else:
        return True

def listToInt(args):
    result = []
    for i in args:
        result.append(int(i))
        print(result)
    return result

def main():
    #2, 4, 12
    while(True):
        args = input().split()
        intArgs = listToInt(args)
        if init(intArgs[0]) == False:
            continue
        else:
            break
    result = init(intArgs[0])
    print(result)

main()






