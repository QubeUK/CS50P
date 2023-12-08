total = 0
while total < 50:
    coin = int(input("Insert Coin: "))
    match coin:
        case 5 | 10 | 25:
            total = total + coin
            if total <50:
                print("Amount Due:",50-total)
            else:
                print("Change Owed:", total-50)
        case _:
            print("Amount Due:",50-total)




