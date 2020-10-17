largest=None
smallest=None

while True:
    num=input("enter a number")
    new_num=float(num)

    try:
        sval=float(num)
    except:
        print('invalid input')
        continue

    if smallest==None:
        smallest=num
        print('first input',smallest)
    elif num < smallest :
        print(num,'<',smallest)
        smallest=num
    else:
        print(num,'>',smallest)
print('minimum',smallest)

