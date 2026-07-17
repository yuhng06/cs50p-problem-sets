def main():
    camel=input('camelCase: ')
    print ('snake_case:', snakecased(camel))
def snakecased(str):
    snaked=''
    for i in range(len(str)):
        if(str[i].isupper()):
            snaked = snaked + '_'
            snaked = snaked + str[i].lower()
        else:
            snaked = snaked + str[i]
    return snaked
main()

