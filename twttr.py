def main():
    tweet=input('Input: ')
    print ('Output:', shorten(tweet))

def shorten(tweet):
    new_tweet=''
    for i in range(len(tweet)):
        if(tweet[i]!='A' and tweet[i]!='a'and tweet[i]!='E'and tweet[i]!='e' and tweet[i]!='I'and tweet[i]!='i'and tweet[i]!='O'and tweet[i]!='o'and tweet[i]!='U'and tweet[i]!='u'):
            new_tweet += tweet[i]

    return new_tweet

if __name__ == '__main__':
    main()
