def main():
    sorted_date = rewrite()
    print(sorted_date)

month = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

def rewrite():
    while True:
        try:
            date = input('Date: ')
            if ('/' in date):
                    x, y, z= date.split('/')
                    x = int(x) #month
                    y = int(y) #day
                    z = int(z) #year
                    if x > 12 or y > 31 or x < 1 or y < 1:
                         raise ValueError
                    else:
                        return f'{z}-{x:02d}-{y:02d}'
            elif (',' in date):
                    x, y, z= date.split(' ')
                    x = month.index(x.title()) + 1
                    y = int(y.strip(','))
                    z = int(z)
                    if y > 31 or y < 1:
                         raise ValueError
                    else:
                        return f'{z}-{x:02d}-{y:02d}'
            else:
                raise ValueError
        except ValueError:
            pass

main()
