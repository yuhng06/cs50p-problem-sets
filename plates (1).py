def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):

    if len(str) < 2 or len(str) > 6 or str[0].isnumeric() or str[1].isnumeric():
        return False
    elif str.isalpha():
        return True

    i =0
    for i in range(len(str)):
        if str[i].isnumeric():
            break
    for j in range(len(str)):
        if str[i] == '0' or str[j].isnumeric() == False:
            return False
    return True

main()

