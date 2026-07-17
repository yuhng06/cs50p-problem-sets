def main():
    eqn = input('Expression: ')
    eqn = convert (eqn)

def convert(eqn):
    x, y, z = eqn.split(' ')
    x = float(x)
    z = float(z)
    if (y=='+'):
        print (x+z)
    elif (y=='-'):
        print (x-z)
    elif (y=='*'):
        print (x*z)
    else:
        print (x/z)
    return eqn

main()
