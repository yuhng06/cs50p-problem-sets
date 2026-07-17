import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif sys.argv[1].endswith(".py"):
    try:
        with open (sys.argv[1]) as file:
            count = 0
            for line in file:
                if line.strip()== '' or line.strip().startswith('#'):
                    continue
                count +=1
        print(count)
    except FileNotFoundError:
        sys.exit ('File does not exist')
else:
    sys.exit('Not a python file')
