def main():
    unpaid = 50
    while (unpaid>0):
        print ('Amount Due:',unpaid)
        paid = int(input('Insert Coin: '))
        if (paid ==5 or paid == 10 or paid ==25):
            unpaid = unpaid - paid
        if (unpaid<=0):
            print ('Change Owed:', -unpaid)


main()
