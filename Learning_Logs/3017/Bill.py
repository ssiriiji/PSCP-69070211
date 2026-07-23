"""this is main"""
def main():
    """this is code"""
    money = int(input())

    if money <= 500:
        service = money + 50
        vat = service * 7/100
        sum_money = service + vat
        print(f"{sum_money:.2f}")
    elif 500 < money < 10000:
        service = money + (money * 10/100)
        vat = service * 7/100
        sum_money = service + vat
        print(f"{sum_money:.2f}")
    else:
        service = money + 1000
        vat = service * 7/100
        sum_money = service + vat
        print(f"{sum_money:.2f}")
main()
