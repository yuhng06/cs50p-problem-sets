def main():
    question = input('How are you feeling? ')
    question = convert(question)
    print(question)

def convert(feeling):
    ans = feeling .replace(':)','🙂') .replace(':(','🙁')
    return ans

main()
