from emoji import emojize

def main():
    response = input('Input: ')
    print (f'Output: {emojize(response, language='alias')}')

main()
