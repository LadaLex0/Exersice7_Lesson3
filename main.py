x = int(input('Write a year: '))
if x % 4 != 0:
    print('Year isn\'t leap')
elif x % 100 == 0 and x % 400 == 0:
        print('Year isn\'t leap')
else: print('Year is leap')
